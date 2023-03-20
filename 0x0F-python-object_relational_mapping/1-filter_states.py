#!/usr/bin/python3
"""A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=arg[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
        )

    cursor=db.cursor()
    cursor.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC")
    rows = cursor.fetchball()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
