#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

def list_states(username, password, dbname):
    """
    Connects to a MySQL database and prints all states sorted by states.id.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.DatabaseError as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")