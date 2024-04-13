#!/usr/bin/python3

'''
lists all states with a name that matches the
argument given from the database
'''


def list_all_states():
    '''
    list all states from database hbtn_0e_0_usa
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
        cursor.execute("SELECT * FROM tv_genres\
            WHERE name = %s ORDER BY id", (sys.argv[4],))

        for row in cursor.fetchall():
            print(row)


if __name__ == '__main__':
    list_all_states()
