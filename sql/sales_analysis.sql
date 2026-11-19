-- 1. Calculate total sales revenue
SELECT 
SUM(total_amount) AS total_revenue
FROM sales;

-- 2. Find revenue by each product
SELECT
product,
SUM(total_amount) AS product_revenue
FROM sales
GROUP BY product
ORDER BY product_revenue DESC;

--3. Calculate revenue by product category
SELECT
category,
SUM(total_amount) AS category_revenue
FROM sales
GROUP BY category
ORDER BY category_revenue DESC;

-- 4. Calculate total revenue for each day
SELECT
order_date,
SUM(total_amount) AS daily_revenue
FROM sales
GROUP BY order_date
ORDER BY order_date;

-- 5. Calculate total spending
SELECT
customer_name,
SUM(total_amount) AS customer_spending
FROM sales
GROUP BY customer_name
ORDER BY customer_spending
DESC;