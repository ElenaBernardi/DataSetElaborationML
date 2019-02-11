import os
import sys
import psycopg2

#hello!
def save_data():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="2912",
                                      port="5433",
                                      host="localhost",
                                      database="ActivityTracker")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select distinct users.age, users.userid from dataset join users on dataset.userid=users.userid where type=5"
        cursor.execute(postgreSQL_select_Query)
        print("Selecting data from users join dataset table using cursor.fetchall")
        data = cursor.fetchall()
        output = open("list_age_userid.txt", "w+")
        for i in data:

            output.write("UserId: %s\t" %str(i[0]))
            output.write(" Age: %s\r\n" %str(i[1]))


    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")