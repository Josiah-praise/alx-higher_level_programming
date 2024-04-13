#!/usr/bin/python3

"""gets all states from database hbtn_0e_0_usa
"""


def get_all_states():
    '''
    gets all states from database hbtn_0e_0_usa
    '''

    import MySQLdb
    import sys

    db = MySQLdb.Connection(
        user=sys.argv[1],
        passwd=sys.argv[2],
        host='localhost',
        db=sys.argv[3])

    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM STATES ORDER BY id')

        for row in cursor.fetchall():
            print(row)


if __name__ == '__main__':
    get_all_states()
