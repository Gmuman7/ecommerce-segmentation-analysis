# dash_by_design.py
# This script visualizes customer segments and provides insights based on K-means clustering results.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_segmented_data(file_path):
    """
    Load the customer segmentation data from the CSV file.
    This data includes customer metrics (TotalRevenue, Frequency, AOV) and the cluster labels.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Segmented data loaded successfully with {data.shape[0]} customers.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def plot_cluster_scatter(data):
    """
    Create scatter plots to visualize customer segments based on their key metrics:
    - TotalRevenue vs Frequency
    - AOV vs Frequency
    
    Different clusters will be shown in different colors for easy comparison.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='TotalRevenue', y='Frequency', hue='Cluster', data=data, palette='Set1', s=100, alpha=0.8)
    plt.title('Customer Segments: Total Revenue vs Frequency')
    plt.xlabel('Total Revenue')
    plt.ylabel('Purchase Frequency')
    plt.legend(title='Cluster')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='AOV', y='Frequency', hue='Cluster', data=data, palette='Set2', s=100, alpha=0.8)
    plt.title('Customer Segments: AOV vs Frequency')
    plt.xlabel('Average Order Value (AOV)')
    plt.ylabel('Purchase Frequency')
    plt.legend(title='Cluster')
    plt.grid(True)
    plt.show()

def plot_cluster_distribution(data):
    """
    Plot the distribution of customers across different clusters.
    This will give us an idea of how many customers belong to each segment.
    """
    cluster_counts = data['Cluster'].value_counts().sort_index()

    plt.figure(figsize=(8, 5))
    sns.barplot(x=cluster_counts.index, y=cluster_counts.values, palette='Set3')
    plt.title('Distribution of Customers Across Clusters')
    plt.xlabel('Cluster')
    plt.ylabel('Number of Customers')
    plt.show()

    print(f"Cluster distribution:\n{cluster_counts}")

def summarize_clusters(data):
    """
    Provide a summary of key metrics (TotalRevenue, Frequency, AOV) for each cluster.
    This gives insights into the typical customer profile for each segment.
    """
    cluster_summary = data.groupby('Cluster').agg({
        'TotalRevenue': ['mean', 'sum'],
        'Frequency': 'mean',
        'AOV': 'mean'
    }).reset_index()
    
    cluster_summary.columns = ['Cluster', 'AvgRevenue', 'TotalRevenue', 'AvgFrequency', 'AvgAOV']
    
    print("Cluster Summary:")
    print(cluster_summary)

    # Plot the summary to give a quick overview of each segment
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Cluster', y='AvgRevenue', data=cluster_summary, palette='Set1')
    plt.title('Average Revenue by Cluster')
    plt.ylabel('Average Revenue')
    plt.xlabel('Cluster')
    plt.show()

    return cluster_summary

if __name__ == "__main__":
    # Load the segmented customer data
    file_path = 'reports/customer_segments.csv'
    data = load_segmented_data(file_path)
    
    if data is not None:
        # Plot scatter plots to visualize the clusters
        plot_cluster_scatter(data)

        # Plot the distribution of customers across clusters
        plot_cluster_distribution(data)

        # Summarize the clusters for insights
        cluster_summary = summarize_clusters(data)
        print(cluster_summary)
