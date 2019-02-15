import os
import sys
import psycopg2
import argparse
import csv
import connection_db

def saveDataUser():

    conn = connection_db.connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE users(
        id integer PRIMARY KEY,
        userID text,
        time_zone text,
        none text,
        gender text,
        age integer, 
        value integer   
    )
    """)
    with open('userinfo.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row.
        for row in reader:
            cur.execute(
                "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s)",
                row
            )
    conn.commit()

def saveDataset():

    conn = connection_db.connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE dataset(
        id integer PRIMARY KEY,
        userID text,
        date text,
        type integer, 
        value float   
    )
    """)
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row.
        j=0;
        for row in reader:
            cur.execute(
                "INSERT INTO dataset VALUES (%s, %s, %s, %s, %s)",
                row
            )
            print(j)
            j=j+1
    conn.commit()