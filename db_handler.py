import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


data_dir = BASE_DIR / "storage"
data_dir.mkdir(exist_ok=True)

file_path = data_dir / "notes.db"


with sqlite3.connect(file_path) as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT,
        full_text TEXT, 
        create_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")


def add_note(user_title, user_text):
    with sqlite3.connect(file_path) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO notes (title, full_text) VALUES (?, ?);", (user_title, user_text))
        db.commit()


def get_all_notes():
    with sqlite3.connect(file_path) as db:
        cursor.execute("SELECT * FROM notes")
        return (cursor.fetchall())


def delete_note(delete_choise):
    with sqlite3.connect(file_path) as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM notes WHERE title = ?", (delete_choise,))
        db.commit()


def delete_all_notes():
    with sqlite3.connect(file_path) as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM notes")
        db.commit()
