CREATE OR REPLACE VIEW bigtable AS(
SELECT customer_city, COUNT(customer_unique_id) AS customers, SUM(payment_value) AS total, SUM(payment_value) / COUNT(orders_order_id) AS avgnum
FROM customers AS C JOIN orders AS O ON C.customer_id = O.order_customer_id JOIN order_payments OP ON O.orders_order_id = OP.order_id
WHERE YEAR(order_purchase_timestamp) = "2017"
GROUP BY customer_city
ORDER BY customers desc
limit 152
);


SELECT C.customer_city, COUNT(customer_unique_id) AS customers, CONCAT(ROUND((1 - ((SELECT B.customers FROM bigtable AS B WHERE B.customer_city = C.customer_city )/COUNT(customer_unique_id))) * 100,1),"%") AS customer_growth_since_2017,
SUM(payment_value) AS total,CONCAT(ROUND((1- (SELECT total FROM bigtable AS B WHERE C.customer_city = B.customer_city)/SUM(payment_value)) * 100,1),"%") AS total_growth_since_2017, 
SUM(payment_value) / COUNT(orders_order_id) AS avgnum, CONCAT(ROUND((1 -  (SELECT avgnum FROM bigtable AS B WHERE C.customer_city = B.customer_city) / (SUM(payment_value) / COUNT(orders_order_id)))* 100,1), "%") AS avgnum_growth_since_2017
FROM customers AS C JOIN orders AS O ON C.customer_id = O.order_customer_id JOIN order_payments OP ON O.orders_order_id = OP.order_id
WHERE YEAR(order_purchase_timestamp) = "2018"
GROUP BY customer_city
ORDER BY customers desc
limit 152