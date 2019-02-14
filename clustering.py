import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
import plot2D

def cluster(n, type1,type2):
    X = np.array(plot2D.query_with_age(type1))
    #X = np.array(plot2D.fromArray_toVectorTuples(type1,type2))
# plt.scatter(X[:,0],X[:,1], s=150, linewidths=5)
# plt.show()
    clf = KMeans(n_clusters=n)
    clf.fit(X)

    centroids = clf.cluster_centers_
    labels = clf.labels_

    colors = ["g.","r.","c.","b.","k.","c."]

    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 5)
    plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=150, linewidths=5)
    plt.show()

def from_triple_to_vectors(X):
    x=[]
    y=[]
    z=[]
    for i in range(len(X)):
        x.append(str(i[0]))
        y.append(str(i[1]))
        z.append(str(i[2]))
    return x,y,z

def cluster3D(n, type1, type2):
    X = np.array(plot2D.query_3_output(type1, type2))
    fig=plt.figure()
    colors = ["g.", "r.", "c.", "b.", "k.", "c."]

    ax = plt.axes(projection='3d')
    ax.scatter3D(X[:,0], X[:,1], X[:,2], cmap='viridis', linewidth=0.5);

    plt.show()
