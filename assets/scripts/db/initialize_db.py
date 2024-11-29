import sqlite3

conn = sqlite3.connect('db/time2learn.db')
c = conn.cursor()

# Create tables
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    avatar TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    lesson TEXT NOT NULL,
    score INTEGER
)
''')

conn.commit()
conn.close()

print("Database initialized successfully.")
