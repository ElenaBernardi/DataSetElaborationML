import psycopg2
from collections import defaultdict
import numpy as np


def avg_user(type, value1, value2):
    map = pull_data(type, value1, value2)
    max_length = 0
    for k,v in map.items():
        length = len(v)
        if(length>max_length) :
            max_length = length
    vector_sum = np.zeros(max_length)


    for k, v in map.items():
        for i in range (0,len(vector_sum)):
            try:
                vector_sum[i]=vector_sum[i]+v[i]
            except(Exception):
                vector_sum[i]=vector_sum[i]+0

    len_map = len(map)
    for i in range(0,len(vector_sum)) :
        vector_sum[i] = vector_sum[i]/len_map

    return vector_sum


def avg_behaviour(type, value1, value2):
    map = pull_data(type, value1, value2)
    vector = []
    i=0
    for k,v in map.items():
        vector.append(np.average(v))
    return vector


def pull_data(type, value1, value2):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="22021996",
                                      #port="5433",
                                      host="localhost",
                                      database="ActivityTracker")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select dataset.value, users.userid from users join dataset on users.userid = dataset.userid where dataset.type="+str(type)+" and users.age<"+str(value2)+" and users.age>"+str(value1)
        cursor.execute(postgreSQL_select_Query)
        results = cursor.fetchall()
        print("Inizio Map")
        map = defaultdict(list)
        for k, v in results:
           map[v].append(k)
        return map
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
