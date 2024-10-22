# segmentation_magic.py
# This script will segment customers based on purchasing behaviors
# We're using K-means clustering to find patterns in the data
# The goal is to group customers into different segments based on their purchase amounts, frequency, etc.

import pandas as pd
import sklearn
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def preprocess_for_clustering(data):
    """
    This function prepares the dataset for clustering.
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
    (TotalRevenue, Frequency, AOV) are on the same scale.
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(customer_summary[['TotalRevenue', 'Frequency', 'AOV']])
    
    print("Data has been standardized.")
    return scaled_data

def perform_kmeans_clustering(scaled_data, n_clusters=4):
    """
    This function applies K-means clustering on the preprocessed customer data.
    The number of clusters can be adjusted based on the elbow method or business requirements.
    
    We'll return both the K-means object and the cluster labels assigned to each customer.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(scaled_data)
    
    # The cluster label for each customer
    customer_clusters = kmeans.labels_
    
    print(f"K-means clustering completed with {n_clusters} clusters.")
    return kmeans, customer_clusters

def plot_elbow_method(scaled_data, max_clusters=10):
    """
    Use the elbow method to determine the optimal number of clusters.
    We'll run K-means for a range of cluster numbers and plot the inertia (within-cluster sum of squares).
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
    
    # Perform K-means clustering with an initial guess of 4 clusters
    kmeans, customer_clusters = perform_kmeans_clustering(scaled_data, n_clusters=2)

    
    # Add the cluster labels to the customer summary for further analysis
    customer_summary['Cluster'] = customer_clusters
    print(customer_summary.head())  # Display the first few rows of the customer summary with clusters

    # Save the customer summary with cluster labels for future use
    customer_summary.to_csv('reports/customer_segments.csv', index=False)
    print("Customer segmentation saved to 'reports/customer_segments.csv'.")
