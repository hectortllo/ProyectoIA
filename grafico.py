#Librerías a utilizar.
from tkinter import *
from tkinter import filedialog
from PIL import Image
import os

#Creacion de la ventana.
root=Tk()
#creo un frame para mayor comodidad y lo empaqueto
miFrame=Frame(root,width=700,height=400)
miFrame.pack()
#Codigo a ejecutar en el evento del boton
def codigoBoton():
	#Abro un File chooser para obtener nada mas la ruta del archivo seleccionado
	filename =  filedialog.askopenfilename(initialdir = "/home",title = "Seleccione una imagen",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	#Con la libreria PIL e importando Image abro la imagen para hacer lo siguiente
	im = Image.open(filename)
	"""
		Le doy un nuevo tamanio que en mi caso es de 300*300 y lo guardo en formato png para poder
		mostrar la imagen en el label
	"""
	im.resize((300,300), Image.ANTIALIAS).save("f.png")
	im=PhotoImage(file="f.png")
	miLabel = Label(miFrame,image=im).place(x=0,y=30).update(miLabel)

btnSeleccionar=Button(miFrame,text="Seleccionar imagen",command=codigoBoton).place(x=0,y=0)
root.mainloop()


if os.path.exists("f.png"):
	os.remove("f.png")
