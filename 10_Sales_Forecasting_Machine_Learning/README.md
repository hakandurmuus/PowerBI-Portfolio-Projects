### 10. Sales Forecasting with Machine Learning (Satış Tahminleme) 🤖
Geçmiş satış verilerini kullanarak gelecekteki ciro trendlerini tahmin eden Makine Öğrenmesi projesi.

**🎯 İş Problemi:**
Şirketin günlük satış verilerindeki dalgalanmalardan (Noise) arındırılmış **ana büyüme trendini** tespit etmek ve gelecek 30 gün için ciro projeksiyonu oluşturmak.

**🛠️ Kullanılan Teknikler:**
* **Python (Scikit-Learn):** 'LinearRegression' algoritması kullanılarak zaman serisi üzerinde trend analizi yapıldı.
* **Feature Engineering:** Tarih verisi 'Ordinal' sayısal formata dönüştürülerek modele uygun hale getirildi.
* **SQL & Power BI Entegrasyonu:** Python ile üretilen tahmin verileri SQL veritabanına geri yazıldı (Write-Back) ve Power BI üzerinde Geçmiş vs Gelecek verisi tek grafikte görselleştirildi.

![Sales Forecast](screenshot.png)
