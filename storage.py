import sqlite3

def connect_to_database(db):
    con = sqlite3.connect(db)
    return con, con.cursor()

def select_all_movies(cursor):
    cursor.execute("SELECT * FROM movie")
    lista_movies = cursor.fetchall()
    return lista_movies

def save_movie(con, cursor, movie):
    cursor.execute("""INSERT INTO movie 
                (title, year, score) VALUES 
                (?, ?, ?)
            """, (movie.title, movie.year, movie.score))
    con.commit()
    print(f"Película '{movie.title}' almacenada exitosamente ")

def delete_movie(con, cursor, title):
    cursor.execute("""DELETE FROM movie
            WHERE title = ?
    """, (title, ))
    con.commit()
    print(f"Película '{title}' eliminada exitosamente")

# class SQLiteStorage:
#     def __init__(self, db):
#         self.db = db
    
#     def connect_to_database(self):
#         con = sqlite3.connect(self.db)
#         self.con = con
#         self.cursor = con.cursor()
#         return con, con.cursor()

#     def select_all_registers(self, model):
#         cursor.execute(f"SELECT * FROM {model}")
#         all_register = self.cursor.fetchall()
#         return all_register
    
# storage = SQLiteStorage("")

# con, cursor = storage.connect_to_database()

# storage.select_all_registers("Movie")