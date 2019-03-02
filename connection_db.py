import psycopg2


def connect():
    connection = psycopg2.connect(user="postgres",
                                  password="22021996",


                                  host="localhost",
                                  database="ActivityTracker")
    return connection
