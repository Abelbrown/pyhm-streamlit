# H&M Group Product Recommendation Competition

This repository contains the code and resources developed by our team for the H&M Group Product Recommendation Competition on Kaggle. In this competition, we were tasked with developing product recommendations based on customer transaction data, as well as customer and product metadata provided by H&M Group.

## Problem Description

H&M Group is a leading retail company with a vast online marketplace and numerous physical stores. The challenge they face is to enhance the shopping experience for their customers by providing personalized product recommendations. By helping customers find the right products quickly, H&M Group aims to increase customer satisfaction and reduce returns, thereby promoting sustainability.

Our goal was to leverage the available data, including transaction history, customer attributes, and product information, to develop accurate and effective product recommendation models. The evaluation metric for this competition is Mean Average Precision @ 12 (MAP@12), which measures the precision of our predictions at cutoff 12.

## Data Description

The provided data includes:

- Transaction data: Information about customer purchases, including customer ID, article ID, and timestamp.
- Customer metadata: Attributes of customers, such as age, gender, and location.
- Product metadata: Various details about the products, including garment type, product description, and images.

It was up to us to explore and utilize the available data to extract meaningful features and develop recommendation models.

## Approaches Used

We employed a combination of different algorithms and techniques to tackle the product recommendation problem. The following approaches were implemented and experimented with:

- Alternating Least Squares (ALS): Collaborative filtering algorithm for generating personalized recommendations based on user-item interactions.
- Graph Neural Network (GNN): Utilizing graph-based models to capture complex relationships between customers and products.
- Recurrent Neural Network (RNN): Sequential models to capture temporal patterns in customer behavior for making personalized recommendations.
- Gradient Boosting: Ensemble learning technique combining multiple weak models to create powerful recommendation models.

We thoroughly evaluated and fine-tuned each approach to optimize the MAP@12 metric and improve the accuracy of our predictions.

## Conclusion

Our team invested considerable effort in developing effective product recommendation models for H&M Group's competition. We explored various algorithms, including ALS, GNN, RNN, and Gradient Boosting, to leverage the provided data and generate accurate predictions.

We hope that our work serves as a valuable contribution to the field of product recommendation and provides insights for improving the shopping experience

## Authors

- Julien Da Silva
- Abel Mebkhout
- Jean Trebuchet