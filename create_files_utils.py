import csv
import psycopg2
import connection_db
import numpy as np
import math
#campi del dataset userinfo.csv
id = 0
user = 1
date = 2
typeOfValue = 3
value = 4

#crea un file dove per ogni tipo restituisce il numero di samples presenti nel dataset
def create_datasetClusteredByType():
    datasetPath = "data.csv"
    dataset = open(datasetPath, 'r')
    array = np.zeros(28)
    csvreader = csv.reader(dataset)
    print('LEGGO')
    stepsCount = 0
    for row in csvreader:
        type = int(row[typeOfValue])
        array[type] += 1
        if (type == 1):
            stepsCount += 1
    print('Steps: ' + str(stepsCount))
    print('SCRIVO')
    output = open("datasetClusteredByType.txt", 'w+')
    output.write("1: steps: " + str(array[1]) + "\n")
    output.write("2: weight: " + str(+array[2]) + "\n")
    output.write("3:  calculated BMI: " + str(+array[3]) + "\n")
    output.write("4:  systolic blood pressure: " + str(+array[4]) + "\n")
    output.write("5:  pulse wave velocity: " + str(+array[5]) + "\n")
    output.write("6:  PWV healthiness: " + str(+array[6]) + "\n")
    output.write("7:  heart rate avg: " + str(+array[7]) + "\n")
    output.write("8:  heart rate min: " + str(+array[8]) + "\n")
    output.write("9:  heart rate max: " + str(+array[9]) + "\n")
    output.write("10: sleepduration: " + str(+array[10]) + "\n")
    output.write("11: bedin: " + str(+array[11]) + "\n")
    output.write("12: bedout: " + str(+array[12]) + "\n")
    output.write("13: nbawake: " + str(+array[13]) + "\n")
    output.write("14: awakeduration (hours): " + str(+array[14]) + "\n")
    output.write("15: time to sleep (hours): " + str(+array[15]) + "\n")
    output.write("16: time to wake up (hours): " + str(+array[16]) + "\n")
    output.write("17: lightduration: " + str(+array[17]) + "\n")
    output.write("18: remduration: " + str(+array[18]) + "\n")
    output.write("19: deepduration: " + str(+array[19]) + "\n")
    output.write("20: activity type: " + str(+array[20]) + "\n")
    output.write("21: activity duration: " + str(+array[21]) + "\n")
    output.write("22: activity calories: " + str(+array[22]) + "\n")
    output.write("23: activity hr average: " + str(+array[23]) + "\n")
    output.write("24: activity hr minimum: " + str(+array[24]) + "\n")
    output.write("25: activity hr maximum: " + str(+array[25]) + "\n")
    output.write("26: steps gait speed: " + str(+array[26]) + "\n")
    output.write("27: distance gait speed: " + str(+array[27]) + "\n")

    output.close()
    print('DONE')

#crea un file che riporta età e userid dato un determinato type
def createFileByType(type):
    try:
        connection = connection_db.connect()
        cursor = connection.cursor()
        postgreSQL_select_Query = "select distinct users.age, users.userid from dataset join users on dataset.userid=users.userid where type="+str(type)
        cursor.execute(postgreSQL_select_Query)
        print("Selecting data from users join dataset table using cursor.fetchall")
        data = cursor.fetchall()
        output = open("list_age_userid_type"+str(type)+".txt", "w+")
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

def createFileByType_age():
    try:
        connection = connection_db.connect()
        cursor = connection.cursor()
        postgreSQL_select_Query = "select distinct users.age, users.userid from dataset join users on dataset.userid=users.userid"
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

def take_typ5(type):
    connection = connection_db.connect()
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = "select value, userid from dataset where type=5 order by dataset.userid"

        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall()
        output = open("list_age_userid.txt", "w+")
        for i in data:
            output.write(str(i[0]))
            output.write("\t%s\n" % str(i[1]))
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def save_patterns(dict, type, valueMin):
    output = open("Patterns Type "+str(type)+".txt", "w+")
    for key, value in dict.items():
        if(value>valueMin):
            value =  math.sqrt(2*value+1/4) - 1/2
            output.write("%s\t" % key )
            output.write("%s\n" % value)

def save_comparison(dict,type1,type2):
    output = open("Compare Type "+str(type1)+" con "+str(type2)+".txt", "w+")
    for key, values in dict.items():
            output.write("%s" % key )
            output.write("\t%s\n" % values)

def save_percentage(dict):
    output = open("Percentage.txt", "w+")
    for key, values in dict.items():
        output.write("%s :\n" % key)
        for key1, values1 in values.items():
            output.write("\t\t%s : " % key1)
            output.write("%s\n" % values1)
