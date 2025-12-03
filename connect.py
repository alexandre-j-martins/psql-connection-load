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
    psycopg.connect(conn_string)
    return

connect()