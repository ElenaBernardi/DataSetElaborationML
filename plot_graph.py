import psycopg2
from matplotlib import pyplot as plt
import avg_vector

def query():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="2912",
                                      port="5433",
                                      host="localhost",
                                      database="ActivityTracker")
        # 25 anni
        cursor = connection.cursor()
        postgreSQL_select_Query = "select value from dataset where userid='6b1d408a49836443dbfc2a1bcf48b44fd0267f11' and type='4'"
        cursor.execute(postgreSQL_select_Query)
        mobile_records1 = cursor.fetchall()
        plt.plot(mobile_records1, label='31')

        #50 anni
        postgreSQL_select_Query = "select value from dataset where userid='49a05aa6295a05f65538e427f2d2d424df77815a'and type='4' "
        cursor.execute(postgreSQL_select_Query)
        mobile_records2 = cursor.fetchall()
        plt.plot(mobile_records2, label='50')

        plt.legend()
        plt.show()
        print("Print each row and it's columns values")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def query_avg():
    vector1=avg_vector.avg_behaviour(2,0,30)
    vector2=avg_vector.avg_behaviour(2,60,70)

    plt.plot(vector1, label='giovani')
    plt.plot(vector2, label='adulti')
    plt.legend()
    plt.show()