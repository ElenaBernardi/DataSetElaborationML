from IPython.core.tests.tclass import C

import cluster_segments
from collections import defaultdict
from collections import Counter
import numpy as np

'''metodo che ritorna, dati in ingresso una fascia di età e due tipi di segnale, un dizionario dove per ogni pattern(chiave),
riscontrato nel segnale di tipo typeFile e di dimensione window, è associata una lista di ricorrenze registrate nel segnale 
di tipo type2'''
def compare(ageMin,ageMax,type2,typeFile,window):
    print("INIZIO CLUSTER1")
    segments1, types1 = cluster_segments.manual_clustering(ageMin, ageMax, typeFile)
    print("INIZIO CLUSTER2")
    segments2, types2 = cluster_segments.manual_clustering(ageMin, ageMax, type2)
    print(len(types2))
    print("INIZIO COMPARISON")
    return comparison(types1,types2,typeFile, window)

'''metodo di ricerca dei comportamenti ripetitivi nel segnale contenuto nella lista list2[] al verificarsi 
dei pattern, di dimensione window, nel segnale contenuto nella lista list1[]'''
def comparison(list1, list2, type, window):
    dict = read_file(type)
    keys = dict.keys()
    range_iter= min(len(list1),len(list2))
    for key in keys:
        for i in range(0,range_iter-1):
            if(i+window<range_iter-1):
                tmp = ""
                for j in range(i,i+window):
                    tmp = tmp+" "+list1[j]
                #print("tmp: "+tmp +"chiave: "+ key)
                #print(key.replace(" ","")==tmp.replace(" ",""))
                if(key.replace(" ","")==tmp.replace(" ","")):
                    tmp1 = ""
                    for j in range(i,i+window):
                        tmp1= tmp1+" "+list2[j]
                    dict[key].append(tmp1)
    return dict

def read_file(type):
    dict = defaultdict(list)
    file = open("Patterns Type " + str(type) + ".txt", "r")
    for x in file:
        tmp = x.split(sep='\t')
        dict[tmp[0]]
    return dict


def read_file_comparison(type1,type2):
    dict = defaultdict(list)
    file = open("Compare Type "+str(type1)+" con "+str(type2)+".txt", "r")
    for x in file:
        tmp = x.split(sep='\t')
        dict[tmp[0]] = tmp[1]
    return dict

'''metodo che calcola le ripetizioni dei comportamenti in percentuale, relativo al segnale di tipo type2, al 
verificarsi di un certo pattern nel segnale di tipo type1; e riporta in output un dizionario con tali informazioni'''
def percentage_comparison(type1,type2):
    dict_file = read_file_comparison(type1,type2)
    dict1= defaultdict(dict)
    for key, values in dict_file.items():

        values=values.replace("]","")
        values = values.replace("[", "")
        values = values.replace(" ", "")
        print("########")
        print(values)
        array = values.split(sep=',')
        dict1[key] = Counter(array)
        tot=0
        final_dict=defaultdict(int)
        for key1,values1 in dict1[key].items():
            tot = int(values1)+ tot
        for key1, values1 in dict1[key].items():
            values2 = (values1/tot * 100)
            final_dict[key1]=values2
        dict1[key]=final_dict
    return dict1