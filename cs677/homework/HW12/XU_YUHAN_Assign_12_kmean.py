import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

df_y1 = pd.read_csv("./PINS_Y1.csv")
df_y2 = pd.read_csv("./PINS_Y2.csv")

X = df_y1[["Average", "Std"]]
y = df_y1["Label"]
X1 = df_y2[["Average", "Std"]]
y1 = df_y2["Label"]

print('Q1:')


def kmeanscluster(X, n):
    kmeans_classifier = KMeans(n_clusters=n)
    y_means = kmeans_classifier.fit_predict(X)
    centroids = kmeans_classifier.cluster_centers_
    return y_means, centroids


y_means, centroids = kmeanscluster(X, 3)
# print(y_means)
# print(centroids)

y_kmeans = []
inertia_list = []
for k in range(1, 9):
    kmeans_classifier = KMeans(n_clusters=k)
    y_kmeans = kmeans_classifier.fit_predict(X)
    inertia = kmeans_classifier.inertia_
    inertia_list.append(inertia)
fig, ax = plt.subplots(1, figsize=(7, 5))
plt.plot(range(1, 9), inertia_list, marker='o', color='green')
# plt.legend()
plt.xlabel('number of clusters : k')
plt.ylabel('inertia')
plt.tight_layout()
plt.savefig("graph.png")
print("According to the graph output, the best k = 3 by 'knee' method")

print()
print('Q2 and Q3: ')
# Computing percentage of green and red weeks in each cluster.
y_means_5, centroids_5 = kmeanscluster(X, 3)
df_y2['Cluster'] = y_means_5
df_y2.to_csv('df_y2.csv', index=False)
counts = df_y2.groupby(['Cluster', 'Label']).agg({'Std': 'count'})
counts = counts.rename({'Std': 'Counts'}, axis='columns')
print(counts)
state_pcts = counts.groupby(level=0).apply(lambda x: round(100 * x / float(x.sum()), 2))
state_pcts = state_pcts.rename({'Counts': 'Percentage%'}, axis='columns')
print(state_pcts)
