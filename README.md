## SISTEMA DE RECOMENDACIÓN DE PELICULAS

Vamos a crear un sistema de recomendación de películas basado en que tan similares son.

Usaremos `python` y `pandas`, también utilizaremos otras herramientas, como `CountVectorizer` y conceptos como la similitud del coseno (de la librería `scikit`).

## AYUDAS

Qué hace CountVectorizer? Convierte una colección de docs de texto en una matriz de tokens contados.

Más detallado: 

* Para entender cómo funciona CountVectorizer, analicemos las matemáticas que lo sustentan. El algoritmo comienza creando un diccionario de todas las palabras únicas presentes en el texto. Luego, cuenta las apariciones de cada palabra en cada documento, lo que da como resultado una representación matricial de los datos del texto. Esta matriz captura la frecuencia de cada palabra, lo que permite realizar más análisis y comparaciones.

Qué es la tokenización?
* La tokenización, es el proceso de dividir el texto en palabras individuales o tokens. Facilita el análisis y la cuantificación.

Ejemplo:
```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
vectorizer.get_feature_names_out()
array(['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third',
       'this'], ...)
print(X.toarray())
```
Explicación:

`corpus`: Es una lista de strings, donde cada string representa un documento.

`vectorizer = CountVectorizer()`: Crea una instancia de `CountVectorizer`.

`X = vectorizer.fit_transform(corpus)`: Este método hace dos cosas:

`fit`: Aprende el vocabulario del `corpus` (identifica las palabras únicas).

`transform`: Transforma los documentos en una matriz de conteo de palabras. Cada fila de la matriz corresponde a un documento y cada columna a una palabra del vocabulario aprendido. El valor en la matriz representa el número de veces que la palabra aparece en el documento.

`vectorizer.get_feature_names_out()`: Devuelve una lista de las características del vocabulario, es decir, las palabras únicas encontradas en el corpus.

`X.toarray()`: Convierte la matriz de conteo de palabras en un array de NumPy. Cada fila del array representa un documento y cada columna representa una palabra del vocabulario.

Salida de `X.toarray()`:
[[0 1 1 1 0 0 1 0 1]
 [0 2 0 1 0 1 1 0 1]
 [1 0 0 1 1 0 1 1 1]
 [0 1 1 1 0 0 1 0 1]]

Este vector muestra la cantidad de veces que una palabra o token aparece en el texto. Por ejemplo, en la fila 1 (iniciando la primera en 0) y en la columna 1 (también iniciando la primera en 0) vemos que 'document' aparece dos veces.

Qué es la similitud del coseno? 

* La similitud coseno es una medida de la similitud existente entre dos vectores en un espacio que posee un producto interior con el que se evalúa el valor del coseno del ángulo comprendido entre ellos. Esta función trigonométrica proporciona un valor igual a 1 si el ángulo comprendido es cero, es decir si ambos vectores apuntan a un mismo lugar. Cualquier ángulo existente entre los vectores, el coseno arrojaría un valor inferior a uno. Si los vectores fuesen ortogonales el coseno se anularía, y si apuntasen en sentido contrario su valor sería -1. De esta forma, el valor de esta métrica se encuentra entre -1 y 1, es decir en el intervalo cerrado [-1,1].

* Supongamos que "Iron Man" está vectorizado como [0, 1, 2] y "Los Vengadores" está vectorizado como [1, 1, 1], el puntaje de similitud calculado ayudará a determinar qué tan cerca está "Los Vengadores" de "Iron Man" en términos de contenido.

## DATASET

Vamos a trabajar con un dataset de películas extraído de `Kaggle`, es importante realizar algunas acciones en nuestro dataser, tales como tokenizarlo y "limpiarlo", para esto usamos la librería `nltk`.

Al tokenizar el dataset, dividimos el texto en tokens (palabras). Por ejemplo, si el texto dice "Hola Mundo, que tal?" la tokenizacion nos devolverá ['Hola', 'Mundo', ',', 'que', 'tal', '?'].

El paso de "limpieza" nos sirve por ejemplo para eliminar palabras vacías, estas son palabras que no aportan significado y no debemos tener en cuenta para la recomendación. Algunos ejemplos de palabras vacías en inglés son 'the', 'and', 'is', etc.

## Función recomendadora 

La función que se encarga de recomendar una película, recibe como parámetro el título de alguna película y se verifica que esa película este en el dataset. Luego, si está, se crea una lista con las películas similares a la película pasada como argumento y se devuelven 5 películas similares.


### Documentación utilizada
[MovieRecommender](https://www.freecodecamp.org/news/build-a-movie-recommendation-system-with-python/#importance-of-machine-learning-in-movie-recommendations)
[pandas](https://pandas.pydata.org/docs/getting_started/index.html)
[scikit](https://scikit-learn.org/stable/user_guide.html)




