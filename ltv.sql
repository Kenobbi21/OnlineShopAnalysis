CREATE OR REPLACE VIEW bigtable AS (
SELECT *
FROM customers AS C JOIN orders AS O ON C.customer_id = O.order_customer_id JOIN order_payments OP ON O.orders_order_id = OP.order_id
);
SELECT B1.customer_city, SUM(B1.payment_value) / COUNT(B1.orders_order_id), SUM(B1.payment_value),  COUNT(B1.orders_order_id) , (SELECT SUM(B.payment_value) / COUNT(B.orders_order_id)
																 FROM bigtable as B
                                                                                                                                 WHERE YEAR(B.order_purchase_timestamp) = 2018 AND B1.customer_city = B.customer_city
                                                                                                                                 )
FROM bigtable AS B1
WHERE YEAR(B1.order_purchase_timestamp) = 2017
GROUP BY B1.customer_city
