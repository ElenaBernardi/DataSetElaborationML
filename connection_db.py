import psycopg2


def connect():
    connection = psycopg2.connect(user="postgres",
                                  password="2912",
                                  port = "5433",

                                  host="localhost",
                                  database="ActivityTracker")
    return connection
