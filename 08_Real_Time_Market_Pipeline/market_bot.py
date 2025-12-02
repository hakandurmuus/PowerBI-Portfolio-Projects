import random
import pyodbc
from datetime import datetime
import time

# --- AYARLAR ---
usd = 39.00
eur = 39.50
gbp = 56.10
server = 'YOUR_SERVER_NAME_HERE' 
database = 'BorsaDB' 

print("🚀 Borsa Robotu Başlatılıyor...")

try:
    conn = pyodbc.connect(
        f'Driver={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    print("✅ SQL Bağlantısı Başarılı!")

except Exception as e:
    print(f"❌ Bağlantı Hatası: {e}")
    exit()

try:
    while True:
        now = datetime.now()
        
        # 1. USD SİMÜLASYONU
        usd = usd + random.uniform(-0.10, 0.10)
        
        # 2. EUR SİMÜLASYONU
        eur = eur + random.uniform(-0.15, 0.15)
        
        # 3. GBP SİMÜLASYONU 
        gbp = gbp + random.uniform(-5.0, 5.0)

        sql = "INSERT INTO CanliBorsa (Symbol, Price, EventTime) VALUES (?, ?, ?)"
        cursor.execute(sql, ('USD', round(usd, 4), now))
        cursor.execute(sql, ('EUR', round(eur, 4), now))
        cursor.execute(sql, ('GBP', round(gbp, 2), now))
        
        conn.commit()

        # Log Bilgisi
        print(f"Update: {now.strftime('%H:%M:%S')} | USD: {usd:.2f} | EUR: {eur:.2f} | GBP: {gbp:.2f}")

        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 Robot Durduruldu. Bağlantı kapatılıyor...")
    conn.close()
    print("👋 Güle güle.")
    