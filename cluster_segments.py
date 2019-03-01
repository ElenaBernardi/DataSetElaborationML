from math import fabs

import db_queries
import math_operations
import segments


'''metodo che restituisce la lista intera dei segmenti appartenenti
 agli utenti, con età compresa in un range, e la loro classe di tipo a cui appartengono, da 1 a 10 '''
def manual_clustering(age_min, age_max, type):
    metadatas = []
    #get data from DB
    results = db_queries.map_user_and_value_from_age_range(age_min, age_max, type)
    #get segments for each user
    elements = segments.segments(results)
    #concatenate all segments for all user
    for segment in elements:
        metadatas.append(math_operations.tuple_module_gradient(segment))
    #get metadatas from segments
    modules, gradients = zip(*metadatas)
    list2 = math_operations.normalize(gradients, min(gradients), max(gradients))
    zipped = zip(modules, list2)
    array = list(zipped)
    #cluster segments by metadatas
    types=get_types_from_features(array)
    return elements,types

'''clustering manuale dei segmenti nei 10 possibili insiemi in base ai valori di inclinazione e modulo'''
def get_types_from_features(list_of_segment_features):
    types=[]
    modules,gradients = zip(*list_of_segment_features)
    avg_module = sum(modules)/float(len(modules))
    for module,gradient in list_of_segment_features:
        if gradient<0:
            if 0.1<fabs(gradient)<0.5:
                if module<avg_module:
                    types.append("0")
                else:
                    types.append("1")
            if 0.5<=fabs(gradient):
                if module<avg_module:
                    types.append("2")
                else:
                    types.append("3")
            if 0<=fabs(gradient)<=0.1:
                if module<avg_module:
                    types.append("4")
                else:
                    types.append("5")
        else:
            if 0.1<fabs(gradient)<0.5:
                if module<avg_module:
                    types.append("6")
                else:
                    types.append("7")
            if 0.5<=fabs(gradient):
                if module<avg_module:
                    types.append("8")
                else:
                    types.append("9")
            if 0<=fabs(gradient)<=0.1:
                if module<avg_module:
                    types.append("4")
                else:
                    types.append("5")
    return types







