import psycopg2
from matplotlib import pyplot as plt
import avg_vector
import plot2D
import numpy as np

#Query specifica relativa ad un valore di un certo tipo di un determinato utente. Fa anche il plot del risultato
def query_Single_User():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="22021996",
                                      #port="5433",
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

#scatter punti di avg_vector.avg_behaviour()
def query_avg_scatter(type1, type2, age1Min, age1Max, age2Min, age2Max):
    vector1 = plot2D.query_types_age(type1,type2,age1Min, age1Max)
    vector2 = plot2D.query_types_age(type1, type2, age2Min, age2Max)
    x1,y1 = zip(*vector1)
    x2, y2 = zip(*vector2)
    giovani = plt.scatter(x1,y1)
    anziani = plt.scatter(x2,y2)
    plt.legend((giovani,anziani), ('Giovani','Anziani'))
    plt.show()

#plot una linea di avg_vector.avg_behaviour()
def plot_avg(type,age1,age2, age3, age4):
    vector1=avg_vector.avg_behaviour(type,age1,age2)
    vector2=avg_vector.avg_behaviour(type,age3,age4)

    plt.plot(vector1, label='giovani')
    plt.plot(vector2, label='adulti')
    plt.legend()
    plt.show()

def scatter_3_types(type1,type2,type3,age1Min,age1Max,age2Min,age2Max):
    X = np.array(plot2D.query_3_types_age(type1,type2,type3,age1Min,age1Max))
    Y = np.array(plot2D.query_3_types_age(type1,type2,type3,age2Min,age2Max))
    print(X)
    fig = plt.figure()
    colors = ["g.", "r.", "c.", "b.", "k.", "c."]

    ax = plt.axes(projection='3d')
    ax.scatter3D(X[:, 0], X[:, 1], X[:, 2], cmap='viridis', linewidth=0.5);
    ax.scatter3D(Y[:, 0], Y[:, 1], Y[:, 2], cmap='viridis', linewidth=0.5);

    plt.show()