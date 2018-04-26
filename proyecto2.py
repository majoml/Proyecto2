from tkinter import *
import time

class Automata_impar(object):
	"""docstring for ClassName"""
  
	def __init__(self, palabra, etiqueta, q1, q2, q3):
		self.palabra = palabra
		self.pila = []
		self.etiqueta=etiqueta
		self.q1=q1
		self.q2=q2
		self.q3=q3
		self.f = open('archivo.txt', "w")
		self.estado_0()
        
	def estado_0(self):
		self.q1["text"] = "P"
		self.f.write("************************ ")
		self.f.write(self.palabra)
		self.f.write(" (IMPAR) ************************************************")
		self.f.write("\n")

		self.f.write("Estado P")
		self.f.write("\n")

		veces = self.palabra.count("c")
		if "c" in self.palabra and veces == 1:

			cont = 0
			posi_c = self.palabra.index("c")
			print(self.pila)
			
			self.f.write(str(self.pila))
			self.f.write("\n")
			while cont < posi_c: 

				if self.palabra[cont] == "b":

					
					if not self.pila:
						
						self.pila.append("#")
						self.pila.append("b")
						print(self.pila)
						self.f.write(str(self.pila))
						self.f.write("\n")
						
					else:
						
						letra = self.pila.pop()
						print(self.pila)
						self.f.write(str(self.pila))
						self.f.write("\n")
						if letra == "b":
							
							self.pila.append("b")
							self.pila.append("b")
							print(self.pila)
							self.f.write(str(self.pila))
							self.f.write("\n")
						if letra == "a":
							
							self.pila.append("a")
							self.pila.append("b")
							print(self.pila)
							self.f.write(str(self.pila))
							self.f.write("\n")
				if self.palabra[cont] == "a":
					
					if not self.pila:
						self.pila.append("#")
						self.pila.append("a")
						print(self.pila)
						self.f.write(str(self.pila))
						self.f.write("\n")
					else:
						letra = self.pila.pop()
						print(self.pila)
						self.f.write(str(self.pila))
						self.f.write("\n")
						if letra == "b":
							self.pila.append("b")
							self.pila.append("a")
							print(self.pila)
							self.f.write(str(self.pila))
							self.f.write("\n")
						if letra == "a":
							self.pila.append("a")
							self.pila.append("a")
							print(self.pila)
							self.f.write(str(self.pila))
							self.f.write("\n")
				cont = cont + 1
			if cont == posi_c:
				letra = self.pila.pop()
				self.f.write(str(self.pila))
				self.f.write("\n")
				print(self.pila)
				if letra == "#":
					self.pila.append("#")
					print(self.pila)
					self.f.write(str(self.pila))
					self.f.write("\n")
				if letra == "a":
					self.pila.append("a")
					print(self.pila)
					self.f.write(str(self.pila))
					self.f.write("\n")
				if letra == "b":
					self.pila.append("b")
					print(self.pila)
					self.f.write(str(self.pila))
					self.f.write("\n")
				print("Estado Q")
				self.f.write("Estado Q")
				self.f.write("\n")
				self.estado_1()

		else:
			print("La palabra no es palindromo")
			self.f.write("La palabra no es palindromo")
			self.f.write("\n")
			self.f.close()
	def estado_1(self):
		self.q2["text"] = "Q"
		posi_c = self.palabra.index("c")
		cont_1 = posi_c + 1
		cont_pi=len(self.pila)-1
		while cont_1 > posi_c and cont_1 < len(self.palabra):
			if self.palabra[cont_1] == self.pila[cont_pi]:
				self.pila.pop()
				print(self.pila)
				self.f.write(str(self.pila))
				self.f.write("\n")
				cont_pi=cont_pi-1
				cont_1=cont_1+1
			else:
				print("La palabra no es palindromo")
				self.f.write("La palabra no es palindromo")
				self.f.write("\n")
				break
		self.f.write("Estado R")
		self.f.write("\n")
		self.estado_acep()
		

	def estado_acep(self):
		self.q3["text"] = "R"
		letra=self.pila.pop()
		
		if letra == "#":
			self.f.write(str(self.pila))
			self.f.write("\n")
			self.pila.append("#")
			self.f.write(str(self.pila))
			self.f.write("\n")
			print("Cadena aceptada")
			self.f.write("CADENA ACEPTADA")
			self.f.write("\n")
		else:
			print("Cadena no Aceptada")
			self.f.write("CADENA NO ACEPTADA")
			self.f.write("\n")
		self.f.write("=============================================")
		self.f.write("=============================================")
		self.f.write("\n")
		self.f.close()

