CREATE OR REPLACE VIEW hugetable AS(
SELECT *
FROM customers AS C JOIN orders AS O ON C.customer_id = O.order_customer_id JOIN order_payments OP ON O.orders_order_id = OP.order_id
WHERE YEAR(order_purchase_timestamp) = "2017" AND order_status = "delivered"
);

CREATE OR REPLACE VIEW order_counter AS (
SELECT customer_unique_id , COUNT(customer_unique_id) AS counter
FROM hugetable
Group by customer_unique_id
);

#MAX order quantitity by one customer and more than 1 order number of customers 
SELECT MAX(counter) , COUNT(customer_unique_id)
FROM order_counter
WHERE counter > 1;

#% of customers who made 2 or more orders
SELECT COUNT(customer_unique_id) / (SELECT DISTINCT COUNT(customer_unique_id) FROM order_counter) AS "%of customers who made 2 or more orders"
FROM order_counter
WHERE counter > 1
