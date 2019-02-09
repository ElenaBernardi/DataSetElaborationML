import os
import sys
import psycopg2
import argparse
import csv

def saveData():

    conn = psycopg2.connect("host=localhost dbname=ActivityTracker user=postgres port=5433 password=2912")
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