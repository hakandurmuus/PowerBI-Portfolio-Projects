import pandas as pd
import pyodbc
from sklearn.linear_model import LinearRegression
import datetime
import warnings

warnings.filterwarnings('ignore')

server = 'YOUR_SERVER_NAME'
database = 'ECommerce'

conn = pyodbc.connect(
    f'Driver={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

query = """SELECT 
    CAST(InvoiceDate AS DATE) as SatisTarihi,
    SUM(Quantity * Price) as GunlukCiro
    FROM OnlineRetail
    WHERE Quantity > 0 
    AND Price > 0 
    AND CustomerID IS NOT NULL
    GROUP BY CAST(InvoiceDate AS DATE)
    ORDER BY SatisTarihi;"""

df = pd.read_sql(query,conn)
df["SatisTarihi"] = pd.to_datetime(df["SatisTarihi"])

df["SatisOrdinal"] = df["SatisTarihi"].apply(lambda x: x.toordinal())

model = LinearRegression()

model.fit(df[["SatisOrdinal"]],df["GunlukCiro"])

son_tarih = df["SatisTarihi"].max()
gelecek_tarihler = pd.date_range(start=son_tarih + datetime.timedelta(days=1),periods=30)

tahmin_df = pd.DataFrame({"SatisTarihi": gelecek_tarihler})
tahmin_df["SatisOrdinal"] = tahmin_df["SatisTarihi"].apply(lambda x: x.toordinal())

tahmin_df["TahminiCiro"] = model.predict(tahmin_df[["SatisOrdinal"]])

conn.execute("TRUNCATE TABLE SalesForecast")
conn.commit()

for index,row in tahmin_df.iterrows():
    sql = "INSERT INTO SalesForecast (ForecastDate,PredictedRevenue) VALUES (?,?)"
    values = (row["SatisTarihi"],row["TahminiCiro"])
    conn.execute(sql,values)
    conn.commit()


