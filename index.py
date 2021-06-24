#Codigo de prototipo de asistente virtual para responder preguntas de atencion al estudiante y visitantes.

#Seccion de importacion de librerias
from time import sleep 
from flask import *
import jyserver.Flask as jsf
import os
from RedNeuronal import inferir

app = Flask(__name__)




#Seccion de funciones de para el lado del html
@jsf.use(app)
class App:
    def __init__(self):
        pass

    def consult(self):
        texto=inferir.inferencia(str(self.js.document.getElementById('texto_salida').value)) #Funcion que realiza la inferencia
        self.js.document.getElementById('textosal').value = texto #Envia el texto resultante de la inferencia a pantalla
        texto_speech = self.js.document.getElementById('textosal').value #extraer el texto resultante para ser enviado a la funcion de habla
        self.js.voz(texto_speech) #funcion donde se transforma el texto a voz y se reproduce
        animacion(self)#funcion para realizar la animacion
        


    
#funcion para reproducir la animacion
def animacion(self):
    i = 0
    image = cargararray()
    while i != 79:
        self.js.anima_foto(url_for('static', filename='img/Animacion/%s'%image[i])) #Se envia la imagen la funcion de javascript que se encargara se reproducir la animacion
        sleep(0.00125)
        i += 1

#Funcion para cargar las direcciones de imagenes a un vector
def cargararray():
    A = os.listdir('static/img/Animacion/')
    return A

#definicion de rutas de la aplicacion web
@app.route('/')
def home():
    return App.render(render_template('index.html'))#pagina principal




#Seccion de codigo que arranca el servidor python
if __name__ == '__main__':
    app.run(debug=True)