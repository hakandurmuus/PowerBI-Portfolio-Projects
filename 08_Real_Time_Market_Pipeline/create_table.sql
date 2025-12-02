CREATE TABLE CanliBorsa (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Symbol NVARCHAR(10),      
    Price DECIMAL(10, 4),     
    EventTime DATETIME       
);