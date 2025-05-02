The crucial objective of the Project is analysis of customer behavior of the Olist store marketplace.
In short, i have 5 main goals for that project:

- Perform an LTV cohort analysis
- Building a sales funnel
- Predict churn using classification
- Run an A/B test to improve the conversion rate
- Build a dashboard (Streamlit)

For first i downloaded dataset from Kaggle https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce and created sql table using python (CreateTheTable.py). After that by using MySqlWorkbench (prcnt.sql) made a cohort analysis found out that more than 1 order made only 0.019032 of all customers in average . (https://github.com/user-attachments/assets/ca790e8d-ac03-4036-80e4-ca86c6e4216b) - here you can see their activity by months, that is a bad dynamics for marketplace also i can say the same thing about all customers lifecycle activity , only 3% of all customers made more than 1 order for all dataset lifetime. Easy to say that that marketplace in a big trouble because one of the main goals of business is keeping clients. We can see the same depressing situation after conducting LTV analysis (ltv.sql):
(https://github.com/user-attachments/assets/20c90c16-fd35-498e-bcdc-0de86f85d28f) - 2017
(https://github.com/user-attachments/assets/deb50460-82a9-4b11-b226-66b0fb32a6d9) - 2018
As you may have noticed, the difference is minimal (less than 1% of grow (total 558,623 / 562,504)). That means that the company is not developing. Actually even after the first Analysis i can say that top of thar marketplace should work on the conditions for customers
because that fact that people are not interested in making new orders after the first one, suggests that they are not satisfied with certain conditions, for example: Convenience of the marketplace website, goods quality or providing timely assistance to the buyer.
And the second problem is that the company does not attract a sufficient number of new clients to grow revenue, they should buy more advertising or make better quality of it at least.
