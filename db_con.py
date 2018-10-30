import psycopg2
from psycopg2.extras import RealDictCursor

db_url= "dbname = 'store_manager' user = 'mwangemi' host ='localhost' port ='5432' password='123'"
    
class DbSetup():
    def __init__(self):
        self.conn = psycopg2.connect(db_url)
   
    def create_tables(self):
        conn = self.conn
        cur = self.cursor()
        queries = self.tables()
        for query in queries:
            cur.execute(query)
        conn.commit()
    
    def tables(self):
        query1="""
        CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            fname varchar NOT NULL,
            lname varchar NOT NULL,
            email varchar NOT NULL,
            password varchar NOT NULL,
            role varchar NOT NULL,
            created_on timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
        )
        """
        query2="""
        CREATE TABLE IF NOT EXISTS products(
            id serial PRIMARY KEY,
            product_name varchar NOT NULL,
            category varchar NOT NULL,
            quantity integer NOT NULL,
            price integer NOT NULL,
            description varchar,
            created_at timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
        )
        """
        query3="""
        CREATE TABLE IF NOT EXISTS sales(
            id serial PRIMARY KEY,
            product_name varchar NOT NULL,
            quantity numeric NOT NULL,
            stock_quantity numeric NOT NULL,
            price numeric NOT NULL,
            total numeric NOT NULL,
            created_by varchar,
            created_at timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
        )
        """

        queries=[query1,query2,query3]
        return queries

    def cursor(self):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        return cur