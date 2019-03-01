from matplotlib import pyplot as plt
import db_queries
import numpy as np

#dati due type e due fasce di età stampa i punti corrispondenti alle due fasce di età
def graph_avg_scatter(type_1, type_2, age1_min, age1_max, age2_min, age2_max):
    vector1 = db_queries.pull_2types_from_range_age(type_1, type_2, age1_min, age1_max)
    vector2 = db_queries.pull_2types_from_range_age(type_1, type_2, age2_min, age2_max)
    x1,y1 = zip(*vector1)
    x2, y2 = zip(*vector2)
    giovani = plt.scatter(x1,y1)
    anziani = plt.scatter(x2,y2)
    plt.legend((giovani,anziani), ('Giovani','Anziani'))
    plt.show()

#dato un type e due fasce di età stampa due linee
def graph_avg_plot(type, age1_min, age1_max, age2_min, age2_max):
    vector1 = db_queries.pull_1type_from_range_age(type, age1_min, age1_max)
    vector2 = db_queries.pull_1type_from_range_age(type, age2_min, age2_max)

    print(vector1)

    plt.plot(vector1, label='giovani')
    plt.plot(vector2, label='adulti')
    plt.legend()
    plt.show()

#grafico 3D a punti, dati 3 tipi e due fasce di età
def scatter3D_3types_from_2ranges(type_1, type_2, type_3, age1_min, age1_max, age2_min, age2_max):
    X = np.array(db_queries.pull_3types_from_range_age(type_1, type_2, type_3, age1_min, age1_max))
    Y = np.array(db_queries.pull_3types_from_range_age(type_1, type_2, type_3, age2_min, age2_max))
    fig = plt.figure()
    colors = ["g.", "r.", "c.", "b.", "k.", "c."]

    ax = plt.axes(projection='3d')
    ax.scatter3D(X[:, 0], X[:, 1], X[:, 2], cmap='viridis', linewidth=0.5);
    ax.scatter3D(Y[:, 0], Y[:, 1], Y[:, 2], cmap='viridis', linewidth=0.5);

    plt.show()

def scatter3D_2types_and_age(n, type_1, type_2):
    X = np.array(db_queries.pull_2types_and_age(type_1, type_2))
    fig=plt.figure()
    colors = ["g.", "r.", "c.", "b.", "k.", "c."]

    ax = plt.axes(projection='3d')
    ax.scatter3D(X[:,0], X[:,1], X[:,2], cmap='viridis', linewidth=0.5);

    plt.show()