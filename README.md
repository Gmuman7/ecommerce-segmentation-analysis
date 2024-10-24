# ML Business Use-Case: Using K-Means for Customer Segmentation Analysis

Customer Segmentation has a ton of upsides for businesses in all industries, giving them deeper insights into their customer bases, and allowing the org to stategically focus efforts within the customer segments.  Modern advances in machine learning and computer power puts this analysis in the arsenal of every business.  In this project, I used a publicly available dataset as an example of how this analysis would be done.  This project focuses on using a machine learning algorithm (K-means clustering) to split customers into segments based on their purchasing behaviors, with the goal of helping the hypotheical business executive in this scenario build a strategy to generate more return for the business.  

## Key Metrics

While the key matrics below are elementary in nature, the goal of this project is to model the process behind the analysis.  Given this is an exercise, one can only analyze so much without additional context.

- **Total Revenue**: The total amount a customer has spent.
- **Frequency**: The number of purchases made by each customer.
- **Average Order Value (AOV)**: The average value of each order.

## Findings

Using the "Elbow Method" to identify that there were two significant clusters within the data, I was able to identify the metrics that set the customer sets apart:

- **Cluster 1: Frequent Buyers**
  - Total Revenue: $100,000
  - Median Frequency: 1971 purchases
  - AOV: $55.38
  
  This small but powerful cluster contributes a large portion of revenue with frequent, high-value purchases.  Given their very high purchase frequencies, they are likely fiercely loyal to this brand.

- **Cluster 0: Casual Shoppers**
  - Total Revenue: $645.81
  - Median Frequency: 41.5 purchases
  - AOV: $16.90
  
  This larger cluster makes less frequent and lower-value purchases but presents potential for upselling and engagement.  There were roughly 11x more customers in this segment than Cluster 1, so there are likely many opportunities to convert these customers into Cluster

## Recommendations

1) Enhance Loyalty Programs for Frequent Buyers\
Objective: Retain and reward loyalty.\
Actions: Introduce exclusive rewards, early access to new products, and personalized offers to maintain their high engagement and spending levels.

2) Upsell and Cross-Sell to Casual Shoppers\
Objective: Increase purchase frequency and order value.\
Actions: Implement targeted marketing campaigns, offer bundle deals, and provide incentives for repeat purchases to encourage higher spending.

4) Personalized Marketing Strategies
Objective: Tailor communication to each segment.
Actions: Use data-driven insights to create personalized email campaigns, social media ads, and in-app notifications that resonate with the specific needs and behaviors of each cluster.

5) Customer Feedback and Engagement
Objective: Understand and address customer needs.
Actions: Conduct surveys and feedback sessions to gather insights on customer preferences and pain points. Use this information to improve products and services.

6) Monitor and Adjust Strategies
Objective: Ensure continuous improvement.
Actions: Regularly review the performance of implemented strategies and make necessary adjustments based on customer behavior and feedback.

Conclusion
By focusing on enhancing loyalty programs for Frequent Buyers and implementing targeted upselling strategies for Casual Shoppers, the business can maximize revenue and customer satisfaction. Personalized marketing and continuous engagement will further strengthen customer relationships and drive growth.

## Dataset

The dataset used in this analysis is publicly available on [Kaggle](https://www.kaggle.com/datasets/carrie1/ecommerce-data).

## How to Run the Code

1. Clone the repository.
2. Install the required packages: `pip install -r requirements.txt`.
3. Run the `segmentation_magic.py` script to perform clustering and export the customer segments.
4. Visualize the results using `dash_by_design.py` to explore insights and generate heatmaps.

## Conclusion

This analysis shows the importance of customer segmentation in identifying high-value customers and understanding the different purchasing behaviors within a customer base. By using this information, businesses can tailor their marketing and engagement strategies to better serve their most valuable customers.

Check out the full project and code on my [GitHub](https://github.com/Gmuman7).

