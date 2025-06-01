from dotenv import load_dotenv
import os
import psycopg2

# Load .env variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    print("✅ Connected to the database!")

    # Run a test query
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("🧠 PostgreSQL version:", version[0])

    cur.close()
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)

