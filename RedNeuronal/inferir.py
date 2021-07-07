#instalar eso primero
#pip install nltk
#pip install tflearn
#pip install numpy

#Seccion de librerias
import tensorflow
import json
import nltk
from nltk.stem.lancaster import LancasterStemmer
import pickle
import tflearn
import random
import numpy

#Iniciando stemmer de nltk para el procesamiento del texto
stemmer = LancasterStemmer()


#Cargando archivos necesarios para la inverenvia.
with open('RedNeuonal/preguntas.json',encoding='utf-8') as conjunto:
    datos = json.load(conjunto)

with open("RedNeuronal/variable.pickle", "rb") as archivopick:
    palabras, tags, entrenamiento, salida = pickle.load(archivopick)

#Definiendo la red neuronal
red = tflearn.input_data(shape=[None,len(entrenamiento[0])])
red = tflearn.fully_connected(red,5)
red = tflearn.fully_connected(red,len(salida[0]),activation="softmax")
red = tflearn.regression(red)

#Definiendo que es una red de tipo profunda
modelo = tflearn.DNN(red)
#Carga los archivos previamente entrenados
modelo.load("RedNeuronal/modelo.tflearn")

#Funcion para el procesado y de texto e inferencia
def inferencia(texto):
    ciclo = 0
    while ciclo != 1:
        entrada = texto
        cubeta = [0 for _ in range(len(palabras))]
        entradaprocesada= nltk.word_tokenize(entrada)
        entradaprocesada = [stemmer.stem(palabra.lower()) for palabra in entradaprocesada]
        for palabraindi in entradaprocesada:
            for i, palabra in enumerate(palabras):
                if palabra == palabraindi:
                    cubeta[i] = 1
        
        resultados = modelo.predict(([numpy.array(cubeta)]))
        resultadoindi = numpy.argmax(resultados)
        tag = tags[resultadoindi]

        for tagAux in datos["preguntas"]:
            if tagAux["tag"] == tag:
                respuesta = tagAux["respuesta"]
        ciclo = 1
        respt = random.choice(respuesta)
        print("llego aqui")
        return respt
