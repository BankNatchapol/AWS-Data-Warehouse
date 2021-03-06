import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Description: This function use to execute all copy table queries to 
    load data into staging tables.
    Arguments:
        cur: the cursor object.
        conn: connection to database.
    Returns:
        None
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Description: This function use to execute all insert table queries to 
    insert data into tables.
    Arguments:
        cur: the cursor object.
        conn: connection to database.
    Returns:
        None
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    print('loading staging tables ...')
    load_staging_tables(cur, conn)
    print('inserting tables ...')
    insert_tables(cur, conn)
    print('finish!')

    conn.close()


if __name__ == "__main__":
    main()