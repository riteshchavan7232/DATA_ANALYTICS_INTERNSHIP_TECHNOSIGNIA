-- DAY 8: SQL FUNDAMENTALS

-- =====================================
-- PART 1: CREATE TABLES
-- =====================================

-- 1. CREATE CUSTOMERS TABLE

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);


-- 2. CREATE PRODUCTS TABLE

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10,2)
);


-- 3. CREATE SALES TABLE

CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    sale_date DATE
);


-- =====================================
-- PART 2: INSERT RECORDS
-- =====================================

-- 4. INSERT CUSTOMERS

INSERT INTO customers (customer_name, email, city)
VALUES
('Rahul Sharma', 'rahul@gmail.com', 'Pune'),
('Priya Patil', 'priya@gmail.com', 'Mumbai'),
('Amit Kumar', NULL, 'Pune'),
('Sneha Joshi', 'sneha@gmail.com', 'Nashik'),
('Rohan Desai', 'rohan@gmail.com', 'Mumbai'),
('Neha Singh', NULL, 'Nagpur');


-- 5. INSERT PRODUCTS

INSERT INTO products (product_name, category, price)
VALUES
('Laptop', 'Electronics', 55000),
('Mobile', 'Electronics', 20000),
('Keyboard', 'Accessories', 1500),
('Mouse', 'Accessories', 800),
('Monitor', 'Electronics', 12000),
('Headphones', 'Accessories', 2500);


-- 6. INSERT SALES

INSERT INTO sales (customer_id, product_id, quantity, sale_date)
VALUES
(1, 1, 1, '2026-01-10'),
(2, 2, 2, '2026-01-12'),
(3, 3, 3, '2026-01-15'),
(4, 4, 2, '2026-02-01'),
(5, 5, 1, '2026-02-05'),
(1, 6, 2, '2026-02-10'),
(2, 1, 1, '2026-02-15'),
(6, 2, 1, '2026-02-20');


-- =====================================
-- PART 3: CHECK INSERTED RECORDS
-- =====================================

SELECT * FROM customers;

SELECT * FROM products;

SELECT * FROM sales;


-- =====================================
-- PART 4: SQL FUNDAMENTAL QUERIES
-- =====================================

-- 1. DISPLAY ALL CUSTOMER RECORDS

SELECT *
FROM customers;


-- 2. DISPLAY CUSTOMER NAME AND CITY

SELECT customer_name, city
FROM customers;


-- 3. FIND CUSTOMERS FROM PUNE

SELECT *
FROM customers
WHERE city = 'Pune';


-- 4. DISPLAY PRODUCTS IN ASCENDING ORDER OF PRICE

SELECT *
FROM products
ORDER BY price ASC;


-- 5. DISPLAY UNIQUE CUSTOMER CITIES

SELECT DISTINCT city
FROM customers;


-- 6. USE ALIAS TO CHANGE COLUMN NAME

SELECT
    customer_name AS Name,
    city AS Location
FROM customers;


-- 7. FIND PRODUCTS WITH PRICE GREATER THAN 10000

SELECT *
FROM products
WHERE price > 10000;


-- 8. FIND CUSTOMERS WHOSE EMAIL IS NULL

SELECT *
FROM customers
WHERE email IS NULL;


-- 9. FIND CUSTOMERS WHOSE NAME STARTS WITH R

SELECT *
FROM customers
WHERE customer_name LIKE 'R%';


-- 10. FIND PRODUCTS WITH PRICE BETWEEN 1000 AND 20000

SELECT *
FROM products
WHERE price BETWEEN 1000 AND 20000;


-- 11. FIND CUSTOMERS FROM PUNE OR MUMBAI

SELECT *
FROM customers
WHERE city = 'Pune' OR city = 'Mumbai';


-- 12. FIND PRODUCTS FROM ELECTRONICS CATEGORY

SELECT *
FROM products
WHERE category = 'Electronics';


-- 13. DISPLAY SALES WITH QUANTITY GREATER THAN 1

SELECT *
FROM sales
WHERE quantity > 1;


-- 14. DISPLAY SALES IN DESCENDING ORDER OF DATE

SELECT *
FROM sales
ORDER BY sale_date DESC;


-- 15. DISPLAY CUSTOMERS WHO HAVE AN EMAIL

SELECT *
FROM customers
WHERE email IS NOT NULL;