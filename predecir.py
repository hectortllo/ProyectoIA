import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform

longitud, altura = 100, 100
modelo = './modelo/modelo.h5'
pesos = './modelo/pesos.h5'

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
	cnn = load_model(modelo)
cnn.load_weights(pesos)

def predict(file):
	x = load_img(file, target_size = (longitud, altura))
	x = img_to_array(x)
	x = np.expand_dims(x, axis=0)
	arreglo = cnn.predict(x)
	resultado = arreglo[0]
	respuesta = np.argmax(resultado)
	if respuesta == 0:
		print "Inmadura"
	elif respuesta == 1:
		print "Madura"
	elif respuesta == 2:
		print "Podrida"
	elif respuesta == 3:
		print "Proceso-maduracion"
	elif respuesta == 4:
		print "semi-madura"

predict('fresa5.jpg')
