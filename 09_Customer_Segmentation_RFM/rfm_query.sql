

CREATE OR ALTER VIEW RFM_Final_Analiz AS

WITH RFM_Base as(
	SELECT 
	CustomerID,
	DATEDIFF(DAY, MAX(InvoiceDate), '2011-12-10') as Recency,
	COUNT(DISTINCT Invoice) as Frequency,
	SUM(Quantity * Price) as Monetary
	FROM OnlineRetail
	WHERE 1 = 1
	and CustomerID is not null
	and Quantity > 0
	and Price > 0
	GROUP BY CustomerID
),

t1 as (
	SELECT 
		*,
		NTILE(5) OVER (ORDER BY Recency DESC) as R_Score,
		NTILE(5) OVER (ORDER BY Frequency) as F_Score,
		NTILE(5) over (ORDER BY Monetary) as M_Score
	FROM RFM_Base
)

select 
	CustomerID,
	Recency,
	Frequency,
	Monetary,
	CONCAT(R_Score,F_Score,M_Score) as RFM_Score,
	CASE 
		WHEN R_Score = 5 and F_Score = 5 and M_Score = 5 THEN 'Þampiyonlar'
		WHEN R_Score >= 4 and F_Score >= 4 THEN 'Sadýk Müþteriler'
		WHEN R_Score <= 2 and F_Score >= 4 THEN 'Riskli'
		WHEN R_Score >= 4 and F_Score <= 2 THEN 'Yeni Müþteriler'
		WHEN R_Score <= 2 and F_Score <= 2 THEN 'Kayýp'
		ELSE 'Diðer'
		end as Segment
from t1


