import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234",
    port=5433
)
print("Connected:", conn.closed == 0)
conn.close()
