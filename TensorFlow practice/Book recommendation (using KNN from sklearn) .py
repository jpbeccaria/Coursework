# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:29:19 2022

@author: Juan
"""

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from operator import itemgetter 
import requests, zipfile, io

url = 'https://cdn.freecodecamp.org/project-data/books/book-crossings.zip'


r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

books_filename = 'BX-Books.csv'
ratings_filename = 'BX-Book-Ratings.csv'

books_filename = 'BX-Books.csv'
ratings_filename = 'BX-Book-Ratings.csv'


# import csv data into dataframes
df_books = pd.read_csv(
    books_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['isbn', 'title', 'author'],
    usecols=['isbn', 'title', 'author'],
    dtype={'isbn': 'str', 'title': 'str', 'author': 'str'})

df_ratings = pd.read_csv(
    ratings_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['user', 'isbn', 'rating'],
    usecols=['user', 'isbn', 'rating'],
    dtype={'user': 'int32', 'isbn': 'str', 'rating': 'float32'})

# Nos quedamos con el dataset de reviews de libros que tienen AL MENOS 100 REVISIONES.
number_reviews = df_ratings['isbn'].value_counts()
number_reviews_filt = number_reviews[number_reviews >= 100]
df_ratings_filt = df_ratings[df_ratings['isbn'].isin(number_reviews_filt.index)]

# Nos quedamos con el dataset de reviews de libros los que tengan usuarios con al menos 200 revisiones.
count_reviewers = df_ratings['user'].value_counts()
count_reviewers_filt = count_reviewers[count_reviewers >= 200]
df_ratings_filt2 = df_ratings_filt[df_ratings_filt['user'].isin(count_reviewers_filt.index)]

# Merge de los dos df
df_final = pd.merge(df_books, df_ratings_filt2, on='isbn')
df_final.describe()


# Pivote proccess detected duplicate values. Let's remove it and create the matrix to fed the model.

df_final.drop_duplicates(subset=["title", "user"], inplace=True)
df_final_pivot = df_final.pivot(index = 'title', columns = 'user', values = 'rating').fillna(0)
df_final_matrix = csr_matrix(df_final_pivot.values)

# Creating model

model_knn = NearestNeighbors(algorithm='brute', metric='cosine')
model_knn.fit(df_final_matrix)


# function to return recommended books - this will be tested

def get_recommends(book = "" ):
      
    X = df_final_pivot[df_final_pivot.index == book]  # Encode the name of the book we are looking for into our matrix's name
    X = X.to_numpy().reshape(1,-1)                    # Reshape cos it's necesary :P
    
    prediction = model_knn.kneighbors(X, 6, return_distance = True)              # predict base on our model
    distances = prediction[0]                                                    # We get 2 lists, neighbords and distances
    books_indx = prediction[1]
    book_neig = []
    c = 1
    while c <= 5:                                                               # cicle to translate neighbord's names into real ones
        book_neig.append(df_final_pivot.iloc[books_indx[0, c]].name)
        c += 1      
    recommended_books = []   
    recommended_books.append(book) 
    lista_recom = []  
    c = 0
    while c <= 4:                                                              # cicle append into the same list, neighbord and distances.
        elementos = []
        elementos.append(book_neig[c])
        elementos.append(distances[0, c + 1])
        lista_recom.append(elementos)
        c += 1       
    sorted_list = sorted(lista_recom,reverse = True, key=itemgetter(1))         # sort by distance
    
    recommended_books.append(sorted_list) 
    return recommended_books


books = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
print(books)

def test_book_recommendation():
  test_pass = True
  recommends = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
  if recommends[0] != "Where the Heart Is (Oprah's Book Club (Paperback))":
    test_pass = False
  recommended_books = ["I'll Be Seeing You", 'The Weight of Water', 'The Surgeon', 'I Know This Much Is True']
  recommended_books_dist = [0.8, 0.77, 0.77, 0.77]
  for i in range(2): 
    if recommends[1][i][0] not in recommended_books:
      test_pass = False
    if abs(recommends[1][i][1] - recommended_books_dist[i]) >= 0.05:
      test_pass = False
  if test_pass:
    print("You passed the challenge! 🎉🎉🎉🎉🎉")
  else:
    print("You haven't passed yet. Keep trying!")

test_book_recommendation()
