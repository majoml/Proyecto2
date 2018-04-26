from tkinter import *
from tkinter import font
from proyecto2 import *
import os
root = Tk()


palabra = StringVar()
root.title('canvas')
canvas = Canvas(width=990, height=540, bg='white')
canvas.pack(expand=YES, fill=BOTH)
color='#DCDCDC'
Helvfont = font.Font(family="Helvetica", size=22, weight="bold")
etiq = Listbox(canvas, width=50, selectforeground="#ffffff",selectbackground="#00aa00",selectborderwidth=5)
etiq.place(x=70, y=230)
Helvfont_q= font.Font(family="Helvetica", size=10, weight="bold")
q1= Label(text="", width=2, height=1, fg="blue", bg="white", font=Helvfont_q)
q1.place(x=619, y=265)
q2= Label(text="", width=2, height=1, fg="blue", bg="white", font=Helvfont_q)
q2.place(x=769, y=265)
q3= Label(text="", width=2, height=1, fg="blue", bg="white", font=Helvfont_q)
q3.place(x=919, y=265)


def validar():
	
	if (len(palabra.get()) % 2) == 0:
		print("PAR")
		proyecto2 = Automata_par(palabra.get(), etiq, q1, q2, q3)
		par_grafica()
		imprimir()
	else:
		print("IMPAR")
		proyecto2 = Automata_impar(palabra.get(), etiq, q1, q2, q3)
		impar_grafica()
		imprimir()
		


def par_grafica():
	color="white"
	circulo_1=canvas.create_oval(650, 260, 600, 210, width=3, fill=color)
	circulo_2=canvas.create_oval(750, 260, 800, 210, width=3, fill=color, tags="r2")
	circulo_3=canvas.create_oval(900, 260, 950, 210, width=3, fill="blue", tags="r1")
	circulo_4=canvas.create_oval(910, 250, 940, 220, width=3, fill=color, tags="r1")
	arco_1=canvas.create_arc(605, 300, 635, 260, width=2,fill="black")
	linea_1=canvas.create_line(800, 240, 900, 240, width=3, fill="black", arrow="last", tags="to_r1")
	linea_2=canvas.create_line(650, 240, 750, 240, width=3, fill="black", arrow="last", tags="to_r2")
	Helvfont = font.Font(family="Helvetica", size=22, weight="bold")
	etiqueta = Label(text="AUTOMATA PAR", width=20, fg="green", bg="white", font=Helvfont)
	etiqueta.place(x=600, y=20)
	Helvfont_1 = font.Font(family="Helvetica", size=8, weight="bold")
	etiqueta = Label(text="b, b/ bb\na, b/ ba\nb, a/ ab\na, a/ aa\nb, #/ #b\na, #/ #a", width=8, fg="black", bg="white", font=Helvfont_1)
	etiqueta.place(x=600, y=80)
	etiqueta = Label(text="b, b/ λ\na, a/ λ", width=8,height=3, fg="black", bg="white", font=Helvfont_1)
	etiqueta.place(x=670, y=180)
	etiqueta = Label(text="b, b/ λ\na, a/ λ", width=8, fg="black", bg="white", font=Helvfont_1)
	etiqueta.place(x=750, y=130)
	etiqueta = Label(text="λ, #/ #", width=8, fg="black", bg="white", font=Helvfont_1)
	etiqueta.place(x=820, y=200)
	
def impar_grafica():
	color="white"
	circulo_1=canvas.create_oval(650, 260, 600, 210, width=3, fill=color)
	circulo_2=canvas.create_oval(750, 260, 800, 210, width=3, fill=color, tags="r2")
	circulo_3=canvas.create_oval(900, 260, 950, 210, width=3, fill="blue", tags="r1")
	circulo_4=canvas.create_oval(910, 250, 940, 220, width=3, fill=color, tags="r1")
	linea_1=canvas.create_line(800, 240, 900, 240, width=3, fill="black", arrow="last", tags="to_r1")
	linea_2=canvas.create_line(650, 240, 750, 240, width=3, fill="black", arrow="last", tags="to_r2")
	Helvfont = font.Font(family="Helvetica", size=22, weight="bold")
	etiqueta_t= Label(text="AUTOMATA IMPAR", width=20, fg="green", bg="white", font=Helvfont)
	etiqueta_t.place(x=600, y=20)
	Helvfont_1 = font.Font(family="Helvetica", size=8, weight="bold")
	etiqueta = Label(text="b, b/ bb\na, b/ ba\nb, a/ ab\na, a/ aa\nb, #/ #b\na, #/ #a", width=8, fg="black", bg="white", font=Helvfont_1)
	etiqueta.place(x=600, y=80)
	etiqueta = Label(text="c, #/ #\nc, b/ b\nc, a/ a", width=8, fg="black", bg="white", font=Helvfont_1)
	etiqueta.place(x=670, y=180)
	etiqueta = Label(text="b, b/ λ\na, a/ λ", width=8, fg="black", bg="white", font=Helvfont_1)
	etiqueta.place(x=750, y=130)
	etiqueta = Label(text="λ, #/ #", width=8, fg="black", bg="white", font=Helvfont_1)
	etiqueta.place(x=820, y=200)
		
def imprimir():
	archivo = open("archivo.txt","r") 
	i=0
	for linea in archivo.readlines():
		etiq.insert(i,linea)
		i=i+1
	archivo.close()   
	os.remove("archivo.txt")
	

etiqueta_1 = Label(text="INGRESE LA PALABRA", width=25, fg="black", bg="white", font=Helvfont)
etiqueta_1.place(x=80, y=20)
entrada= Entry(canvas, textvariable=palabra).place(x=190, y=80)

botom=Button(canvas,text="VALIDAR", command=validar).place(x=240, y=120)



root.mainloop()
