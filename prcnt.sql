SELECT customer_city, COUNT(customer_unique_id) AS customers, SUM(payment_value), SUM(payment_value) / COUNT(orders_order_id) AS avgnum
FROM customers AS C JOIN orders AS O ON C.customer_id = O.order_customer_id JOIN order_payments OP ON O.orders_order_id = OP.order_id
WHERE YEAR(order_purchase_timestamp) = "2017"
GROUP BY customer_city
ORDER BY customers desc
limit 152
