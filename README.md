The crucial objective of the Project is analysis of customer behavior of the Olist store marketplace.
In short, i have 5 main goals for that project:

- Perform an LTV cohort analysis
- Building a sales funnel
- Predict churn using classification
- Run an A/B test to improve the conversion rate
- Build a dashboard (Streamlit)

For first i downloaded dataset from Kaggle https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce and created sql table using python (CreateTheTable.py). 

## 1. Perform an LTV cohort analysis.
After that by using MySqlWorkbench (prcnt.sql) made a cohort analysis found out that more than 1 order made only 0.019032 of all customers in average . (https://github.com/user-attachments/assets/ca790e8d-ac03-4036-80e4-ca86c6e4216b) - here you can see their activity by months, that is a bad dynamics for marketplace also i can say the same thing about all customers lifecycle activity , only 3% of all customers made more than 1 order for all dataset lifetime. Easy to say that that marketplace in a big trouble because one of the main goals of business is keeping clients. We can see better situation after conducting LTV analysis (ltv.sql):
(https://github.com/user-attachments/assets/03364cb8-e3ec-43a3-84fa-fa61239636b2) - 2017
(https://github.com/user-attachments/assets/bff53354-115a-4afe-87ed-58958e4516b2) - 2018
in this dashboards you can notice pretty good dynamics of the total customers growth it is 18% and less then 1% of avg check price growth which is not so good. But this calculations have been made based on values by city(values by city.sql), that data reflects the situation in relation to all cities, without taking into account their importance, so I also conducted a research on general data (revenue.sql, main.py), which provides a more correct picture in terms of the entire business.
We can see a growth between 2017 and 2018 in 22% in total and 2% by average order check, that means that the company is developing but need to put more effort to increase the average check just like in first research.
By using (values by city.sql) we can see the percentage difference between 2017 and 2018 for each city in detail, (https://github.com/user-attachments/assets/f40daf8e-5dfe-4441-8788-0c095a739e3a) (first 28 cities) in that photo for example we can see that the city of Sao Paulo showed a growth of 29.2% in the number of customers and 31.8% growth in the total sum of check, impressive isnt it? The second one, Rio De Janeiro showed much worse results, growth of 4.1% in the number of customers and growth of 1.5% in total sum of check. Besides the Rio there are 3 cities which showed less than 10% of customers growth is really low accordingly to avg values and that means that this cities need more attention. 
 I can offer to Olist store next sollutions:
 #### 1. Targeted advertising in social media.
 #### 2. Increasing first order conversion.
 #### 3. Retention and repeat purchases (Retention): Email and SMS Marketing, loyalti program, personalized recomendations
 #### 4. Viral mechanics (Referral): bring friend and get discounts
 And etc.

Now look at avgnum growth, about 40% of negative values in the range of cities we have identified. next sollutions can help solve this problem:
 
 #### 1. Offer to customers additional goods which can complement the main product
 #### 2. Upsell & Cross-sell or personalized recomendations, offer more expensive alternative 
 #### 3. Dynamic pricing and discounts, for example: "this is the last day you can buy this phone for only 500$ instead of 700$"
 #### 4. Improve UX/UI to encourage purchases, delete extra steps to buy something, for example you can add a button "buy now" instead of add to basket.
 #### 5. Loyalty and Subscription Programs
 #### 6. FOMO, put pressure on the buyer with a missed opportunity to make a good purchase.

## 2. Building a sales funnel.
- Now making a sales funnel. This database does not provide all necessary information for making full-fledged sales funnel so only way i can offer is count how much succesful orders do we have minus "unavaliable" and "canceled" orders. As a result(SalesFunnel.sql) 1.26% of unsuccesful orders and it is a great result compare to other marketplaces for comparison Amazon has 5-10% of it. 

## 3. Predict churn using classification.
Сonsidering low customers activity detected in first stages, we will consider the churn as less than 2 orders in a year by customer (predict_churn_using_classification.sql). After the first calculations i considered that max number of orders by customer is 33, but that is solitary instance as you can see here:(https://github.com/user-attachments/assets/21c2b1e3-8c34-4edc-b0c3-2c711e43dc86). 2550 is a number of customers who made more than 2 orders for 2017, when total number is 42136 and we get 6% of customers who made at least 2 orders. Sure if i would work with marketplaces which have had better results i would make more detailed analysis, for example by months, but here it is simply not necessary. At Result we can compare Olists results with results of other marketplaces Amazon,Ozon,Wildberries and etc, for example Amazon (which statistics you can find here)(https://ir.aboutamazon.com/annual-reports-proxies-and-shareholder-letters/default.aspx) shows 10-25% of churn yearly. Therefore, to understand the reasons of that result, we can read reviews of various products, I have chosen a range of ratings from 1 to 3 which makes up 29.76% of the total ratings while the Amazon has 15-25%. To make definition of complains categories easier i`ve made some functions in "main.py" (translate_reviews, detect_category, analyze_sentiment, count_complains, complains_viz_data) After anylising the data i got of selected range of comments, i came to the conclusion that the majority of negative reviews are complaints about: long delivery times, the actual number of units received does not correspond to the ordered quantity, discrepancy between the declared quality of the goods, inappropriate packaging. (![blbablabla]https://github.com/user-attachments/assets/d2a8267a-f271-4bd2-86bc-6fb6feabf531) -Here you can see a pie chart (visuzlization.py, circle_drawer) with the detailed percentage of each complaint category. As a result the problem is systematic, 94% of all customers leave the Olists store. 

The following tips should improve the situation: 
 ### 1.long delivery times.
      - Implement demand forecasting algorithms to place goods in the nearest warehouses.
	  - Introduce express delivery (1-2 days) for premium customers.
	  - Use your own delivery services to control deadlines.
 ### 2.Shortage (quantity discrepancy)
      - Control at the order assembly stage: Implement a double-check system (barcode scanner, parcel weighing, Use computer vision in warehouses for automatic verification.
	  - If a shortage is detected - immediate refund for the missing goods. Bonus points as an apology.
	  - Strict sanctions for sellers: blocking of goods in case of repeated cases, demand for prepayment from unreliable suppliers.
 ### 3.Discrepancy with the declared quality.
      - Verification of sellers: photo and video recording of goods before shipment, mandatory certification for "risk" categories (electronics, cosmetics).
	  - Money Back Guarantee: free returns within 14-30 days, customer photo report to speed up the claim.
	  - Ratings and reviews, ai analysis of reviews to detect fraudsters, sellers with low ratings are subject to sanctions.
 ### 4.Inappropriate packaging
      - Packaging standardization, mandatory requirements for materials (bubble wrap, boxes), partnership with packaging companies for discounts for sellers.
	  - Control at marketplace warehouses: random checks of parcels before shipping, fines for violating standards.
	  
And as a result to reduce negative customer experience, the marketplace needs to: 

    - Strictly control sellers (fines, blocking).   
    - Invest in logistics and automation (AI, scanners, chatbots).
    - Provide transparency to buyers (tracking, guarantees).
