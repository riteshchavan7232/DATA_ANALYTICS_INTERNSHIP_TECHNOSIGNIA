-- DAY 9: SQL JOINS AND AGGREGATIONS


-- =====================================
-- PART 1: INNER JOIN AND LEFT JOIN
-- =====================================

-- 1. INNER JOIN: DISPLAY CUSTOMER DETAILS WITH SALES

SELECT
    c.customer_name,
    s.sale_id,
    s.quantity,
    s.sale_date
FROM customers c
INNER JOIN sales s
ON c.customer_id = s.customer_id;


-- 2. LEFT JOIN: DISPLAY ALL CUSTOMERS WITH THEIR SALES

SELECT
    c.customer_name,
    s.sale_id,
    s.quantity
FROM customers c
LEFT JOIN sales s
ON c.customer_id = s.customer_id;


-- 3. JOIN THREE TABLES TO DISPLAY SALES DETAILS

SELECT
    c.customer_name,
    p.product_name,
    s.quantity,
    p.price,
    s.quantity * p.price AS total_amount
FROM sales s
INNER JOIN customers c
ON s.customer_id = c.customer_id
INNER JOIN products p
ON s.product_id = p.product_id;


-- =====================================
-- PART 2: GROUP BY AND AGGREGATE FUNCTIONS
-- =====================================

-- 4. CALCULATE TOTAL SALES BY PRODUCT

SELECT
    p.product_name,
    SUM(s.quantity * p.price) AS total_sales
FROM sales s
INNER JOIN products p
ON s.product_id = p.product_id
GROUP BY p.product_name;


-- 5. CALCULATE TOTAL SALES BY CUSTOMER

SELECT
    c.customer_name,
    SUM(s.quantity * p.price) AS total_sales
FROM sales s
INNER JOIN customers c
ON s.customer_id = c.customer_id
INNER JOIN products p
ON s.product_id = p.product_id
GROUP BY c.customer_name;


-- 6. COUNT TOTAL SALES RECORDS FOR EACH PRODUCT

SELECT
    p.product_name,
    COUNT(s.sale_id) AS total_orders
FROM products p
LEFT JOIN sales s
ON p.product_id = s.product_id
GROUP BY p.product_name;


-- 7. CALCULATE SUM, AVG, MIN AND MAX OF PRODUCT PRICES

SELECT
    SUM(price) AS total_price,
    AVG(price) AS average_price,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price
FROM products;


-- 8. USE HAVING TO FIND PRODUCTS WITH TOTAL SALES
-- GREATER THAN 10000

SELECT
    p.product_name,
    SUM(s.quantity * p.price) AS total_sales
FROM sales s
INNER JOIN products p
ON s.product_id = p.product_id
GROUP BY p.product_name
HAVING SUM(s.quantity * p.price) > 10000;


-- =====================================
-- PART 3: CASE WHEN
-- =====================================

-- 9. CLASSIFY PRODUCTS BASED ON THEIR PRICE

SELECT
    product_name,
    price,
    CASE
        WHEN price >= 30000 THEN 'Expensive'
        WHEN price >= 10000 THEN 'Medium'
        ELSE 'Affordable'
    END AS price_category
FROM products;


-- 10. CLASSIFY SALES BASED ON TOTAL AMOUNT

SELECT
    s.sale_id,
    p.product_name,
    s.quantity * p.price AS total_amount,
    CASE
        WHEN s.quantity * p.price >= 30000 THEN 'High Sales'
        WHEN s.quantity * p.price >= 10000 THEN 'Medium Sales'
        ELSE 'Low Sales'
    END AS sales_category
FROM sales s
INNER JOIN products p
ON s.product_id = p.product_id;


-- =====================================
-- PART 4: SUBQUERIES
-- =====================================

-- 11. FIND PRODUCTS WHOSE PRICE IS GREATER
-- THAN THE AVERAGE PRODUCT PRICE

SELECT *
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);


-- 12. FIND CUSTOMERS WHO HAVE MADE AT LEAST ONE SALE

SELECT *
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM sales
);


-- =====================================
-- PART 5: COMMON TABLE EXPRESSIONS (CTE)
-- =====================================

-- 13. CALCULATE TOTAL SALES USING CTE

WITH product_sales AS (
    SELECT
        p.product_name,
        SUM(s.quantity * p.price) AS total_sales
    FROM sales s
    INNER JOIN products p
    ON s.product_id = p.product_id
    GROUP BY p.product_name
)
SELECT *
FROM product_sales;


-- 14. FIND CUSTOMERS WHOSE TOTAL SALES
-- ARE GREATER THAN 20000

WITH customer_sales AS (
    SELECT
        c.customer_name,
        SUM(s.quantity * p.price) AS total_sales
    FROM sales s
    INNER JOIN customers c
    ON s.customer_id = c.customer_id
    INNER JOIN products p
    ON s.product_id = p.product_id
    GROUP BY c.customer_name
)
SELECT *
FROM customer_sales
WHERE total_sales > 20000;


-- =====================================
-- PART 6: MONTHLY SALES ANALYSIS
-- =====================================

-- 15. CALCULATE TOTAL SALES BY MONTH

SELECT
    TO_CHAR(s.sale_date, 'YYYY-MM') AS sales_month,
    SUM(s.quantity * p.price) AS monthly_sales
FROM sales s
INNER JOIN products p
ON s.product_id = p.product_id
GROUP BY TO_CHAR(s.sale_date, 'YYYY-MM')
ORDER BY sales_month;