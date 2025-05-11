The crucial objective of the Project is analysis of customer behavior of the Olist store marketplace.
In short, i have 5 main goals for that project:

- Perform an LTV cohort analysis
- Building a sales funnel
- Predict churn using classification
- Design and run A/B test to improve conversion rates
- Build a dashboard (Streamlit)

For first i downloaded dataset from Kaggle https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce and created sql table using python (CreateTheTable.py). 

## 1. Perform an LTV cohort analysis.
After that by using MySqlWorkbench (prcnt.sql) made a cohort analysis found out that more than 1 order made only 0.019032 of all customers in average . (https://github.com/user-attachments/assets/ca790e8d-ac03-4036-80e4-ca86c6e4216b) - here you can see their activity by months, that is a bad dynamics for marketplace also i can say the same thing about all customers lifecycle activity , only 3% of all customers made more than 1 order for all dataset lifetime. Easy to say that that marketplace in a big trouble because one of the main goals of business is keeping clients. We can see better situation after conducting LTV analysis (ltv.sql):
(https://github.com/user-attachments/assets/03364cb8-e3ec-43a3-84fa-fa61239636b2) - 2017
(https://github.com/user-attachments/assets/bff53354-115a-4afe-87ed-58958e4516b2) - 2018
in this dashboards you can notice pretty good dynamics of the total customers growth it is 18% and less then 1% of avg check price growth which is not so good. But this calculations have been made based on values by city(values by city.sql), that data reflects the situation in relation to all cities, without taking into account their importance, so I also conducted a research on general data (revenue.sql, main.py), which provides a more correct picture in terms of the entire business.
We can see a growth between 2017 and 2018 in 22% in total and 2% by average order check, that means that the company is developing but need to put more effort to increase the average check just like in first research.
By using (values by city.sql) we can see the percentage difference between 2017 and 2018 for each city in detail, (https://github.com/user-attachments/assets/f40daf8e-5dfe-4441-8788-0c095a739e3a) (first 28 cities) in that photo for example we can see that the city of Sao Paulo showed a growth of 29.2% in the number of customers and 31.8% growth in the total sum of check, impressive isnt it? The second one, Rio De Janeiro showed much worse results, growth of 4.1% in the number of customers and growth of 1.5% in total sum of check. Besides the Rio there are 3 cities which showed less than 10% of customers growth, is really low accordingly to avg values and that means that this cities need more attention. 
### I can offer the Olist store the following customer acquisition solutions:
     - Targeted advertising in social media.
     - Increasing first order conversion.
     - Retention and repeat purchases (Retention): Email and SMS Marketing, loyalti program, personalized recomendations
     - Viral mechanics (Referral): bring friend and get discounts
 And etc.

### Now look at avgnum growth, about 40% of negative values in the range of cities we have identified. next sollutions can help solve this problem:
     - Offer to customers additional goods which can complement the main product
     - Upsell & Cross-sell or personalized recomendations, offer more expensive alternative 
     - Dynamic pricing and discounts, for example: "this is the last day you can buy this phone for only 500$ instead of 700$"
     - Improve UX/UI to encourage purchases, delete extra steps to buy something, for example you can add a button "buy now" instead of add to basket.
     - Loyalty and Subscription Programs
     - FOMO, put pressure on the buyer with a missed opportunity to make a good purchase.

## 2. Building a sales funnel.
- Now making a sales funnel. This database does not provide all necessary information for making full-fledged sales funnel so only way i can offer is count how much succesful orders do we have minus "unavaliable" and "canceled" orders. As a result(SalesFunnel.sql) 1.26% of unsuccesful orders and it is a great result compare to other marketplaces for comparison Amazon has 5-10% of it.
  
## 3. Predict churn using classification.
Сonsidering low customers activity detected in first stages, we will consider the churn as less than 2 orders in a year by customer (predict_churn_using_classification.sql). After the first calculations i considered that max number of orders by customer is 33, but that is solitary instance as you can see here:(https://github.com/user-attachments/assets/21c2b1e3-8c34-4edc-b0c3-2c711e43dc86). 2550 is a number of customers who made more than 2 orders for 2017, when total number is 42136 and we get 6% of customers who made at least 2 orders. Sure if i would work with marketplaces which have had better results i would make more detailed analysis, for example by months, but here it is simply not necessary. At Result we can compare Olists results with results of other marketplaces Amazon,Ozon,Wildberries and etc, for example Amazon (which statistics you can find here)(https://ir.aboutamazon.com/annual-reports-proxies-and-shareholder-letters/default.aspx) shows 10-25% of churn yearly. Therefore, to understand the reasons of that result, we can read reviews of various products, I have chosen a range of ratings from 1 to 3 which makes up 29.76% of the total ratings while the Amazon has 15-25%. To make definition of complains categories easier i`ve made some functions in "main.py" (translate_reviews, detect_category, analyze_sentiment, count_complains, complains_viz_data) After anylising the data i got of selected range of comments, i came to the conclusion that the majority of negative reviews are complaints about: long delivery times, the actual number of units received does not correspond to the ordered quantity, discrepancy between the declared quality of the goods, inappropriate packaging. (https://github.com/user-attachments/assets/d2a8267a-f271-4bd2-86bc-6fb6feabf531) - Here you can see a pie chart ("visuzlization.py", circle_drawer) with the detailed percentage of each complaint category. As a result the problem is systematic, 94% of all customers leave the Olists store. 
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
	  
 ### As a result to reduce negative customer experience, the marketplace needs to: 
    - Strictly control sellers (fines, blocking).   
    - Invest in logistics and automation (AI, scanners, chatbots).
    - Provide transparency to buyers (tracking, guarantees).

## 4. Design and run A/B test to improve conversion rates.
On this stage i decided to make a A/B test, My hypothesis: free shipping will increase conversion by 10%. For first i took "orders.sql" and disband almost 100k of customers on two groups (a,b) ("main.py", AB_test), if we want to count conversion we should count views, in that dataframe we dont have that information so i took avg values which is in area of 50 views on 1 purchase also i found out an each group orders count. After all the calculations, we actually get a 10% increase in conversion. However, it should be taken into account that the situation is modeled due to the lack of real data, but all values are selected based on average statistical values. 

## In conclusion of my research, I would like to highlight next aspects of my assessment:
### 1. Challenges and Risks
#### Low Customer Retention
     - Only 3% of customers make repeat purchases.
     - 94% of users leave after their first order (high churn rate).
     - The average order value is growing slowly (+2% per year), indicating weak monetization of the existing customer base.
#### Service Quality Issues
     - 29.76% of negative reviews (compared to 15–25% for Amazon).
     - Main complaints:
       - Long delivery times.
       - Missing items in orders.
       - Product quality discrepancies.
       - Poor packaging.
#### Regional Imbalances
     - Revenue growth is concentrated in major cities (e.g., São Paulo: +31.8%), while other cities like Rio de Janeiro show weaker performance (+1.5–4.1%).
### 2. Growth Opportunities
#### Customer Retention
     - Loyalty programs
     - Personalization
     - Service improvements
     - the majority of the economically active population of the country where the marketplace is located are not its clients.
#### Increasing Average Order Value
     - Cross-selling and upselling
     - Dynamic pricing
     - Personalization
####  Logistics Optimization
     - Localized warehouses
     - AI-powered review analysis
#### Marketing
     - Targeted advertising
     - Referral programs
### 3.  Expected Outcomes
#### If the proposed measures are implemented:
     - Repeat purchase rate: Increase from 3% to 10–15% within 1–2 years.
     - Churn rate reduction: Drop from 94% to 70–80%.
     - Higher average order value: 5–10% growth through cross-selling.
     - Fewer negative reviews: Decrease from 29.76% to 15–20%.
### 4. Priority Action Plan
     - Launch A/B tests:
       - Free shipping for orders above a certain threshold.
       - Redesigned product pages with highlighted reviews.
     - Invest in logistics:
       - Partnerships with local courier services.
     - Stricter seller oversight:
       - Penalties for delivery delays and defective products.
### Final Verdict
#### Olist has significant growth potential but requires systemic improvements in customer experience, logistics, and marketing. Key growth levers:
     - Boosting customer loyalty.
     - Enhancing service quality.
     - Expanding into underserved regions.
With proper execution, Olist could compete with major players like Mercado Libre or Amazon in Latin America. 
     
