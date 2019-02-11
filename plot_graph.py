import psycopg2
from matplotlib import pyplot as plt


def query():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="2912",
                                      port="5433",
                                      host="localhost",
                                      database="ActivityTracker")
        # 67 anni
        cursor = connection.cursor()
        postgreSQL_select_Query = "select value from dataset where userid='2e6822c963b20adbd4c863bb65ba79642e2c0489' and type='5'"
        cursor.execute(postgreSQL_select_Query)
        mobile_records1 = cursor.fetchall()
        plt.plot(mobile_records1, label='67')
        #70 anni
        cursor = connection.cursor()
        postgreSQL_select_Query = "select value from dataset where userid='a1625a009fe1007237af2d66d50e1fb8eeba84f3' and type='5'"
        cursor.execute(postgreSQL_select_Query)
        mobile_records1 = cursor.fetchall()
        plt.plot(mobile_records1, label = '70')
        # 60 anni
        postgreSQL_select_Query = "select value from dataset where userid='f7c63d5636bacf91887fbc03574c64f57eae6c42'and type='5' "
        cursor.execute(postgreSQL_select_Query)
        mobile_records2 = cursor.fetchall()
        #plt.plot(mobile_records2, label='60')
        # 46
        postgreSQL_select_Query = "select value from dataset where userid='a2bd251237bab34576ecf46ea20d77ca2b3776c5'and type='5' "
        cursor.execute(postgreSQL_select_Query)
        mobile_records2 = cursor.fetchall()
        #plt.plot(mobile_records2, label='46')
        #31 anni
        postgreSQL_select_Query = "select value from dataset where userid='19f0793e5d7f5519ad9bb23b96dd6b4c3ed247b4'and type='5' "
        cursor.execute(postgreSQL_select_Query)
        mobile_records2 = cursor.fetchall()
        #plt.plot(mobile_records2, label='31')
        #22 anni
        postgreSQL_select_Query = "select value from dataset where userid='e4310d4eb3a7a42db5b46b7ed1667ef01ab5bbb1'and type='5' "
        cursor.execute(postgreSQL_select_Query)
        mobile_records2 = cursor.fetchall()
        plt.plot(mobile_records2, label='22')
        #12 anni
        postgreSQL_select_Query = "select value from dataset where userid='1260ea8d455196d6b28453606e95a457807de2a6'and type='5' "
        cursor.execute(postgreSQL_select_Query)
        mobile_records2 = cursor.fetchall()
        plt.plot(mobile_records2, label='59')

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