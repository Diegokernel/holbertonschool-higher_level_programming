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

    ro = cur.fetchall()
    ci = []
    for i in ro:
        ci.append(i[1])
    print(*ci, sep=", ")
    cur.close()
    db.close()
