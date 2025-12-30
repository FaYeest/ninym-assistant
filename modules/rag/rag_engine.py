import os
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
from docx import Document  # Library untuk baca Word
from colorama import Fore

class RagEngine:
    def __init__(self, data_dir="data", persist_dir="core/chroma_db"):
        print(f"{Fore.BLUE}[RAG] Initializing Local Memory (Vector DB)...")
        
        # 1. Setup ChromaDB (Local Persistent)
        # Check path first to avoid relative path issues
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        real_persist_dir = os.path.join(base_dir, persist_dir)
        real_data_dir = os.path.join(base_dir, data_dir)
        
        self.chroma_client = chromadb.PersistentClient(path=real_persist_dir)
        
        print(f"{Fore.BLUE}[RAG] Loading Embedding Model (all-MiniLM-L6-v2)...")
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        
        self.collection = self.chroma_client.get_or_create_collection(name="ninym_knowledge")
        self.data_dir = real_data_dir

    def _read_file(self, file_path, ext):
        """Helper function to read different file types."""
        text_content = ""
        try:
            if ext == '.pdf':
                reader = PdfReader(file_path)
                for page in reader.pages:
                    text = page.extract_text()
                    if text: text_content += text + "\n"
            
            elif ext == '.docx':
                doc = Document(file_path)
                for para in doc.paragraphs:
                    text_content += para.text + "\n"
            
            # Treat code files as plain text
            elif ext in ['.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.env', '.c', '.cpp', '.h', '.hpp']:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    text_content = f.read()
            
            return text_content
            
        except Exception as e:
            print(f"{Fore.RED}[RAG] Error reading {file_path}: {e}")
            return ""

    def ingest_data(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            return "Folder data kosong."

        print(f"{Fore.YELLOW}[RAG] Scanning documents in '{self.data_dir}'...")
        
        # Added C/C++ support
        supported_exts = ['.txt', '.pdf', '.docx', '.md', '.py', '.js', '.html', '.css', '.json', '.c', '.cpp', '.h', '.hpp']
        files = [f for f in os.listdir(self.data_dir) if any(f.endswith(ext) for ext in supported_exts)]
        
        if not files:
            return "Tidak ada file yang didukung di folder data."

        documents = []
        metadatas = []
        ids = []
        doc_count = 0

        for filename in files:
            file_path = os.path.join(self.data_dir, filename)
            ext = os.path.splitext(filename)[1].lower()
            
            # Read Content
            text_content = self._read_file(file_path, ext)
            
            if not text_content.strip():
                continue
            
            # Simple Chunking (500 chars overlap 50)
            chunk_size = 500
            chunks = [text_content[i:i+chunk_size] for i in range(0, len(text_content), chunk_size-50)]
            
            for idx, chunk in enumerate(chunks):
                if len(chunk) < 50: continue 
                
                doc_id = f"{filename}_chunk_{idx}"
                
                # Check duplicate (Simple check by ID)
                # In production, maybe check by content hash is better
                existing = self.collection.get(ids=[doc_id])
                if existing['ids']:
                    continue

                documents.append(chunk)
                metadatas.append({"source": filename, "type": ext})
                ids.append(doc_id)
                doc_count += 1
        
        if documents:
            print(f"{Fore.YELLOW}[RAG] Embedding {len(documents)} chunks... (This might take a while)")
            embeddings = self.embedder.encode(documents).tolist()
            
            self.collection.add(
                documents=documents,
                embeddings=embeddings,
                metadatas=metadatas,
                ids=ids
            )
            return f"Sukses! {doc_count} potongan informasi baru dari {len(files)} file tersimpan."
        else:
            return "Semua dokumen sudah tersimpan sebelumnya. Tidak ada yang baru."

    def search(self, query, n_results=3):
        print(f"{Fore.MAGENTA}[RAG] Recall memory for: '{query}'...")
        query_embed = self.embedder.encode([query]).tolist()
        
        results = self.collection.query(
            query_embeddings=query_embed,
            n_results=n_results
        )
        
        if not results['documents'] or not results['documents'][0]:
            return None
            
        knowledge_text = ""
        for i, doc in enumerate(results['documents'][0]):
            meta = results['metadatas'][0][i]
            source = meta['source']
            knowledge_text += f"- [{source}] {doc}\n"
            
        return knowledge_text

if __name__ == "__main__":
    rag = RagEngine()
    print(rag.ingest_data())
    q = input("Search Local Data: ")
    print(rag.search(q))