import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# descargar recursos necesarios
nltk.download('stopwords')

def read_movie(filepath):    
    # verifica si el archivo existe
    if os.path.exists(filepath):
        movies = pd.read_csv(filepath)
        return movies
    else:
        raise FileNotFoundError(f"El archivo {filepath} no existe")
    
def preprocess_text(text):
    # verificar que no estemos intentando procesar algo que no sea una cadena de texto
    if not isinstance(text, str):
        return ""
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english')) # Conjunto de palabras vacías
    
    # guardar en filtered_tokens aquellas palabras que no sean vacías ('the', 'and', 'is')
    filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words]
    return ' '.join(filtered_tokens) # Devolver una cadena de texto con los tokens filtrados

def recommend_movie(movie_title):
    # filtrar el dataframe para encontrar la película que le pasamos
    filtered_movie = new_data[new_data['title'].str.contains(movie_title, case=False)]
    
    # si no esta vacío
    if not filtered_movie.empty:
        index = filtered_movie.index[0] # obtener el índice en el dataframe de la película
        
         # guardar en 'distance' una lista con las peliculas similares a la película en el indice 4.
         # se usa una función lambda para decir que ordene la lista por similaridad (vector[1] = vector[similaridad]) 
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    
        # print(distance) --> si printeamos esto, nos muestra una matriz gigante (xD) que tiene
        # [(indice de película, similaridad con la peli en el indice 4)    
    
        print(f"La película {movie_title} tiene estas películas similares: ")
        # mostrar los titulos de las películas similares a la 5ta película
        for i in distance[1:6]:
            print(new_data.iloc[i[0]].title)
    else:
        print("No se encontro la película ingresada")
      
    
if __name__ == "__main__":
    filepath = "../data/movies2.csv"
   
    # leer el dataset 
    movie_data = read_movie(filepath)
    
    # crear una nueva columna 'tags' mezclando descripción y género
    movie_data['tags'] = movie_data['overview'] + movie_data['genre']
    
    # nuevo dataframe eliminando las columnas 'overview' y 'genre', ya que ahora son redundantes
    new_data = movie_data.drop(columns=['overview', 'genre'])
    
    # aplicar el preprocesamiento de los 'tags' de las películas
    new_data['tags_clean'] = new_data['tags'].astype(str).apply(preprocess_text)
    
    # eliminar filas con tags_clean NaN
    new_data = new_data.dropna(subset=['tags_clean'])
    
    # vectoriza los tags de las películas
    vectorizer = CountVectorizer(max_features=5000, stop_words='english')
    vectorized_data = vectorizer.fit_transform(new_data['tags_clean']).toarray()
    
    # calcular la similitud del coseno para ver que tan similares son los vectores
    # es decir, que tan similares son las películas 
    similarity = cosine_similarity(vectorized_data)

    movie_name = input("Ingrese un nombre de película (en inglés) y obtenga películas similares: ")
        
    recommend_movie(movie_name)
    
