import sqlite3
from venv import create

from models import Movie, MovieCreate


def create_conn():
    connection = sqlite3.connect("movies.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute('''
    create table if not exists movies(
        id integer primary key autoincrement,
        title text not null,
        director text not null
    )
    ''')
    conn.commit()
    conn.close()

create_table()

def create_movie(movie: MovieCreate) -> int:
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute("Insert into movies (title, director) values (?, ?)", (movie.title, movie.director))
    conn.commit()
    movie_id = cursor.lastrowid
    conn.close()
    return movie_id

def read_movies():
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute("select * from movies")
    rows = cursor.fetchall()
    conn.close()
    movies = [Movie(id = row[0], title = row[1], director = row[2]) for row in rows]
    return movies

def read_movie(movie_id: int):
    conn = create()
    cursor = conn.cursor()
    cursor.execute("select * from movies where id = ?", (movie_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return None
    return Movie(id = row["id"], title = row["title"], director = row["director"])

def update_movie(movie_id: int) -> bool:
    conn = create_conn()
    cursor = conn.cursor()

    cursor.execute("update movies set title = ?, director = ? where id = ?", (movie.title, movie.director, movie_id))
    conn.commit()
    update = cursor.rowcount
    conn.close()
    return update > 0

def delete_movie(movie_id: int) -> bool:
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute("delete from movies where id = ?", (movie_id,))
    conn.commit()
    delete = cursor.rowcount
    conn.close()
    return delete > 0