# E-commerce Revenue and Customer Segmentation Analysis

This project focuses on using machine learning (K-means clustering) to segment customers based on their purchasing behaviors, helping businesses identify key revenue drivers and customer patterns. The analysis uses an open-source e-commerce dataset that tracks transactions and customer information.

## Project Overview

The goal of this project is to analyze customer data and identify distinct segments that can help drive business insights. By clustering customers based on their Total Revenue, Frequency of Purchases, and Average Order Value (AOV), we were able to uncover valuable patterns that can inform customer retention strategies and upselling opportunities.

## Key Metrics

- **Total Revenue**: The total amount a customer has spent.
- **Frequency**: The number of purchases made by each customer.
- **Average Order Value (AOV)**: The average value of each order.

## Findings

- **Cluster 1: Frequent Buyers**
  - Total Revenue: $100,000
  - Median Frequency: 1971 purchases
  - AOV: $55.38
  
  This small but powerful cluster contributes a large portion of revenue with frequent, high-value purchases.

- **Cluster 2: Casual Shoppers**
  - Total Revenue: $645.81
  - Median Frequency: 41.5 purchases
  - AOV: $16.90
  
  This larger cluster makes less frequent and lower-value purchases but presents potential for upselling and engagement.

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

