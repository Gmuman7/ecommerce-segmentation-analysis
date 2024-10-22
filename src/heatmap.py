def plot_cluster_heatmap(data):
    """
    Create a heatmap to compare the metrics for each cluster.
    This allows a quick visual comparison of revenue, frequency, and AOV across segments.
    """
    cluster_metrics = data.groupby('Cluster').agg({
        'TotalRevenue': 'mean',
        'Frequency': 'mean',
        'AOV': 'mean'
    })
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cluster_metrics, annot=True, cmap='coolwarm')
    plt.title('Heatmap of Average Metrics by Cluster')
    plt.show()
