
CREATE DATABASE Production;
GO

use Production;
GO

CREATE TABLE ProductPrice (
	ID INT IDENTITY(1,1) PRIMARY KEY,
	ProductName NVARCHAR(200),
	SiteName NVARCHAR(100),
	Price DECIMAL(10,4),
	EventTime DATETIME
);

