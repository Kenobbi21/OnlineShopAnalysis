SELECT YEAR(order_purchase_timestamp) AS date, SUM(payment_value), SUM(payment_value) / COUNT(orders_order_id) AS avgnum
FROM customers AS C JOIN orders AS O ON C.customer_id = O.order_customer_id JOIN order_payments OP ON O.orders_order_id = OP.order_id
WHERE order_status = "delivered"
GROUP BY date
ORDER BY date
