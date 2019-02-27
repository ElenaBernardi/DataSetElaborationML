import cluster_segments
from collections import defaultdict

def compare(ageMin,ageMax,type2,typeFile,window):
    print("INIZIO CLUSTER1")
    segments1, types1 = cluster_segments.manual_clustering(ageMin, ageMax, typeFile)
    print("INIZIO CLUSTER2")
    segments2, types2 = cluster_segments.manual_clustering(ageMin, ageMax, type2)
    print(len(types2))
    print("INIZIO COMPARISON")
    comparison(types1,types2,typeFile, window)


def comparison(list1, list2, type, window):
    dict = read_file(type)
    keys = dict.keys()
    range_iter= min(len(list1),len(list2))
    for key in keys:
        for i in range(0,200-1):
            if(i+window<200-1):
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
    print(dict.items())
    return dict




def read_file(type):
    dict = defaultdict(list)
    file = open("Patterns Type " + str(type) + ".txt", "r")
    for x in file:
        tmp = x.split(sep='\t')
        dict[tmp[0]]
    return dict