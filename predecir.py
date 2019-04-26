import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform
from tkinter import *
from tkinter import filedialog
from PIL import  Image

"""
	Clase para predecir si la imagen que ingresa el usuario
	es una fresa o no.
	En caso de ser una fresa lo que hace es medir su grado de maduración
	De lo contrario mostrara un mensaje diciendo que no es una fresa.
"""
class RNA(object):
	"""docstring for RNA"""
	def __init__(self):
		self.longitud, self.altura = 100, 100
		self.modelo_red1 = './modelo/red1/modelo.h5'
		self.pesos_red1 = './modelo/red1/pesos.h5'

		self.modelo_red2 = './modelo/modelo.h5'
		self.pesos_red2 = './modelo/modelo.h5'

		with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
			self.cnn = load_model(self.modelo_red1)
		self.cnn.load_weights(self.pesos_red1)

		with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
			self.cnn2 = load_model(self.modelo_red2)
		self.cnn2.load_weights(self.pesos_red2)

	def predict_red2(self,file):
		x = load_img(file, target_size = (self.longitud, self.altura))
		x = img_to_array(x)
		x = np.expand_dims(x, axis=0)
		arreglo = self.cnn2.predict(x)
		resultado = arreglo[0]
		respuesta = np.argmax(resultado)
		if respuesta == 0:
			return "Inmadura"
		elif respuesta == 1:
			return "Madura"
		elif respuesta == 2:
			return "Podrida"
		elif respuesta == 3:
			return "Proceso-maduracion"
		elif respuesta == 4:
			return "Semi-madura"

	def predict_red1(self,file):
		x = load_img(file, target_size = (self.longitud, self.altura))
		x = img_to_array(x)

		x = np.expand_dims(x, axis=0)
		arreglo = self.cnn.predict(x)
		resultado = arreglo[0]
		respuesta = np.argmax(resultado)
		if respuesta == 0:
			return"Esto es un Banano, no una fresa"
		elif respuesta == 1:
			return"Esto es un Coco, no una fresa"
		elif respuesta == 2:
			return"Esto es una Naranja, no una fresa"
		elif respuesta == 3:
			return "Es una fresa con grado de maduracion: " + self.predict_red2(file)



class GUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        w,h = 650, 650
        master.minsize(width=w, height=h)
        master.maxsize(width=w, height=h)
        self.rna=RNA()
        self.pack()
        self.maduracion=StringVar()
        self.file = Button(self, text='Seleccionar imagen', command=self.buscarImg)
        self.choose = Label(self, text="IA Proyecto").pack()
        self.image = PhotoImage(file='url.png')
        self.label = Label(image=self.image)
        self.label1 = Label(textvariable=self.maduracion)
        self.file.pack()
        self.label.pack()
        self.label1.pack()

    def buscarImg(self):
        filename =  filedialog.askopenfilename(title = "Seleccione una imagen",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        img = Image.open(filename)
        img.resize((300,300),Image.ANTIALIAS).save("f.png")
        self.img=PhotoImage(file="f.png")
        self.label.configure(image=self.img)
        self.label.image=self.img
        self.maduracion.set(self.rna.predict_red1(filename))


root = Tk()
app = GUI(master=root)
app.mainloop()