class Automata_par(object):
	"""docstring for ClassName"""
  
	def __init__(self, palabra, etiqueta, q1, q2, q3):
		self.palabra = palabra
		self.pila = []
		self.etiqueta=etiqueta
		self.q1=q1
		self.q2=q2
		self.q3=q3
		self.f = open('archivo.txt', "w")
		self.estado_0()
        
	def estado_0(self):
		self.q1["text"] = "P"
		self.f.write("************************ ")
		self.f.write(self.palabra)
		self.f.write(" (PAR) ************************************************")
		self.f.write("\n")
		self.f.write("Estado P")
		self.f.write("\n")

		if "a" in self.palabra or "b" in self.palabra:
			centro=int(len(self.palabra)/2)
			cont=0
			print(self.pila)
			self.f.write(str(self.pila))
			self.f.write("\n")
			while cont < centro: 
				if "a" in self.palabra[cont] or "b" in self.palabra[cont]:
					if self.palabra[cont] == "b":
						if not self.pila:
							
							self.pila.append("#")
							self.pila.append("b")
							print(self.pila)
							self.f.write(str(self.pila))
							self.f.write("\n")
							
						else:
							
							letra = self.pila.pop()
							print(self.pila)
							self.f.write(str(self.pila))
							self.f.write("\n")
							if letra == "b":
								
								self.pila.append("b")
								self.pila.append("b")
								print(self.pila)
								self.f.write(str(self.pila))
								self.f.write("\n")
							if letra == "a":
								
								self.pila.append("a")
								self.pila.append("b")
								print(self.pila)
								self.f.write(str(self.pila))
								self.f.write("\n")
					if self.palabra[cont] == "a":
						
						if not self.pila:
							self.pila.append("#")
							self.pila.append("a")
							print(self.pila)
							self.f.write(str(self.pila))
							self.f.write("\n")
						else:
							letra = self.pila.pop()
							print(self.pila)
							self.f.write(str(self.pila))
							self.f.write("\n")
							if letra == "b":
								self.pila.append("b")
								self.pila.append("a")
								print(self.pila)
								self.f.write(str(self.pila))
								self.f.write("\n")
							if letra == "a":
								self.pila.append("a")
								self.pila.append("a")
								print(self.pila)
								self.f.write(str(self.pila))
								self.f.write("\n")
					cont = cont + 1
				else:
					print("Letra no aceptada en el automata par")
					self.f.write("Letra no aceptada en el automata par")
					self.f.write("\n")
					self.f.close()
					break
			if cont == centro:
				letra = self.pila.pop()
				if letra == "b":
					print(self.pila)
					self.f.write(str(self.pila))
					self.f.write("\n")
				if letra == "a":
					print(self.pila)
					self.f.write(str(self.pila))
					self.f.write("\n")
				print("Estado Q")
				self.f.write("Estado Q")
				self.f.write("\n")
				self.estado_1()

		else:
			print("Letra no aceptada en el automata par")
			self.f.write("Letra no aceptada en el automata par")
			self.f.write("\n")
			self.f.close()
	def estado_1(self):
		self.q2["text"] = "Q"
		centro=int(len(self.palabra)/2)
		cont_1 = centro + 1
		cont_pi=len(self.pila)-1
		while cont_1 > centro and cont_1 < len(self.palabra):
			if self.palabra[cont_1] == self.pila[cont_pi]:
				self.pila.pop()
				print(self.pila)
				self.f.write(str(self.pila))
				self.f.write("\n")
				cont_pi=cont_pi-1
				cont_1=cont_1+1
			else:
				print("La palabra no es palindromo")
				self.f.write("La palabra no es palindromo")
				self.f.write("\n")
				break
				#self.f.close()
				
		self.f.write("Estado R")
		self.f.write("\n")
		self.estado_acep()
		

	def estado_acep(self):
		self.q3["text"] = "R"
		letra=self.pila.pop()
		
		if letra == "#":
			self.f.write(str(self.pila))
			self.f.write("\n")
			self.pila.append("#")
			self.f.write(str(self.pila))
			self.f.write("\n")
			print("Cadena Aceptada")
			self.f.write("CADENA ACEPTADA")
			self.f.write("\n")
		else:
			print("Cadena no Aceptada")
			self.f.write("CADENA NO ACEPTADA")
			self.f.write("\n")
		self.f.write("=============================================")
		self.f.write("=============================================")
		self.f.write("\n")
		self.f.close()