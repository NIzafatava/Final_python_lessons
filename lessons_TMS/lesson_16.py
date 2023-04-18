# import pip

import psycopg2

from functools import lru_cache


# Warning Never, never, NEVER use Python string concatenation (+)
# or string parameters # interpolation (%) to pass variables
# to a SQL query string. Not even at gunpoint.


@lru_cache(maxsize=1)
def get_db_connection():
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='izofatova123',
        database='lessondb',
    )
    connection.autocommit = True  # сохранять изменения автоматически после каждого запроса, иначе нужно самим вызывать commit()
    return connection


def run_db_queries(db_connection):
    with db_connection.cursor() as cursor:
        # population_boundary = 100
        str_pattern = 'J%'
        # cursor.execute('SELECT * FROM country1 WHERE population > %s AND name LIKE %s', (population_boundary, str_pattern))
        cursor.execute('SELECT * FROM country1 WHERE name LIKE %s', (str_pattern, ))
        countries = cursor.fetchall()
        # cursor.commit()
        print(countries)


if __name__ == '__main__':
    db_connection = get_db_connection()

    run_db_queries(db_connection)

    db_connection.close()
    get_db_connection.cache_clear()


################## ORM ##################






