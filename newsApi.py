import requests

API_KEY = "57e8d496ef2e4c53a5fa13a390e43cd8"

kategori_berita = {
    "1": "teknologi",
    "2": "bisnis",
    "3": "olahraga",
    "4": "kesehatan",
    "5": "sains"
}

def get_top_5_news(keyword):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": keyword,        # gunakan keyword pencarian, bukan kategori
        "language": "id",    # filter berita berbahasa Indonesia
        "pageSize": 5,
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        articles = data.get("articles", [])
        if articles:
            for i, article in enumerate(articles, start=1):
                print(f"{i} - {article['title']}")
        else:
            print("Tidak ada berita ditemukan untuk kategori ini.")
    else:
        print("Gagal mengambil data. Periksa API key atau jaringan.")

def main():
    print("Selamat datang, mau tahu berita apa hari ini?")
    print("[1] Berita seputar teknologi")
    print("[2] Berita seputar bisnis")
    print("[3] Berita seputar olahraga")
    print("[4] Berita seputar kesehatan")
    print("[5] Berita seputar science")

    pilihan = input("Ketik pilihan Anda [1/2/3/4/5] : ").strip()

    if pilihan in kategori_berita:
        keyword = kategori_berita[pilihan]
        print(f"\nBerikut adalah top 5 berita Indonesia seputar {keyword}:\n")
        get_top_5_news(keyword)
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1–5.")

if __name__ == "__main__":
    main()
