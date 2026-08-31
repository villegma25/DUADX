-- =========================================================
-- EJERCICIOS DE JOINs
-- =========================================================

-- =========================================================
-- 1. CREAR TABLAS
-- =========================================================

CREATE TABLE Authors (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);

CREATE TABLE Books (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Author INTEGER,
    FOREIGN KEY (Author) REFERENCES Authors(ID)
);

CREATE TABLE Customers (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL
);

CREATE TABLE Rents (
    ID INTEGER PRIMARY KEY,
    BookID INTEGER NOT NULL,
    CustomerID INTEGER NOT NULL,
    State TEXT NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books(ID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(ID)
);


-- =========================================================
-- 2. INSERTAR AUTORES
-- =========================================================

INSERT INTO Authors (ID, Name)
VALUES
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');


-- =========================================================
-- 3. INSERTAR LIBROS
-- =========================================================

INSERT INTO Books (ID, Name, Author)
VALUES
(1, 'Don Quijote', 1),
(2, 'La Divina Comedia', 2),
(3, 'Vagabond 1-3', 3),
(4, 'Dragon Ball 1', 4),
(5, 'The Book of the 5 Rings', NULL);


-- =========================================================
-- 4. INSERTAR CLIENTES
-- =========================================================

INSERT INTO Customers (ID, Name, Email)
VALUES
(1, 'John Doe', 'j.doe@email.com'),
(2, 'Jane Doe', 'jane@doe.com'),
(3, 'Luke Skywalker', 'darth.son@email.com');


-- =========================================================
-- 5. INSERTAR RENTAS
-- =========================================================

INSERT INTO Rents (ID, BookID, CustomerID, State)
VALUES
(1, 1, 2, 'Returned'),
(2, 2, 2, 'Returned'),
(3, 1, 1, 'On time'),
(4, 3, 1, 'On time'),
(5, 2, 2, 'Overdue');


-- =========================================================
-- QUERY 1
-- Obtener todos los libros y sus autores, en caso de tenerlos
-- =========================================================

SELECT
    Books.ID AS BookID,
    Books.Name AS BookName,
    Authors.Name AS AuthorName
FROM Books
LEFT JOIN Authors
    ON Books.Author = Authors.ID;


-- =========================================================
-- QUERY 2
-- Obtener todos los libros que no tienen autor
-- =========================================================

SELECT
    Books.ID AS BookID,
    Books.Name AS BookName
FROM Books
LEFT JOIN Authors
    ON Books.Author = Authors.ID
WHERE Authors.ID IS NULL;


-- =========================================================
-- QUERY 3
-- Obtener todos los autores que no tienen libros
-- =========================================================

SELECT
    Authors.ID AS AuthorID,
    Authors.Name AS AuthorName
FROM Authors
LEFT JOIN Books
    ON Authors.ID = Books.Author
WHERE Books.ID IS NULL;


-- =========================================================
-- QUERY 4
-- Obtener todos los libros que han sido rentados en algún momento
-- =========================================================

SELECT DISTINCT
    Books.ID AS BookID,
    Books.Name AS BookName
FROM Books
INNER JOIN Rents
    ON Books.ID = Rents.BookID;


-- =========================================================
-- QUERY 5
-- Obtener todos los libros que nunca han sido rentados
-- =========================================================

SELECT
    Books.ID AS BookID,
    Books.Name AS BookName
FROM Books
LEFT JOIN Rents
    ON Books.ID = Rents.BookID
WHERE Rents.ID IS NULL;


-- =========================================================
-- QUERY 6
-- Obtener todos los clientes que nunca han rentado un libro
-- =========================================================

SELECT
    Customers.ID AS CustomerID,
    Customers.Name AS CustomerName,
    Customers.Email
FROM Customers
LEFT JOIN Rents
    ON Customers.ID = Rents.CustomerID
WHERE Rents.ID IS NULL;


-- =========================================================
-- QUERY 7
-- Obtener todos los libros rentados que están "Overdue"
-- =========================================================

SELECT DISTINCT
    Books.ID AS BookID,
    Books.Name AS BookName,
    Rents.State
FROM Books
INNER JOIN Rents
    ON Books.ID = Rents.BookID
WHERE Rents.State = 'Overdue';