

SELECT 
    CAST(InvoiceDate AS DATE) as SatisTarihi,
    SUM(Quantity * Price) as GunlukCiro
FROM OnlineRetail
WHERE Quantity > 0 
  AND Price > 0 
  AND CustomerID IS NOT NULL
GROUP BY CAST(InvoiceDate AS DATE)
ORDER BY SatisTarihi;


CREATE TABLE SalesForecast(
	ForecastDate DATE,
	PredictedRevenue DECIMAL(18,2)
);


