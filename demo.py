import psycopg2

conn = psycopg2.connect('dbname=amy user=postgres password=secret" ')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS persons;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE persons (
    id serial PRIMARY KEY,
    name VARCHAR NOT NULL
  );
""")
SQL = 'INSERT INTO persons (id, name) VALUES (%(id)s, %(name)s);'
data = {
  'id': 2, 'name':'mazen'
}
cur.execute(" INSERT INTO persons (id, name) VALUES (%s, %s);", (1, 'Abdelfattah'))
cur.execute(SQL, data)


# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()