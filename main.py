import csv
from collections import defaultdict

import numpy as np

import comparison_between_types
import find_pattern
import cluster_segments
import graph
import db_queries
import clustering
import classificator
import create_files_utils
import segments
import math_operations
import comparison_between_types
import math

if __name__=="__main__":

    """save dataset in db"""
    #saveDatasetInDB.saveData()
    #saveUsersInDB.saveData()

    """create file with userid and age"""
    #create_files_utils.createFileByType(type=5)

    """clustering 3D"""
    #vector1= db_queries.pull_3types_from_range_age(type_1 = 1, type_2 = 4, type_3 = 5, age_min = 30, age_max = 40)
    #vector2 = db_queries.pull_3types_from_range_age(type_1 = 1, type_2 = 4, type_3 = 5, age_min = 60, age_max = 90)
    #vector1 = np.array(vector1)
    #vector2 = np.array(vector2)
    #vector = np.concatenate([vector1,vector2])
    #clustering.cluster3D(dataset = vector, range1 = vector1, range2 = vector2, n_clusters = 2)

    """clustering 2D"""
    vector1= db_queries.pull_2types_from_range_age(type_1 = 5, type_2 = 4, age_min = 30, age_max = 40)
    vector2 = db_queries.pull_2types_from_range_age(type_1 = 5, type_2 = 4, age_min = 60, age_max = 90)
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    vector = np.concatenate([vector1,vector2])
    clustering.cluster2D_by_vectors(dataset = vector, range1 = vector1, range2 = vector2, n_clusters = 2)

    """grafici a linea monodimensionali"""
    #graph.graph_avg_plot(type = 5, age1_min = 0, age1_max = 30, age2_min = 60, age2_max = 90)

    """grafici a punti 2D"""
    #graph.graph_avg_scatter(type_1 = 5,type_2 = 2,age1_min = 0,age1_max = 30,age2_min = 60,age2_max = 90)

    """grafici a punti 3D"""
    #graph.scatter3D_3types_from_2ranges(type_1 = 5,type_2 = 4,type_3 = 1,age1_min = 0,age1_max = 30,age2_min = 60,age2_max = 90)

    """classificatore"""
    #classificator.training(5,4)
    #user = "'8ac9cda47064ec1f64f873dff99f0edd44bcf38a'"
    #classificator.predict_result(user)

    '''clustering dei segmenti, relativi ai segnali di tipo 5, in base al loro modulo e alla loro inclinazione'''
    #segments1,types=cluster_segments.manual_clustering(10,90,5)
    #segments2, types2 = cluster_segments.manual_clustering(10, 90, 4)

    #print(types)

    '''rilevazione dei pattern di sequenza di n segmenti'''

    #B= types.copy()
    #d=find_pattern.get_patters(types,B,5)
    #create_files_utils.save_patterns(d,5,200)

    '''rilevazione di comportamenti ripetitivi in altri segnali al verificarsi dei pattern'''
    #dict=comparison_between_types.compare(10,90,4,5,5,6)
    #print(dict)
    #create_files_utils.save_comparison(dict,4,5)

    '''rilevazione di comportamenti ripetitivi, relativi ad altri segnali, al verificarsi dei pattern con la relativa percentuale di successo'''
    #dict=comparison_between_types.percentage_comparison(4,5)
    #create_files_utils.save_percentage(dict)
    # print(math.sqrt(2 * 102912 + 1/4) - 1/2)