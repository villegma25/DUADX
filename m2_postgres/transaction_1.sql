-- ============================================
-- EJERCICIO 1: CREACIÓN DE LA BASE DE DATOS
-- ============================================

-- Tabla de usuarios
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de productos
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    stock INTEGER NOT NULL CHECK (stock >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de facturas
CREATE TABLE bills (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    total NUMERIC(10, 2) NOT NULL DEFAULT 0,
    status VARCHAR(20) NOT NULL DEFAULT 'Completada',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_bills_user
        FOREIGN KEY (user_id)
        REFERENCES users(id),

    CONSTRAINT chk_bill_status
        CHECK (status IN ('Completada', 'Retornada'))
);

-- Tabla cruz entre facturas y productos
CREATE TABLE bill_products (
    id SERIAL PRIMARY KEY,
    bill_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(10, 2) NOT NULL CHECK (unit_price >= 0),

    CONSTRAINT fk_bill_products_bill
        FOREIGN KEY (bill_id)
        REFERENCES bills(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_bill_products_product
        FOREIGN KEY (product_id)
        REFERENCES products(id)
);

-- ============================================
-- DATOS DE PRUEBA
-- ============================================

INSERT INTO users (name, email)
VALUES
    ('Juan Perez', 'juan@example.com'),
    ('Maria Lopez', 'maria@example.com');

INSERT INTO products (name, price, stock)
VALUES
    ('Laptop', 850.00, 10),
    ('Mouse', 25.00, 50),
    ('Keyboard', 45.00, 30),
    ('Monitor', 250.00, 15);