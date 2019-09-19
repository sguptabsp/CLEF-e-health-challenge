
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth

# x = [500,512,600,1,1,5,6,1,5,10,22,23,23,50,51,51,52,100,112,130]
# x = [1,2,3,4,100,200,300]
import pandas as pd
df = pd.read_csv("CSV\\CD010632.csv", usecols=['pid', 'score'])
x = []
for i in df.score:
    x.append(i)
X = np.array(list(zip(x,np.zeros(len(x)))), dtype=np.int)

# X = np.array(list(zip(x,)), dtype=np.int)
# print(list(zip(x,np.zeros(len(x)))))
# print(X)
bandwidth = estimate_bandwidth(X)
print(bandwidth)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
print(labels)
labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

# c0=[]
# c1=[]
# c2=[]
# c3=[]
# n=0
# for i in ms.labels_:
#     if i==0:
#         c0.append(x[n])
#         n= n+1
#     if i==1:
#         c1.append(x[n])
#         n = n+1
#     if i==2:
#         c2.append(x[n])
#         n = n + 1
#     if i==3:
#         c3.append(x[n])
#         n = n + 1
#
# print(len(c0))
# print(len(c1))
# print(len(c2))
# print(len(c3))


# print(X[0])
# print(n_clusters_)
for k in range(n_clusters_):
    my_members = labels == k
    print ("cluster {0}: {1}".format(k, X[my_members, 0]))



# a = [1, 5, 1.5, 8, 1, 9]
# b = [2, 8, 1.8, 8, 0.6, 11]
# c = []
# c.append(a)
# c.append(b)
#
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import style
# style.use("ggplot")
# from sklearn.cluster import KMeans
# #
# c = np.array(list(zip(x,np.zeros(len(x)))), dtype=np.int)
# # plt.scatter(a,b)
# # # plt.show()
# # kmeans = KMeans(n_clusters=3)
# # kmeans.fit(c)
# #
# centroids = ms.cluster_centers_
# labels = ms.labels_

# print(centroids)
# print(labels)
#
#
# colors = ["g.","r.","c.","y."]
# plt.xlabel("Score")
# plt.title("Mean Shift")
#
# for i in range(len(c)):
#     # print("coordinate:",c[i], "label:", labels[i])
#     plt.plot(c[i][0], c[i][1], colors[labels[i]], markersize = 10)
#
# plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
# plt.savefig("Plot\\Mean_Shift.png")
# plt.show()


