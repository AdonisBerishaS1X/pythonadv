from lib2to3.pgen2.tokenize import detect_encoding

from dagestan import response
from fastapi import FastApi, HHTPException
from typing import List
import database
import models
from models import Movie, MovieCreate

app = FastApi()

@app.get('/')
def read_root():
    return {"Message": "Welcome to the movies CRUD API"}

@app.get('/movies/', response_model = List[Movie])
def read_movies():
    return database.read_movies()

@app.get('/movies/{movie_id}', response_model = Movie)
def read_movies(movie_id: int):
    movie = database.read_movie(movie_id)
    if movie is None:
        raise HHTPException(status_code=404, detail="Movie not found")
    return movie

@app.get('/movie/{movie_id}', response_model = Movie)
def read_movies(movie_id: int):