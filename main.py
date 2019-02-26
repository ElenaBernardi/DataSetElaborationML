import csv
from collections import defaultdict

import numpy as np
import graph
import db_queries
import clustering
import classificator
import create_files_utils
import segments
import math_operations

if __name__=="__main__":

    """save dataset in db"""
    #saveDatasetInDB.saveData()
    #saveUsersInDB.saveData()

    """create file with userid and age"""
    #create_files_utils.createFileByType(5)

    """clustering 3D"""
    #vector1= db_queries.pull_3types_from_range_age(5, 4, 2, 30, 40)
    #vector2 = db_queries.pull_3types_from_range_age(5, 4, 2, 60, 90)
    #vector1 = np.array(vector1)
    #vector2 = np.array(vector2)
    #vector = np.concatenate([vector1,vector2])
    #clustering.cluster3D(vector, vector1, vector2)

    """clustering 2D"""
    #vector1= db_queries.pull_2types_from_range_age(5, 2, 30, 40)
    #vector2 = db_queries.pull_2types_from_range_age(5, 2, 60, 90)
    #vector1 = np.array(vector1)
    #vector2 = np.array(vector2)
    #vector = np.concatenate([vector1,vector2])
    #clustering.cluster2D_by_vectors(vector, vector1, vector2)

    """grafici a linea monodimensionali"""
    #graph.graph_avg_plot(5,0,30,60,90)

    """grafici a punti 2D"""
    #graph.graph_avg_scatter(5,2,0,30,60,90)

    """grafici a punti 3D"""
    #graph.scatter3D_3types_from_2ranges(5,4,1,0,30,60,90)

    """classificatore"""
    #classificator.training(5,4)
    #user = "'8ac9cda47064ec1f64f873dff99f0edd44bcf38a'"
    #classificator.predict_result(user)

    """prova"""
    #segments.segments()
    array=[]
    results=db_queries.map(30,40)
    print(len(results))
    elements = segments.segments(results)
    for segment in elements:
        array.append(math_operations.tuple_module_gradient(segment))
    #print(array)
    list1, list2 = zip(*array)
    print(max(list2))
    print(min(list2))
    #map_segments=defaultdict(list)
    #for k,values in map.items():
     #   map_segments[k].append(segments.segments(values))