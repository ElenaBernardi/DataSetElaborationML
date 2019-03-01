import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D

style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.cm as cm
import db_queries


#clustering 2D, dato il numero di cluster da trovare e 2 tipi di dati
def cluster2D(n, type1,type2):
    X = np.array(db_queries.pull_2types_values(type1, type2))
    clf = KMeans(n_clusters=n)
    clf.fit(X)

    centroids = clf.cluster_centers_
    labels = clf.labels_

    colors = ["g.","r.","c.","b.","k.","c."]

    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 5)
    plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=150, linewidths=5)
    plt.show()

#clustering 2D date due vettori diversi
def cluster2D_by_vectors(dataset, range1, range2, n_clusters):
    plt.rcParams['figure.figsize'] = (16, 9)
    dataset = np.array(dataset)
    # Creating a sample dataset with n clusters
    X = dataset
    Y = range1
    Z= range2
    # Initializing KMeans
    kmeans = KMeans(n_clusters)
    # Fitting with inputs
    kmeans = kmeans.fit(X)
    # Predicting the clusters
    labels = kmeans.predict(X)
    # Getting the cluster centers
    C = kmeans.cluster_centers_
    fig = plt.figure()
    plt.scatter(Y[:, 0], Y[:, 1])
    plt.scatter(Z[:, 0], Z[:, 1])
    plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505', s=1000)
    plt.show()

    silhouette=metrics.silhouette_score(X, labels)
    silhouette_sample=metrics.silhouette_samples(X,labels)
    print("silhouette score: "+str(silhouette))
    print("silhouette samples: "+str(silhouette_sample))




#clustering 3D, dato un dataset
def cluster3D(dataset, range1, range2, n_clusters):
    plt.rcParams['figure.figsize'] = (16, 9)
    dataset = np.array(dataset)
    # Creating a sample dataset with n clusters
    X = dataset
    Y = range1
    Z= range2
    # Initializing KMeans
    kmeans = KMeans(n_clusters)
    # Fitting with inputs
    kmeans = kmeans.fit(X)
    # Predicting the clusters
    labels = kmeans.predict(X)
    # Getting the cluster centers
    C = kmeans.cluster_centers_
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(Y[:, 0], Y[:, 1], Y[:, 2])
    ax.scatter(Z[:, 0], Z[:, 1], Z[:, 2])
    ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c='#050505', s=1000)
    plt.show()

    silhouette = metrics.silhouette_score(X, labels)
    silhouette_sample = metrics.silhouette_samples(X, labels)
    print("silhouette score: " + str(silhouette))
    print("silhouette samples: " + str(silhouette_sample))


