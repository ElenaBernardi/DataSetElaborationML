from collections import defaultdict

import numpy as np
import psycopg2

import connection_db


#dati due tipi restituisce un vettore di coppie di uno stesso utente (val1,val2)
def pull_2types_values(type_1, type_2):
    try:
        connection = connection_db.connect()
        cursor = connection.cursor()
        postgreSQL_select_Query = "select value1, value2 from ( select userid, avg(value) as value1 from dataset where type="+str(type_1)+\
                                  "group by userid) as query1 join (select userid, avg(value) as value2 from dataset where type="+str(type_2)+\
                                   "group by userid) as query2 on query1.userid = query2.userid "

        cursor.execute(postgreSQL_select_Query)
        results = cursor.fetchall()
        return results
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#dato un tipo e un'età restituisce un vettore di coppie (val,età)
def pull_type_and_age(type):
    try:
        connection = connection_db.connect()
        cursor = connection.cursor()

        postgreSQL_select_Query = "select query1.value1, users.age from(" + \
                                  "select value1, query2.userid from(" + \
                                  "select userid, avg(value) as value1 from dataset where type= " + str(type) + \
                                  " group by userid)as query2) as query1 join users on users.userid=query1.userid"
        cursor.execute(postgreSQL_select_Query)
        results = cursor.fetchall()
        return results
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#restituisce un vettore con una tripla di uno stesso utente (val1,val2,age) per 2 tipi di valori diversi
def pull_2types_and_age(type_1, type_2):
    try:
        connection = connection_db.connect()
        cursor = connection.cursor()
        postgreSQL_select_Query = "select query3.value1, query3.value2, users.age from(select value1, value2, query1.userid from ( select userid, avg(value) as value1 from dataset where type=" + str(
            type_1) + \
                                  "group by userid) as query1 join (select userid, avg(value) as value2 from dataset where type=" + str(
            type_2) + \
                                  "group by userid) as query2 on query1.userid = query2.userid) as query3 join users on query3.userid = users.userid "

        cursor.execute(postgreSQL_select_Query)
        results = cursor.fetchall()
        return results

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#dato un type e una fascia di età restituisce un vettore di valori medi per ogni utente
def pull_1type_from_range_age(type, age_min, age_max):
    connection = connection_db.connect()
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = "select query.media from(select avg(dataset.value) as media, dataset.userid from users join dataset on users.userid = dataset.userid where dataset.type=" + str(type) +" and users.age<" + str(age_max) + " and users.age>" + str(age_min) + "group by dataset.userid) as query"

        cursor.execute(postgreSQL_select_Query)
        results = cursor.fetchall()
        return results
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#dati due types e una fascia di età restituisce un vettore bidimensionale con i valori medi dei types per uno stesso utente
def pull_2types_from_range_age(type_1, type_2, age_min, age_max):
    connection = connection_db.connect()
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = "select query3.value1, query3.value2 " +\
                                  "from(" +\
                                  " select value1, value2, query1.userid " + \
                                  " from ( " +\
                                  "   select userid, avg(value) as value1 " +\
                                  "   from dataset " +\
                                  "   where type=" + str(type_1) + \
                                  "   group by userid) as query1 join (" +\
                                  "   select userid, avg(value) as value2 " +\
                                  "   from dataset " +\
                                  "   where type=" + str(type_2) +\
                                  "   group by userid) as query2 " +\
                                  " on query1.userid = query2.userid) as query3 join users on query3.userid = users.userid " +\
                                  "where users.age<"+str(age_max)+" and users.age>"+str(age_min)

        cursor.execute(postgreSQL_select_Query)
        results = cursor.fetchall()
        return results
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#dati 3 types e una fascia di età restituisce un vettore di triple con i valori medi di uno stesso utente
def pull_3types_from_range_age(type_1, type_2, type_3, age_min, age_max):
    connection = connection_db.connect()
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = "select query3.value1, query3.value2, query3.value3 from(select value1, value2, query2.value3, query1.userid from(select userid, avg(value) as value1 from dataset where type="+str(type_1)+ \
                                  "group by userid) as query1 join (select dataset.userid, avg(value) as value2, value3 from dataset join(select userid, avg(value) as value3 from dataset where type="+str(type_2)+ \
                                  "group by userid) as query4 on query4.userid=dataset.userid where type="+str(type_3)+ \
                                  "group by dataset.userid, value3) as query2 on query1.userid = query2.userid) as query3 join users on query3.userid = users.userid where users.age<"+str(age_max)+" and users.age>"+str(age_min)

        cursor.execute(postgreSQL_select_Query)
        results = cursor.fetchall()
        return results
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

"""metodo che risporta i valori medi dei type in ingresso dato uno user"""
def pull_avg_value_from_user(user, type_1, type_2):
    connection = connection_db.connect()
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = "select query3.value1, query3.value2 from(select value1, value2, query1.userid from ( select userid, avg(value) as value1 from dataset where type=" + str(type_1) +\
                                  "group by userid) as query1 join (select userid, avg(value) as value2 from dataset where type=" + str(type_2) +\
                                  "group by userid) as query2 on query1.userid = query2.userid) as query3  where query3.userid=" + str(user)

        cursor.execute(postgreSQL_select_Query)
        results = cursor.fetchall()
        return results
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def prova():
    connection = connection_db.connect()
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = "select value from dataset where userid='102b72d02aebae82c5c1ee3d4dcbc4d82de7c7ee' and type=5"

        cursor.execute(postgreSQL_select_Query)
        results = cursor.fetchall()
        results = np.squeeze(np.asarray(results))
        return results
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def map_user_and_value_from_age_range(age_min, age_max, type):
    connection = connection_db.connect()
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = "select dataset.value from dataset join users on dataset.userid=users.userid where dataset.type=" + str(type) +" and users.age<" + str(age_max) + " and users.age>" + str(age_min)

        cursor.execute(postgreSQL_select_Query)
        results = cursor.fetchall()
        results = np.squeeze(np.asarray(results))
        results=results.tolist()
        return results
        #map=defaultdict(list)
        #for k,value in results:
         #   map[k].append(value)

        #return map
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")