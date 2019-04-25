import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as k

k.clear_session()

data_entrenamiento_red2 = './data/red2/entrenamiento'
data_validacion_red2 = './data/red2/validacion'

epocas = 20
altura, longitud = 100, 100
batch_size = 32 #numero de imagenes a procesar en cada iteracion
pasos = 1000
pasos_validacion = 200
filtrosConv1 = 32
filtrosConv2 = 64
tamanio_filtro1 = (3,3)
tamanio_filtro2 = (2,2)
tamanio_pool = (2,2)
clases = 5 #numero de frutas existentes
lr = 0.0005 #constante de aprendizaje

#Pre-procesamiento de imagenes
entrenamiento_datagen = ImageDataGenerator(
	rescale = 1./255,
	shear_range = 0.3,
	zoom_range = 0.3,
	horizontal_flip = True
)

validacion_datagen = ImageDataGenerator(
	rescale = 1./255
)

imagen_entrenamiento_red2 = entrenamiento_datagen.flow_from_directory(
	data_entrenamiento_red2,
	target_size = (altura, longitud),
	batch_size = batch_size,
	class_mode = 'categorical'
)

imagen_validacion_red2 = validacion_datagen.flow_from_directory(
	data_validacion_red2,
	target_size = (altura, longitud),
	batch_size = batch_size,
	class_mode = 'categorical'
)

def entrenamiento_red2():
	cnn = Sequential()
	cnn.add(Convolution2D(filtrosConv1, tamanio_filtro1, padding='same', input_shape=(altura, longitud, 3), activation='relu'))
	cnn.add(MaxPooling2D(pool_size=tamanio_pool))
	cnn.add(Convolution2D(filtrosConv2, tamanio_filtro2, padding='same', activation='relu'))
	cnn.add(MaxPooling2D(pool_size=tamanio_pool))
	cnn.add(Flatten())
	cnn.add(Dense(256,activation='relu'))
	cnn.add(Dropout(0.5))
	cnn.add(Dense(clases, activation='softmax'))
	cnn.compile(loss='categorical_crossentropy', optimizer=optimizers.Adam(lr=lr), metrics=['accuracy'])

	cnn.fit_generator(imagen_entrenamiento_red2, steps_per_epoch=pasos, epochs=epocas, validation_data=imagen_validacion_red2, validation_steps=pasos_validacion)
	dir='./modelo/red2/'

	if not os.path.exists(dir):
		os.mkdir(dir)
	cnn.save('./modelo/red2/modelo.h5')
	cnn.save_weights('./modelo/red2/pesos.h5')

entrenamiento_red2()