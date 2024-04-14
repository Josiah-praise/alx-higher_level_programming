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

    username, password, database, state_name_arg = sys.argv[1:]

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
            SELECT cities.name AS city
            FROM cities INNER JOIN states
            ON cities.state_id=states.id
            WHERE states.name LIKE BINARY %s
            ORDER BY cities.id ASC
            """,
            (state_name_arg,)
        )

        result = cursor.fetchall()
        print(", ".join([row[0] for row in result]))


if __name__ == "__main__":
    list_cities_by_states()
