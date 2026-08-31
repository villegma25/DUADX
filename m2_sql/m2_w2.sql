-- ==========================================
-- EXTRA SQL EXERCISES - SQLITE
-- ==========================================

-- ==========================================
-- CREATE CATEGORIES TABLE
-- ==========================================

CREATE TABLE Categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- ==========================================
-- ADD CATEGORY_ID TO PRODUCTS
-- ==========================================

ALTER TABLE Productos
ADD COLUMN category_id INTEGER;

-- ==========================================
-- INSERT CATEGORIES
-- ==========================================

INSERT INTO Categories (name, description)
VALUES
('Computers', 'Desktop and Laptop computers'),
('Accessories', 'Computer accessories'),
('Mobile Devices', 'Phones and tablets');

-- ==========================================
-- INSERT MORE PRODUCTS
-- ==========================================

INSERT INTO Productos (nombre, descripcion, precio, cantidad)
VALUES
('Apple MacBook Air', 'Laptop', 950000, 8),
('Apple iPhone 15', 'Smartphone', 780000, 12),
('Apple Magic Mouse', 'Wireless Mouse', 45000, 15),
('Samsung Galaxy S24', 'Smartphone', 650000, 20),
('Dell XPS 13', 'Laptop', 890000, 6),
('HP Pavilion', 'Laptop', 520000, 9),
('Logitech Keyboard', 'Mechanical Keyboard', 65000, 30),
('Acer Monitor', '27-inch Monitor', 180000, 5),
('USB-C Cable', 'Charging Cable', 8000, 100),
('Wireless Charger', 'Qi Charger', 25000, 18);

-- ==========================================
-- ASSIGN CATEGORIES
-- ==========================================

UPDATE Productos
SET category_id = 1
WHERE nombre IN ('Apple MacBook Air', 'Dell XPS 13', 'HP Pavilion');

UPDATE Productos
SET category_id = 2
WHERE nombre IN ('Apple Magic Mouse', 'Logitech Keyboard', 'USB-C Cable', 'Wireless Charger');

UPDATE Productos
SET category_id = 3
WHERE nombre IN ('Apple iPhone 15', 'Samsung Galaxy S24');

-- ==========================================
-- VERIFY PRODUCTS
-- ==========================================

SELECT
    id,
    nombre AS product_name,
    precio AS price,
    category_id,
    cantidad AS stock_available
FROM Productos;

-- ==========================================
-- SELECT ALL PRODUCTS
-- ==========================================

SELECT *
FROM Productos;

-- ==========================================
-- PRODUCTS PRICE > 50000
-- ==========================================

SELECT *
FROM Productos
WHERE precio > 50000;

-- ==========================================
-- PRODUCTS CONTAINING "APPLE"
-- ==========================================

SELECT *
FROM Productos
WHERE nombre LIKE '%Apple%';

-- ==========================================
-- TOP 5 MOST EXPENSIVE PRODUCTS
-- ==========================================

SELECT *
FROM Productos
ORDER BY precio DESC
LIMIT 5;

-- ==========================================
-- SET STOCK = 0 WHERE PRICE <= 0
-- ==========================================

UPDATE Productos
SET cantidad = 0
WHERE precio <= 0;

-- ==========================================
-- INCREASE PRICE BY 100 WHERE STOCK < 10
-- ==========================================

UPDATE Productos
SET precio = precio + 100
WHERE cantidad < 10;

-- ==========================================
-- DECREASE STOCK OF A SPECIFIC PRODUCT
-- (Example: Product ID = 1)
-- ==========================================

UPDATE Productos
SET cantidad = cantidad - 1
WHERE id = 1;

-- ==========================================
-- VERIFY FIRST 10 PRODUCTS
-- ==========================================

SELECT *
FROM Productos
ORDER BY id ASC
LIMIT 10;