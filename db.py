# db.py
import sqlite3

DB_NAME = 'config.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS webhooks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        url TEXT NOT NULL,
        description TEXT
    )''')
    conn.commit()
    conn.close()


def get_webhooks():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT id, title, url, description FROM webhooks')
    rows = c.fetchall()
    conn.close()
    return rows


def add_webhook(title, url, description):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO webhooks (title, url, description) VALUES (?, ?, ?)', (title, url, description))
    conn.commit()
    conn.close()

