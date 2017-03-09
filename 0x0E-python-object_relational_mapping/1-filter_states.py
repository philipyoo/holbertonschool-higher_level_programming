#!/usr/bin/python3
# List all states with a name starting with uppercase N
# Username, password, and database names are given as user args
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cmd = """SELECT id, name
             FROM states
             WHERE name LIKE 'N%'
             ORDER BY id ASC;"""
    cur.execute(cmd)
    nStates = cur.fetchall()

    for state in nStates:
        if (state[1][0] == 'N'):
            print(state)

    cur.close()
    db.close()
