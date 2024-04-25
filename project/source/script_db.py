import psycopg2


def cria_db():
    conn = psycopg2.connect(
      database="postgres",
      user='postgres',
      password='552277',
      host='localhost',
      port='5432'
    )
    conn.autocommit = True

    cursor = conn.cursor()
    sql_query_create = '''CREATE database analytics_engineering_ada;'''
    cursor.execute(sql_query_create)
    conn.close()
    print("Database criado ok")


conn = psycopg2.connect(
   database="analytics_engineering_ada",
   user='postgres',
   password='552277',
   host='localhost',
   port='5432'
)
conn.autocommit = True

cursor = conn.cursor()
sql_query_create_schema = '''CREATE SCHEMA bronze;'''
cursor.execute(sql_query_create_schema)
conn.close()
print("Schema criado ok")


############################################################################

