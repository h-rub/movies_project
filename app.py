import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')

def connect_to_database(db):
    con = sqlite3.connect(db)
    return con, con.cursor()

con, cursor = connect_to_database(DB_NAME)

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS movie(title TEXT NOT NULL, year INTEGER NOT NULL, score REAL)")

def save_movie(title, year, score):
    cursor.execute("""INSERT INTO movie 
                (title, year, score) VALUES 
                (?, ?, ?)
            """, (title, year, score))
    con.commit()

def select_all_movies():
    cursor.execute("SELECT * FROM movie")
    lista_movies = cursor.fetchall()
    return lista_movies

# save_movie("Ratatouille", 2007, 9.0)

lista_movies = select_all_movies()

for movie in lista_movies:
    print(movie)
