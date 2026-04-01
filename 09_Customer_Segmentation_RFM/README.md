### Customer Segmentation Analysis (RFM) 🎯
A strategic marketing analysis where e-commerce customers are segmented based on purchasing behavior.

🎯 Business Problem: To better understand the customer base, identify “Lost” or “At Risk” customers, and develop targeted strategies for loyal customers using RFM (Recency, Frequency, Monetary) scoring.

🛠️ Techniques Used:

- **Data Engineering (SQL):** RFM metrics calculated from raw data and scored (1–5) using the `NTILE` window function.  
- **Segmentation Logic:** Dynamic segments such as “Champions”, “Loyal Customers”, and “At Risk” created using `CASE WHEN`.  
- **Visualization:** Treemap for segment size analysis and bar charts for revenue contribution.

![RFM Dashboard](screenshot.png)
