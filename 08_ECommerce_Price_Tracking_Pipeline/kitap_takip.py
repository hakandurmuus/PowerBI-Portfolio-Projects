import requests
from bs4 import BeautifulSoup
import pyodbc
from datetime import datetime
import time
import random

server = 'YOUR_SERVER_NAME' 
database = 'Production'

urunler = [
    {
        "ad": "Simyacı", 
        "link": "https://www.kitapyurdu.com/kitap/simyaci-ciltsiz/27328.html&filter_name=S%C4%B0MYACI" 
    },
    {
        "ad": "1984", 
        "link": "https://www.kitapyurdu.com/kitap/1984/691418.html&filter_name=1984" 
    },
    {
        "ad": "Şeker Portakalı", 
        "link": "https://www.kitapyurdu.com/kitap/seker-portakali-ciltsiz/10139.html&filter_name=seker+portakali" 
    }
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("📚 Kitap Fiyat Takip Ajanı Başlatıldı...")

try:
    conn = pyodbc.connect(
        f'Driver={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    print("✅ SQL Bağlantısı Kuruldu ve Hazır.")

except Exception as e:
    print(f"❌ Kritik Bağlantı Hatası: {e}")
    exit()

try:
    while True:
        now = datetime.now()

        for urun in urunler:
            try:
                response = requests.get(urun['link'], headers=headers)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, "html.parser")
                    fiyat_etiketi = soup.find("div", {"class": "price__item"})
                    
                    if fiyat_etiketi:
                        raw_price = fiyat_etiketi.text
                        clean_price = raw_price.replace(".", "").replace(",", ".").replace("TL", "").strip()
                        real_price = float(clean_price)

                        noise = random.uniform(-5.0, 5.0) 
                        final_price = real_price + noise

                        sql = "INSERT INTO ProductPrice (ProductName, SiteName, Price, EventTime) VALUES (?, ?, ?, ?)"
                        values = (urun['ad'], 'Kitapyurdu', final_price, now)
                        cursor.execute(sql, values)
                        conn.commit()
                        
                        print(f"✅ {urun['ad']} Fiyatı: {final_price:.2f} TL (Gerçek: {real_price})")
                    else:
                        print(f"⚠️ {urun['ad']} için fiyat etiketi bulunamadı.")
                else:
                    print(f"❌ Siteye erişilemedi: {urun['ad']} (Kod: {response.status_code})")
            
            except Exception as e:
                print(f"❌ Hata ({urun['ad']}): {e}")

        print(f"⏳ Tur bitti. Bekleniyor... ({now.strftime('%H:%M:%S')})")
        time.sleep(10)

except KeyboardInterrupt:
    print("\n🛑 Ajan durduruldu.")
    conn.close()