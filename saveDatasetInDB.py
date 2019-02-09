import os
import sys
import psycopg2
import argparse
import csv

def saveData():

    conn = psycopg2.connect("host=localhost dbname=ActivityTracker user=postgres port=5433 password=2912")
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