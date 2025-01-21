import pytest
import sqlite3
from contextlib import contextmanager

class UserDatabase:
    def __init__(self, db_name=":memory:"):
        self.db_name = db_name
        
    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        try:
            yield conn
        finally:
            conn.close()
            
    def setup_database(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                )
            """)
            conn.commit()
    
    def add_user(self, name, email):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            return cursor.lastrowid

@pytest.fixture
def db():
    database = UserDatabase()
    database.setup_database()
    return database

def test_add_user(db):
    user_id = db.add_user("João Silva", "joao@email.com")
    assert user_id == 1
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        assert user is not None
        assert user[1] == "João Silva"
        assert user[2] == "joao@email.com"

def test_duplicate_email(db):
    db.add_user("João Silva", "joao@email.com")
    with pytest.raises(sqlite3.IntegrityError):
        db.add_user("Maria Silva", "joao@email.com")
