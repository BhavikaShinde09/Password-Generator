import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X, y = make_blobs(n_samples=300, centers=4, random_state=42, cluster_std=1.0)

plt.scatter(X[:, 0], X[:, 1], s=50, color='gray')
plt.title('Dataset Before Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

k = 4
kmeans = KMeans(n_clusters=k, random_state=42)
y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, marker='x')

plt.title('K-Means Clustering (k=4)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

sil_score = silhouette_score(X, y_kmeans)
print(f'Silhouette Score: {sil_score:.2f}')

print("Cluster centers:")
print(kmeans.cluster_centers_)