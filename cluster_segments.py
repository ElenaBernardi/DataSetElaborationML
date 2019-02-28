from math import fabs

import db_queries
import math_operations
import segments


'''metodo che restituisce la lista intera dei segmenti appartenenti
 agli utenti, con età compresa in un range, e la loro classe di tipo a cui appartengono, da 1 a 10 '''
def manual_clustering(ageMin,ageMax, type):
    metadatas = []
    #get data from DB
    results = db_queries.map_user_and_value_from_age_range(ageMin, ageMax, type)
    #get segments for each user
    elements = segments.segments(results)
    #concatenate all segments for all user
    for segment in elements:
        metadatas.append(math_operations.tuple_module_gradient(segment))
    #get metadatas from segments
    modules, gradients = zip(*metadatas)
    list2 = math_operations.normalize(gradients, min(gradients), max(gradients))
    zipped = zip(modules, gradients)
    array = list(zipped)
    #cluster segments by metadatas
    types=get_types_from_metadatas(metadatas)
    return elements,types

'''clustering manuale dei segmenti nei 10 possibili insiemi in base ai valori di inclinazione e modulo'''
def get_types_from_metadatas(metadatas):
    #print(metadatas)
    types=[]
    modules,gradients =zip(*metadatas)
    avg_module = sum(modules)/float(len(modules))
    for module,gradient in metadatas:
        if gradient<0:
            if 0.1<fabs(gradient)<0.5:
                if module<avg_module:
                    types.append("type_1")
                else:
                    types.append("type_2")
            if 0.5<=fabs(gradient):
                if module<avg_module:
                    types.append("type_3")
                else:
                    types.append("type_4")
            if 0<=fabs(gradient)<=0.1:
                if module<avg_module:
                    types.append("type_5")
                else:
                    types.append("type_6")
        else:
            if 0.1<fabs(gradient)<0.5:
                if module<avg_module:
                    types.append("type_7")
                else:
                    types.append("type_8")
            if 0.5<=fabs(gradient):
                if module<avg_module:
                    types.append("type_9")
                else:
                    types.append("type_10")
            if 0<=fabs(gradient)<=0.1:
                if module<avg_module:
                    types.append("type_5")
                else:
                    types.append("type_6")
    return types







