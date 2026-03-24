###  E-Commerce Price Tracking Pipeline (Canlı Fiyat Takip Sistemi) 🚀
Python (Web Scraping), SQL ve Power BI entegrasyonu ile oluşturulmuş, rakip fiyat analizi sağlayan otomasyon projesi.

**🎯 İş Problemi:**
E-ticaret sitelerindeki (Kitapyurdu vb.) ürün fiyatlarını anlık olarak takip etmek, fiyat değişimlerini veritabanında loglamak ve rekabet avantajı sağlamak için canlı dashboard oluşturmak.

**🛠️ Mimari ve Teknolojiler:**
* **Python (Scraping & ETL):** 'BeautifulSoup' ve 'Requests' kütüphaneleri ile web sitelerinden veri kazındı. Anti-bot engelleri için 'User-Agent' rotasyonu uygulandı.
* **Data Simulation:** Veri akışını test etmek ve dashboard tepkisini ölçmek için fiyatlara mikro-simülasyon (Jitter) uygulandı.
* **SQL Server:** 'NVARCHAR' ve 'DECIMAL' veri tipleri ile optimize edilmiş veritabanı şeması.
* **Power BI:** DirectQuery ile canlı veri akışı görselleştirildi.

![Price Tracking Dashboard](08_Real_Time_Market_Pipeline/screenshot.png)
