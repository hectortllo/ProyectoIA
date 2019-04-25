import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform

archivo = 'fresa4.jpg'
longitud, altura = 100, 100
modelo_red1 = './modelo/red1/modelo.h5'
pesos_red1 = './modelo/red1/pesos.h5'

modelo_red2 = './modelo/red2/modelo.h5'
pesos_red2 = './modelo/red2/modelo.h5'

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
	cnn = load_model(modelo_red1)
cnn.load_weights(pesos_red1)

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
	cnn2 = load_model(modelo_red2)
cnn2.load_weights(pesos_red2)

def predict_red1(file):
	x = load_img(file, target_size = (longitud, altura))
	x = img_to_array(x)

	x = np.expand_dims(x, axis=0)
	arreglo = cnn.predict(x)
	resultado = arreglo[0]
	respuesta = np.argmax(resultado)
	if respuesta == 0:
		print("Banano")
	elif respuesta == 1:
		print("Coco")
	elif respuesta == 2:
		print("Naranja")
	elif respuesta == 3:
		print("Fresa")
		predict_red2(archivo)

def predict_red2(file):
	x = load_img(file, target_size = (longitud, altura))
	x = img_to_array(x)

	x = np.expand_dims(x, axis=0)
	arreglo = cnn2.predict(x)
	resultado = arreglo[0]
	respuesta = np.argmax(resultado)
	if respuesta == 0:
		print("Inmadura")
	elif respuesta == 1:
		print("Madura")
	elif respuesta == 2:
		print("Podrida")
	elif respuesta == 3:
		print("Proceso-maduracion")
	elif respuesta == 4:
		print("Semi-madura")

predict_red1(archivo)
