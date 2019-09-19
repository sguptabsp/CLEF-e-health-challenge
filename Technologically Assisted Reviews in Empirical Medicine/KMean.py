def bar_plot():
    import matplotlib.pyplot as barplt
    from matplotlib import style
    style.use("ggplot")
    barplt.xlabel("Rank")
    barplt.ylabel("Score")
    barplt.title("Topic : CD010632")
    barplt.scatter(range(len(df.score)), df.score)
    barplt.savefig("Plot\\K-Mean_Bar_Plot.png")

def simple_plot():
    import matplotlib.pyplot as plt
    from matplotlib import style
    style.use("ggplot")
    plt.xlabel("Rank")
    plt.ylabel("Score")
    plt.title("Topic : CD010632")
    plt.scatter(range(len(df.score)), df.score)
    plt.savefig("Plot\\K-Mean_Simple_Plot.png")

# def scatter_plot():
    # import matplotlib.pyplot as plts
    # from matplotlib import style
    # style.use("ggplot")
    # plts.xlabel("Score")
    # plts.title("K-Mean")
    #
    # colors = ["g.", "r.", "c.", "y."]
    #
    # for i in range(len(c)):
    #     # print("coordinate:",c[i], "label:", labels[i])
    #     plts.plot(c[i][0], c[i][1], colors[labels[i]], markersize=10)
    #
    # plts.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
    # plts.savefig("Plot\\K-Mean.png")

# import numpy as np
# import matplotlib.pyplot as plt
#
# np.random.seed(45)
# n = 20;
# b = n//10;
# i = np.random.randint(0,2,n)
# x = i*np.random.normal(-2.0,0.8,n) + (1-i)*np.random.normal(2.0,0.8,n)
# _ = plt.hist(x,bins=b)
#
# print(x)
# from sklearn.cluster import KMeans
# h = np.histogram(x,bins=b)
# h = np.vstack((0.5*(h[1][:-1]+h[1][1:]),h[0])).T  # because h[0] and h[1] have different sizes.
#
# kmeans = KMeans(n_clusters=2).fit(x.reshape(n,1))
# # print (kmeans.cluster_centers_)
# print(kmeans.labels_)
#
# c0=[]
# c1=[]
# for i in kmeans.labels_:
#     if i==0:
#         c0.append(x[i])
#     else:
#         c1.append(x[i])
#
# print(c0)
# print(c1)


import numpy as np
# import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# a = [1,2,3,4,100,200,300]
import pandas as pd
df = pd.read_csv("CSV\\CD010632.csv", usecols=['pid', 'score'])
a = []
for i in df.score:
    a.append(i)
# z = np.zeros(len(a))
# print(z)
# print(list(zip(a,z)))
b = np.array(list(zip(a,np.zeros(len(a)))), dtype=np.int)
# simple_plot()
#
# print(b)
#
km = KMeans(n_clusters=4)
km.fit(b)
#
# print(km.labels_)
print(km.cluster_centers_)
#
# c0=[]
# c1=[]
# c2=[]
# c3=[]
# n=0
# for i in km.labels_:
#     if i==0:
#         c0.append(a[n])
#         n= n+1
#     if i==1:
#         c1.append(a[n])
#         n = n+1
#     if i==2:
#         c2.append(a[n])
#         n = n + 1
#     if i==3:
#         c3.append(a[n])
#         n = n + 1
#
# print(len(c0))
# print(len(c1))
# print(len(c2))
# print(len(c3))


# a = [1, 5, 1.5, 8, 1, 9]
# b = [2, 8, 1.8, 8, 0.6, 11]
# c = []
# c.append(a)
# c.append(b)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

c = np.array(list(zip(a,np.zeros(len(a)))), dtype=np.int)

# # plt.show()
# kmeans = KMeans(n_clusters=4)
# kmeans.fit(c)
#
# centroids = kmeans.cluster_centers_
# labels = kmeans.labels_

# print(centroids)
# print(labels)
# scatter_plot()
# plt.xlabel("Score")
# plt.title("K-Mean")

# colors = ["g.","r.","c.","y."]
#
# for i in range(len(c)):
#     # print("coordinate:",c[i], "label:", labels[i])
#     plt.plot(c[i][0], c[i][1], colors[labels[i]], markersize = 10)
#
#
# plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
# plt.savefig("Plot\\K-Mean.png")
# plt.show()


