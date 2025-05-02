SELECT CONCAT(YEAR(O.order_purchase_timestamp),"-",MONTH(O.order_purchase_timestamp)) AS date, COUNT(DISTINCT C.customer_unique_id) AS customers, COUNT(order_id) / COUNT(DISTINCT C.customer_unique_id) - 1 AS same_customer_procent
FROM customers AS C JOIN orders AS O ON C.customer_id = O.customer_id
GROUP BY date
ORDER BY LEFT(date, 4), RIGHT(date, 2)
