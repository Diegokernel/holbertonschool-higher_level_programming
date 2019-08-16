#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %(id)s", {'id': argv[4]})

    rows = cur.fetchall()
    ci = []
    for data in rows:
        for i in data:
            ci.append(i)
    print(', '.join(ci))
    cur.close()
    db.close()
