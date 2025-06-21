import psycopg2
import os

def create_table():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id SERIAL PRIMARY KEY,
            name TEXT,
            mobile TEXT,
            arrival TEXT,
            departure TEXT,
            persons INTEGER,
            children INTEGER,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Bookings table created successfully.")
