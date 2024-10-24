# segmentation_magic.py
# This script will segment customers based on purchasing behaviors
# We're using K-means clustering to find patterns in the data
# The goal is to group customers into different segments based on their purchase amounts, frequency, etc.

import pandas as pd
import sklearn
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def preprocess_for_clustering(data):
    """
    This function cleans the dataset for clustering.
    It focuses on summarizing customer purchase behavior for segmentation purposes.
    
    We'll calculate:
    - Total Revenue per Customer
    - Frequency of Purchases
    - Average Order Value (AOV)
    
    These metrics will allow us to better cluster customers based on their purchasing patterns.
    """
    # Create a summary DataFrame to store customer metrics
    customer_summary = data.groupby('CustomerID').agg({
        'TotalPrice': 'sum',     # Total Revenue (sum of all orders)
        'InvoiceNo': 'count',    # Frequency (number of purchases)
    }).reset_index()
    
    # Rename columns for clarity
    customer_summary.rename(columns={
        'TotalPrice': 'TotalRevenue',
        'InvoiceNo': 'Frequency'
    }, inplace=True)

    # Calculate Average Order Value (AOV) for each customer
    customer_summary['AOV'] = customer_summary['TotalRevenue'] / customer_summary['Frequency']

    print(f"Preprocessed data for clustering: {customer_summary.shape[0]} customers.")
    return customer_summary

def standardize_data(customer_summary):
    """
    Standardize the data to have a mean of 0 and a standard deviation of 1.
    K-means is sensitive to feature scaling, so this step ensures that all our features
    (TotalRevenue, Frequency, AOV) are on the same scale. The higher values in the Total 
    Revenue would overwhelm the results and would be badly skewed.
    
    This is important! 
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(customer_summary[['TotalRevenue', 'Frequency', 'AOV']])
    
    print("Data has been standardized.")
    return scaled_data

def perform_kmeans_clustering(scaled_data, n_clusters=2):
    """
    Applies K-means clustering on the preprocessed customer data.
    The number of clusters can be adjusted based on the elbow method or business requirements.
    
    Lets call both the K-means object and the cluster labels assigned to each customer.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(scaled_data)
    
    # The cluster label for each customer
    customer_clusters = kmeans.labels_
    
    print(f"K-means clustering completed with {n_clusters} clusters.")
    return kmeans, customer_clusters

def plot_elbow_method(scaled_data, max_clusters=10):
    """
    Use the 'elbow method' to determine the optimal number of clusters.
    We'll run K-means for a range of cluster numbers and plot the "inertia" (within-cluster sum of squares).
    "Inertia" is a complex concept, and one needs to be familiar with it in this section.
    """
    inertia = []
    cluster_range = range(1, max_clusters+1)
    
    for n in cluster_range:
        kmeans = KMeans(n_clusters=n, random_state=42)
        kmeans.fit(scaled_data)
        inertia.append(kmeans.inertia_)  # Inertia: Sum of squared distances to cluster centers

    # Plot the elbow curve
    plt.figure(figsize=(8, 5))
    plt.plot(cluster_range, inertia, marker='o', linestyle='--')
    plt.title('Elbow Method for Optimal Cluster Selection')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.show()

    print("Elbow plot displayed. Look for the 'elbow' to determine the optimal cluster count.")

def plot_cluster_heatmap(data):
    """
    Create a rudimentary heatmap to compare the metrics for each cluster.
    We'll format the revenue and AOV as currency and handle different scales for each metric.
    (Like we normalized the data above in the K-Means algorithm)
    """
    # Step 1: Calculate the metrics for each cluster
    cluster_metrics = data.groupby('Cluster').agg({
        'TotalRevenue': 'mean',
        'Frequency': 'mean',
        'AOV': 'mean'
    })

    # Step 2: Format TotalRevenue and AOV as currency, round Frequency to 1 decimal place
    formatted_metrics = cluster_metrics.copy()
    formatted_metrics['TotalRevenue'] = cluster_metrics['TotalRevenue'].apply(lambda x: f"${x:,.2f}")
    formatted_metrics['AOV'] = cluster_metrics['AOV'].apply(lambda x: f"${x:,.2f}")
    formatted_metrics['Frequency'] = cluster_metrics['Frequency'].apply(lambda x: f"{x:.1f}")
    
    # Step 3: Normalize each column for better color scale representation
    normalized_metrics = cluster_metrics.copy()
    for column in ['TotalRevenue', 'Frequency', 'AOV']:
        normalized_metrics[column] = (cluster_metrics[column] - cluster_metrics[column].min()) / \
                                     (cluster_metrics[column].max() - cluster_metrics[column].min())

    # Step 4: Plot the heatmap using normalized data but show original formatted values as annotations
    plt.figure(figsize=(8, 6))
    sns.heatmap(normalized_metrics, annot=formatted_metrics, fmt="", cmap='coolwarm', cbar=False)
    plt.title('Heatmap of Mean Metrics by Cluster')
    plt.show()



if __name__ == "__main__":
    # Load the cleaned dataset
    data_path = 'data/dataset.csv'
    data = pd.read_csv(data_path)
    
    # Preprocess the data for clustering
    customer_summary = preprocess_for_clustering(data)
    
    # Standardize the data
    scaled_data = standardize_data(customer_summary)
    
    # Plot the elbow method to find the optimal number of clusters
    plot_elbow_method(scaled_data)
    
    # Perform K-means clustering with an initial guess of 2 clusters
    kmeans, customer_clusters = perform_kmeans_clustering(scaled_data, n_clusters=2)
    
    # Add the cluster labels to the customer summary for further analysis
    customer_summary['Cluster'] = customer_clusters
    print(customer_summary.head())  # Display the first few rows of the customer summary with clusters

    # Save the customer summary with cluster labels for future use
    customer_summary.to_csv('reports/customer_segments.csv', index=False)
    print("Customer segmentation saved to 'reports/customer_segments.csv'.")
    
    # Now plot the heatmap
    plot_cluster_heatmap(customer_summary)