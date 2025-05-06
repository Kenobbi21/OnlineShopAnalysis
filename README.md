The crucial objective of the Project is analysis of customer behavior of the Olist store marketplace.
In short, i have 5 main goals for that project:

- Perform an LTV cohort analysis
- Building a sales funnel
- Predict churn using classification
- Run an A/B test to improve the conversion rate
- Build a dashboard (Streamlit)

For first i downloaded dataset from Kaggle https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce and created sql table using python (CreateTheTable.py). 

#1 After that by using MySqlWorkbench (prcnt.sql) made a cohort analysis found out that more than 1 order made only 0.019032 of all customers in average . (https://github.com/user-attachments/assets/ca790e8d-ac03-4036-80e4-ca86c6e4216b) - here you can see their activity by months, that is a bad dynamics for marketplace also i can say the same thing about all customers lifecycle activity , only 3% of all customers made more than 1 order for all dataset lifetime. Easy to say that that marketplace in a big trouble because one of the main goals of business is keeping clients. We can see better situation after conducting LTV analysis (ltv.sql):
(https://github.com/user-attachments/assets/03364cb8-e3ec-43a3-84fa-fa61239636b2) - 2017
(https://github.com/user-attachments/assets/bff53354-115a-4afe-87ed-58958e4516b2) - 2018
in this dashboards you can notice pretty good dynamics of the total customers growth it is 18% and less then 1% of avg check price growth which is not so good. But this calculations have been made based on values by city(values by city.sql), that data reflects the situation in relation to all cities, without taking into account their importance, so I also conducted a research on general data (revenue.sql, main.py), which provides a more correct picture in terms of the entire business.
We can see a growth between 2017 and 2018 in 22% in total and 2% by average order check, that means that the company is developing but need to put more effort to increase the average check just like in first research.
By using (values by city.sql) we can see the percentage difference between 2017 and 2018 for each city in detail, (https://github.com/user-attachments/assets/f40daf8e-5dfe-4441-8788-0c095a739e3a) (first 28 cities) in that photo for example we can see that the city of Sao Paulo showed a growth of 29.2% in the number of customers and 31.8% growth in the total sum of check, impressive isnt it? The second one, Rio De Janeiro showed much worse results, growth of 4.1% in the number of customers and growth of 1.5% in total sum of check. Besides the Rio there are 3 cities which showed less than 10% of customers growth is really low accordingly to avg values and that means that this cities need more attention. 
 I can offer to Olist store next sollutions:
 1. Targeted advertising in social media.
 2. Increasing first order conversion.
 3. Retention and repeat purchases (Retention): Email and SMS Marketing, loyalti program, personalized recomendations
 4. Viral mechanics (Referral): bring friend and get discounts
 And etc.

 Now look at avgnum growth, about 40% of negative values in the range of cities we have identified. next sollutions can help solve this problem:
 
 1. Offer to customers additional goods which can complement the main product
 2. Upsell & Cross-sell or personalized recomendations, offer more expensive alternative 
 3. Dynamic pricing and discounts, for example: "this is the last day you can buy this phone for only 500$ instead of 700$"
 4. Improve UX/UI to encourage purchases, delete extra steps to buy something, for example you can add a button "buy now" instead of add to basket.
 5. Loyalty and Subscription Programs
 6. FOMO, put pressure on the buyer with a missed opportunity to make a good purchase.

- Now making a sales funnel. This database does not provide all necessary information for making full-fledged sales funnel so only way i can offer is count how much succesful orders do we have minus "unavaliable" and "canceled" orders. As a result(SalesFunnel.sql) 1.26% of unsuccesful orders and it is a great result compare to other marketplaces for comparison Amazon has 5-10% of it. 
