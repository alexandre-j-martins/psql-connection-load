import os
import psycopg

from dotenv import load_dotenv


def connect():
    load_dotenv()
    host = os.getenv('PSQL_HOST')
    port = os.getenv('PSQL_PORT')
    db = os.getenv('PSQL_DB')
    user = os.getenv('PSQL_USER')
    password = os.getenv('PSQL_PASS')

    conn_string = "postgresql://{}:{}@{}:{}/{}".format(user, password, host, port, db)
    return psycopg.connect(conn_string)

def select():
    conn = connect()
    with conn.cursor() as cur:
        query = "SELECT first_name, last_name FROM artist"
        cur.execute(query)
        artists = cur.fetchall()
        for artist in artists:
            print(artist[0], artist[1])


select()
