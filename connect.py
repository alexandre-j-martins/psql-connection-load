import os
import psycopg
import time

from concurrent.futures import ThreadPoolExecutor, as_completed
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

def select(i):
    conn = connect()
    with conn.cursor() as cur:
        query = "SELECT first_name, last_name FROM artist"
        cur.execute(query)
        artists = cur.fetchall()
        for artist in artists:
            print("Thread", i, artist[0], artist[1])


def main():
    warm_up = 10
    print("Initializing in {} seconds...".format(warm_up))
    time.sleep(10)
    start = time.time()
    num_threads = 20   # number of simultaneous connections
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(select, i) for i in range(num_threads)]

        for future in as_completed(futures):
            print(future.result())

    print("Total time:", time.time() - start)

if __name__ == "__main__":
    main()
