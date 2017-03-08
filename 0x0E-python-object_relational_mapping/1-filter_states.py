#!/usr/bin/python3
# List all states with a name starting with uppercase N
# Username, password, and database names are given as user args
import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3],
                     host='localhost',
                     port=3306)
cur = db.cursor()
cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
nStates = cur.fetchall()

for state in nStates:
    print(state)

cur.close()
db.close()
