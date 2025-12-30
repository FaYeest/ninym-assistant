import requests
from bs4 import BeautifulSoup
from ddgs import DDGS
from colorama import Fore
import concurrent.futures

class WebSearch:
    def __init__(self):
        self.ddgs = DDGS()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def _scrape_url(self, url):
        """Membuka URL dan mengambil teks utamanya (Deep Research)."""
        try:
            print(f"{Fore.LIGHTBLACK_EX}[TOOL] Reading: {url[:40]}...")
            response = requests.get(url, headers=self.headers, timeout=5)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Hapus elemen pengganggu (Script, Style, Navigasi)
            for script in soup(["script", "style", "nav", "header", "footer", "aside"]):
                script.decompose()
            
            # Ambil teks
            text = soup.get_text(separator=' ', strip=True)
            
            # Potong jika terlalu panjang (Hemat token)
            return text[:1500] + "..." if len(text) > 1500 else text
            
        except Exception as e:
            return f"[Gagal membaca konten: {e}]"

    def read_url(self, url):
        """Public method untuk membaca satu URL spesifik."""
        print(f"{Fore.MAGENTA}[TOOL] Direct Reading: {url}...")
        return self._scrape_url(url)

    def search(self, query, max_results=3, deep_search=True):
        """
        Mode Deep Search: Mencari URL lalu mengunjungi isinya.
        """
        print(f"{Fore.MAGENTA}[TOOL] Deep Searching: '{query}'...")
        try:
            # 1. Cari Link (Ambil dikit aja biar gak context overflow)
            # Safesearch set to 'off' for wider/unfiltered results
            # Region set to 'id-id' for Indonesian context relevance
            raw_results = list(self.ddgs.text(query, region='id-id', max_results=3, backend="api", safesearch="off"))
            
            if not raw_results:
                return "Maaf, aku gak nemu link yang relevan."
            
            # 2. Filter Link Sampah (Gambar, Sosmed, Wallpaper)
            blocked_domains = [
                "pinterest", "tenor", "youtube", "tiktok", "instagram", "facebook", 
                "twitter", "wallpaper", "uhdpaper", "stock", "shutterstock"
            ]
            
            clean_results = []
            for res in raw_results:
                url = res.get('href', '').lower()
                if not any(bad in url for bad in blocked_domains):
                    clean_results.append(res)
                if len(clean_results) >= max_results:
                    break
            
            if not clean_results:
                # Kalau semua ke-filter, terpaksa ambil yang ada
                clean_results = raw_results[:max_results]

            final_summary = "Berikut hasil Deep Research dari internet:\n\n"
            
            # 3. Visit Link Terpilih
            urls = [r.get('href') for r in clean_results]
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
                contents = list(executor.map(self._scrape_url, urls))
            
            # 3. Gabungkan Hasil
            for i, res in enumerate(clean_results):
                title = res.get('title', 'No Title')
                url = res.get('href', '')
                snippet = res.get('body', '')
                full_content = contents[i]
                
                # Jika scraping gagal/kosong, pakai snippet bawaan
                content_to_use = full_content if len(full_content) > 100 else snippet
                
                final_summary += f"### {i+1}. {title}\nSOURCE: {url}\nCONTENT: {content_to_use}\n\n"
                
            return final_summary
            
        except Exception as e:
            print(f"{Fore.RED}[SEARCH ERROR] {e}")
            return "Aduh, sistem deep search error. Coba lagi ya."

if __name__ == "__main__":
    ws = WebSearch()
    print(ws.search("Anime Sousou no Frieren"))