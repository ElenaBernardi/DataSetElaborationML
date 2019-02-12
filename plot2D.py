import psycopg2

import avg_vector


def fromArray_toVectorTuples(type1, type2):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="22021996",
                                      #port="5433",
                                      host="localhost",
                                      database="ActivityTracker")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select value1, value2 from ( select userid, avg(value) as value1 from dataset where type="+str(type1)+\
                                  "group by userid) as query1 join (select userid, avg(value) as value2 from dataset where type="+str(type2)+\
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

def query_with_age(type):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="22021996",
                                      # port="5433",
                                      host="localhost",
                                      database="ActivityTracker")
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

def query_3_output(type1, type2):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="22021996",
                                      # port="5433",
                                      host="localhost",
                                      database="ActivityTracker")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select query3.value1, query3.value2, users.age from(select value1, value2, query1.userid from ( select userid, avg(value) as value1 from dataset where type=" + str(
            type1) + \
                                  "group by userid) as query1 join (select userid, avg(value) as value2 from dataset where type=" + str(
            type2) + \
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
