#!/usr/bin/python3

'''
 lists all cities from the database passed as argument
 to the script
'''


def list_cities_by_states():
    '''
    lists all cities from the database passed as argument
    to the  script
    '''
    import sys
    import MySQLdb

    username, password, database = sys.argv[1:]

    connection = MySQLdb.connect(
        user=username,
        host='localhost',
        db=database,
        passwd=password,
        port=3306
    )

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT cities.id AS id, cities.name AS city, states.name AS state
            FROM cities INNER JOIN states
            ON cities.state_id=states.id
            ORDER BY id ASC
            """
        )

        result = cursor.fetchall()
        for each in result:
            print(each)


if __name__ == "__main__":
    list_cities_by_states()
