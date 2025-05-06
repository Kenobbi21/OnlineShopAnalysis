#Count of Reviews
SELECT COUNT(review_score) / (SELECT COUNT(review_score) FROM order_reviews WHERE review_score > 3 )
FROM order_reviews
WHERE review_score < 4
ORDER BY review_score DESC;

#Revies text
SELECT *
FROM order_reviews
WHERE review_score <= 3;
