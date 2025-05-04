SELECT CONCAT(ROUND(((SELECT COUNT(order_status) FROM online_shop.orders) / COUNT(order_status) - 1) * 100,2), "%") AS procent_of_unsuccesful
FROM online_shop.orders
WHERE order_status != "unavailable" AND order_status != "canceled";
