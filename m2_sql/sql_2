-- ==========================================
-- SQL EXERCISES - SQLite
-- ==========================================

-- ==========================================
-- CREATE TABLES
-- ==========================================

CREATE TABLE Productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL CHECK(precio >= 0),
    cantidad INTEGER NOT NULL CHECK(cantidad >= 0)
);

CREATE TABLE Compradores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    correo TEXT UNIQUE
);

CREATE TABLE Facturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_factura TEXT NOT NULL UNIQUE,
    comprador_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    monto_total REAL NOT NULL,

    FOREIGN KEY (comprador_id)
        REFERENCES Compradores(id)
);

CREATE TABLE DetalleFactura (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    factura_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL CHECK(cantidad > 0),
    precio_unitario REAL NOT NULL CHECK(precio_unitario >= 0),

    FOREIGN KEY (factura_id)
        REFERENCES Facturas(id),

    FOREIGN KEY (producto_id)
        REFERENCES Productos(id)
);

-- ==========================================
-- ALTER TABLE
-- ==========================================

ALTER TABLE Facturas
ADD COLUMN telefono_comprador TEXT;

ALTER TABLE Facturas
ADD COLUMN codigo_empleado TEXT;

-- ==========================================
-- SAMPLE DATA
-- ==========================================

INSERT INTO Productos (nombre, descripcion, precio, cantidad)
VALUES
('Laptop', 'Gaming Laptop', 850000, 10),
('Mouse', 'Wireless Mouse', 15000, 50),
('Keyboard', 'Mechanical Keyboard', 60000, 25),
('Monitor', '27 inch Monitor', 180000, 15);

INSERT INTO Compradores (nombre, apellido, correo)
VALUES
('Juan', 'Perez', 'juan@email.com'),
('Maria', 'Lopez', 'maria@email.com');

INSERT INTO Facturas (
    numero_factura,
    comprador_id,
    fecha,
    monto_total,
    telefono_comprador,
    codigo_empleado
)
VALUES
('F001', 1, '2026-04-20', 910000, '8888-1111', 'EMP001'),
('F002', 2, '2026-04-21', 180000, '8888-2222', 'EMP002');

INSERT INTO DetalleFactura (
    factura_id,
    producto_id,
    cantidad,
    precio_unitario
)
VALUES
(1, 1, 1, 850000),
(1, 3, 1, 60000),
(2, 4, 1, 180000);

-- ==========================================
-- SELECT 1
-- Obtain all stored products
-- ==========================================

SELECT *
FROM Productos;

-- ==========================================
-- SELECT 2
-- Products with price greater than 50000
-- ==========================================

SELECT *
FROM Productos
WHERE precio > 50000;

-- ==========================================
-- SELECT 3
-- All purchases of the same product by ID
-- Example: Product ID = 1
-- ==========================================

SELECT *
FROM DetalleFactura
WHERE producto_id = 1;

-- ==========================================
-- SELECT 4
-- Purchases grouped by product showing
-- total quantity purchased
-- ==========================================

SELECT
    p.id,
    p.nombre,
    SUM(df.cantidad) AS total_comprado
FROM Productos p
JOIN DetalleFactura df
ON p.id = df.producto_id
GROUP BY p.id, p.nombre;

-- ==========================================
-- SELECT 5
-- All invoices from the same buyer
-- Example: Buyer ID = 1
-- ==========================================

SELECT *
FROM Facturas
WHERE comprador_id = 1;

-- ==========================================
-- SELECT 6
-- Invoices ordered by total amount descending
-- ==========================================

SELECT *
FROM Facturas
ORDER BY monto_total DESC;

-- ==========================================
-- SELECT 7
-- One invoice by invoice number
-- Example: F001
-- ==========================================

SELECT *
FROM Facturas
WHERE numero_factura = 'F001';

-- ==========================================
-- SQLite Notes
-- ==========================================
-- 1. INTEGER PRIMARY KEY AUTOINCREMENT is used
--    to generate IDs automatically.
--
-- 2. SQLite does not have a native DATE type,
--    so dates are stored as TEXT (YYYY-MM-DD).
--
-- 3. SQLite uses dynamic typing (type affinity),
--    so TEXT and REAL are appropriate here.