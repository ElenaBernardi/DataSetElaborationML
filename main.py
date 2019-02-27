import csv
from collections import defaultdict

import numpy as np
import find_pattern
import cluster_segments
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

    '''clustering dei segmenti, relativi ai segnali di tipo 5, in base al loro modulo e alla loro inclinazione'''
    segments,types=cluster_segments.manual_clustering(10,90)
    #print(types)

    '''rilevazione dei pattern di sequenza di n segmenti'''
    patterns=find_pattern.sliding_window(types,5,10)
    print(patterns)

    # map_segments=defaultdict(list)
    # for k,values in map.items():
    #   map_segments[k].append(segments.segments(values))