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
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_states(username, password, dbname)