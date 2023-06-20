# global imports
import psycopg2
from psycopg2.extensions import parse_dsn

# Connect to postgres DB
connection = psycopg2.connect(parse_dsn('postgresql://postgres:bjOVNjyp6khBGM5VZ6F5@containers-us-west-63.railway.app:7097/railway'))


from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db =



# Connect to postgres DB
# conn = psycopg2.connect("dbname=test user=postgres")
connection = psycopg2.connect(parse_dsn('postgresql://postgres:bjOVNjyp6khBGM5VZ6F5@containers-us-west-63.railway.app:7097/railway'))


