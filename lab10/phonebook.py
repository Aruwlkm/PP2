import psycopg2
import csv
def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="1234",
        port=5433
    )

def create_table():
    sql = """
        CREATE TABLE phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            phone VARCHAR(20)
        );
    """
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print("Table created!")
    except Exception as e:
        print("Error creating table:", e)

def insert_user(first_name, phone):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
            (first_name, phone)
        )
        conn.commit()
        cur.close()
        conn.close()
        print("User added!")
    except Exception as e:
        print("Error inserting user:", e)

def insert_from_csv(filename):
    try:
        conn = connect()
        cur = conn.cursor()
        with open(filename, encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )
        conn.commit()
        cur.close()
        conn.close()
        print("CSV data inserted!")
    except Exception as e:
        print("Error inserting CSV:", e)

def update_user(name, new_phone):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE first_name = %s",
            (new_phone, name)
        )
        conn.commit()
        cur.close()
        conn.close()
        print("User updated!")
    except Exception as e:
        print("Error updating user:", e)

def search(name=None):
    try:
        conn = connect()
        cur = conn.cursor()
        if name:
            cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
        else:
            cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    except Exception as e:
        print("Error fetching users:", e)

def delete_user(name):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
        conn.commit()
        cur.close()
        conn.close()
        print("User deleted!")
    except Exception as e:
        print("Error deleting user:", e)

if __name__ == "__main__":
  create_table()
insert_from_csv("data.csv")