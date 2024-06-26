#!/usr/bin/python3

'''
lists all states with a name that matches the
argument given from the database
'''


def filter_states():
    '''
    list all states from database hbtn_0e_0_usa that match
    the argument passsed to the script
    '''

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        host='localhost',
        db=sys.argv[3],
        port=3306)

    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM states\
            WHERE name LIKE BINARY %s ORDER BY states.id ASC", (sys.argv[4],))
        result = cursor.fetchall()
        for row in result:
            print(row)


if __name__ == '__main__':
    filter_states()
