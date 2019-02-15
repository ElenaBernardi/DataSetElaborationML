import csv
import numpy as np
import graph
import db_queries
import clustering

if __name__=="__main__":
    #main()
    #saveDatasetInDB.saveData()
    #saveUsersInDB.saveData()
    #plot_graph.query_avg()
    #age_userid_type5.save_data()
    #age_userid_type4.save_data()
    #avg_vector.avg_behaviour(5,0,30)
    #plot2D.fromArray_toVectorTuples(5,6)
    #clustering.cluster3D(3,5,11)
    #clustering.cluster(3,1,4)
    #plot_graph.query_avg_scatter(5,4,0,30,60,90)
    #plot_graph.scatter_3_types(5,4,1,0,30,60,90)
    #dataset = plot_graph.scatter_3_types(5,4,1,0,30,0,90)
    vector1= db_queries.pull_3types_from_range_age(7, 5, 3, 0, 30)
    vector2 = db_queries.pull_3types_from_range_age(7, 5, 3, 60, 90)
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    vector = np.concatenate([vector1,vector2])
    clustering.cluster3D(vector, vector1, vector2)
