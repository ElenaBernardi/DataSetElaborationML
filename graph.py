from matplotlib import pyplot as plt
import db_queries
import numpy as np

#dati due type e due fasce di età stampa i punti corrispondenti alle due fasce di età
def graph_avg_scatter(type1, type2, age1Min, age1Max, age2Min, age2Max):
    vector1 = db_queries.pull_2types_from_range_age(type1, type2, age1Min, age1Max)
    vector2 = db_queries.pull_2types_from_range_age(type1, type2, age2Min, age2Max)
    x1,y1 = zip(*vector1)
    x2, y2 = zip(*vector2)
    giovani = plt.scatter(x1,y1)
    anziani = plt.scatter(x2,y2)
    plt.legend((giovani,anziani), ('Giovani','Anziani'))
    plt.show()

#dato un type e due fasce di età stampa due linee
def graph_avg_plot(type, age1, age2, age3, age4):
    vector1 = db_queries.pull_1type_from_range_age(type, age1, age2)
    vector2 = db_queries.pull_1type_from_range_age(type, age3, age4)

    plt.plot(vector1, label='giovani')
    plt.plot(vector2, label='adulti')
    plt.legend()
    plt.show()

#grafico 3D a punti, dati 3 tipi e due fasce di età
def scatter3D_3types_from_2ranges(type1, type2, type3, age1Min, age1Max, age2Min, age2Max):
    X = np.array(db_queries.pull_3types_from_range_age(type1, type2, type3, age1Min, age1Max))
    Y = np.array(db_queries.pull_3types_from_range_age(type1, type2, type3, age2Min, age2Max))
    fig = plt.figure()
    colors = ["g.", "r.", "c.", "b.", "k.", "c."]

    ax = plt.axes(projection='3d')
    ax.scatter3D(X[:, 0], X[:, 1], X[:, 2], cmap='viridis', linewidth=0.5);
    ax.scatter3D(Y[:, 0], Y[:, 1], Y[:, 2], cmap='viridis', linewidth=0.5);

    plt.show()

def scatter3D_2types_and_age(n, type1, type2):
    X = np.array(db_queries.pull_2types_and_age(type1, type2))
    fig=plt.figure()
    colors = ["g.", "r.", "c.", "b.", "k.", "c."]

    ax = plt.axes(projection='3d')
    ax.scatter3D(X[:,0], X[:,1], X[:,2], cmap='viridis', linewidth=0.5);

    plt.show()