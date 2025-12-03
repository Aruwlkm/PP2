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

def create_table(): #first_name and phonebook  бар кесте куру
    sql = """
        CREATE TABLE IF NOT EXISTS phonebook ( 
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) UNIQUE,
            phone VARCHAR(20)
        );
    """
    try:
        conn = connect()
        cur = conn.cursor() #дереккормен жумыс истеуге арналган
        cur.execute(sql)
        conn.commit()  # озгеристи сактау
        cur.close()
        conn.close()
        print("Table created!")
    except Exception as e:
        print("Error creating table:", e)
def insert_or_update_from_csv(filename):
    try:
        conn = connect()
        cur = conn.cursor()
        with open(filename, encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  
            for row in reader:
                cur.execute("""
                    INSERT INTO phonebook (first_name, phone)
                    VALUES (%s, %s)
                    ON CONFLICT (first_name)
                    DO UPDATE SET phone=EXCLUDED.phone;
                    """,(row[0], row[1]))
        conn.commit()
        cur.close()
        conn.close()
        print("CSV data inserted!")
    except Exception as e:
        print("Error inserting CSV:", e)
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
         
# 1тапсырма
def create_search_function():
    sql = """
    CREATE OR REPLACE FUNCTION search_phonebook(p_pattern TEXT)
    RETURNS SETOF phonebook
    LANGUAGE plpgsql
    AS $$
    BEGIN
        RETURN QUERY
        SELECT *
        FROM phonebook
        WHERE first_name ILIKE '%' || p_pattern || '%'
           OR phone ILIKE '%' || p_pattern || '%';
    END;
    $$;
    """
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print("search_phonebook FUNCTION created!")
    except Exception as e:
        print("Error creating search function:", e)

def search_by_pattern(pattern):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    except Exception as e:    
        print("Error searching by pattern:", e)          #SELECT * FROM search_phonebook('Di');

  # 2 тапсырма
def create_upsert_function():
    sql = """
    CREATE OR REPLACE FUNCTION upsert_phonebook(p_name VARCHAR, p_phone VARCHAR)
    RETURNS VOID
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
            UPDATE phonebook
            SET phone = p_phone
            WHERE first_name = p_name;
        ELSE
            INSERT INTO phonebook(first_name, phone)
            VALUES (p_name, p_phone);
        END IF;
    END;
    $$;
    """
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print("upsert_phonebook FUNCTION created!")
    except Exception as e:
        print("Error creating upsert function:", e)

def upsert_user_proc(name, phone):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT upsert_phonebook(%s, %s);", (name, phone))
        conn.commit()
        cur.close()
        conn.close()
        print("User inserted/updated via procedure!")
    except Exception as e:
        print("Error in upsert_user_proc:", e)                #  SELECT upsert_phonebook('Dias', '87070000000');
                                                              #  SELECT upsert_phonebook('Dias', '87074444444'); -- update болады
                                                              #  SELECT * FROM phonebook;

 
 #3 тапсырма
def create_insert_many_function():
    sql = """
    CREATE OR REPLACE FUNCTION insert_many_users(
        p_names  TEXT[],
        p_phones TEXT[]
    )
    RETURNS TABLE(bad_name TEXT, bad_phone TEXT)
    LANGUAGE plpgsql
    AS $$
    DECLARE
        i INT;
    BEGIN
        IF array_length(p_names, 1) IS DISTINCT FROM array_length(p_phones, 1) THEN
            RAISE EXCEPTION 'Arrays must have same length';
        END IF;

        FOR i IN 1 .. array_length(p_names, 1) LOOP
            -- қарапайым телефон тексеру: + және цифралар, ұзындық 5–20
            IF p_phones[i] ~ '^[0-9+]{5,20}$' THEN
                PERFORM upsert_phonebook(p_names[i], p_phones[i]);
            ELSE
                bad_name  := p_names[i];
                bad_phone := p_phones[i];
                RETURN NEXT;
            END IF;
        END LOOP;
    END;
    $$;
    """
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print("insert_many_users FUNCTION created!")
    except Exception as e:
        print("Error creating insert_many function:", e)

def insert_many_from_list(data):
    """
    data = [("Dias","8707..."), ("Ali","8777..."), ("Bad","xxx")]
    """
    names = [row[0] for row in data]
    phones = [row[1] for row in data]

    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM insert_many_users(%s, %s);", (names, phones))
        bad_rows = cur.fetchall()                          
        cur.close()
        conn.close()
        print("Invalid rows:", bad_rows)  # неправильные данные
    except Exception as e:
        print("Error in insert_many_from_list:", e)         #SELECT * FROM insert_many_users(
                                                            #ARRAY['Dias','Alma','BadUser','Nura'],
                                                            #ARRAY['87075554433','+77001112233','xxx','87078889900'];


# 4 тапсырма
def create_pagination_function():
    sql = """
    CREATE OR REPLACE FUNCTION get_phonebook_page(p_limit INT, p_offset INT)
    RETURNS SETOF phonebook
    LANGUAGE plpgsql
    AS $$
    BEGIN
        RETURN QUERY
        SELECT *
        FROM phonebook
        ORDER BY id
        LIMIT p_limit OFFSET p_offset;
    END;
    $$;
    """
    try:
        conn = connect()
        cur = conn.cursor()                           #SELECT * FROM get_phonebook_page(5, 0);
                                                      #SELECT * FROM get_phonebook_page(5, 5);
                                                      #SELECT * FROM get_phonebook_page(5, 10);

        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print("get_phonebook_page FUNCTION created!")
    except Exception as e:
        print("Error creating pagination function:", e)

def get_page(limit, offset):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_phonebook_page(%s, %s);", (limit, offset))
        rows = cur.fetchall()
        for row in rows:
            print(row)       #limit- лимит мысалы 5, 5сан гана шыгарады
        cur.close()          #offset- мысалы 4, 4санды откизип жиберу
        conn.close()
    except Exception as e:
        print("Error in get_page:", e)
#5 тапсырма
def create_delete_function():
    sql = """
    CREATE OR REPLACE FUNCTION delete_from_phonebook(
        p_name  TEXT DEFAULT NULL,
        p_phone TEXT DEFAULT NULL
    )
    RETURNS INTEGER
    LANGUAGE plpgsql
    AS $$
    DECLARE
        deleted_count INT;
    BEGIN
        DELETE FROM phonebook
        WHERE (p_name  IS NOT NULL AND first_name = p_name)
           OR (p_phone IS NOT NULL AND phone = p_phone);

        GET DIAGNOSTICS deleted_count = ROW_COUNT;
        RETURN deleted_count;
    END;
    $$;
    """
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print("delete_from_phonebook FUNCTION created!")
    except Exception as e:
        print("Error creating delete function:", e)
def delete_by(name=None, phone=None):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT delete_from_phonebook(%s, %s);", (name, phone))
        deleted = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        print("Deleted rows:", deleted)
    except Exception as e:
        print("Error in delete_by:", e)

if __name__ == "__main__":
  create_table()
  create_search_function()
  create_upsert_function()
  create_insert_many_function()
  create_pagination_function()
  create_delete_function()
  insert_or_update_from_csv("/Users/macbook/Documents/GitHub/PP2/lab11/data.csv")
  search_by_pattern("Di")  # 1task
  search_by_pattern("as")

  upsert_user_proc("Dias","87070000000")  #2task
  upsert_user_proc("Dias","87075555555")

  data=[
      ("Dias","87075554433"),   #3task
      ("Alma","+77001112233"),
      ("NotBad","aaa"),
      ("Nura","87078889900")
  ]
  insert_many_from_list(data)

  get_page(5,0)   #4task       
  get_page(5,10)
  
  delete_by(name="Aru")              #5 task
  delete_by(phone="+77055678942")
  search()

