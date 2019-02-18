import csv
import numpy as np
import graph
import db_queries
import clustering
import classificator

if __name__=="__main__":
    #saveDatasetInDB.saveData()
    #saveUsersInDB.saveData()

    #vector1= db_queries.pull_3types_from_range_age(5, 4, 2, 30, 40)
    #vector2 = db_queries.pull_3types_from_range_age(5, 4, 2, 60, 90)
    #vector1 = np.array(vector1)
    #vector2 = np.array(vector2)
    #vector = np.concatenate([vector1,vector2])
    #clustering.cluster3D(vector, vector1, vector2)
    #clustering.cluster2D(2,5,2)

    #graph.graph_avg_plot(5,0,30,60,90)

    #graph.graph_avg_scatter(5,2,0,30,60,90)

    #graph.scatter3D_3types_from_2ranges(5,4,1,0,30,60,90)

    classificator.training(5,2)