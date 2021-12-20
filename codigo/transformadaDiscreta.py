import os#Limpiar pantalla
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import cmath as cmth

#Objetivo: Realizar un programa que realice la transformada rápida discreta de Fourier

#O1: Este programa debe mostrar la operación de cosenos y senos (lo realizado en la V1).
#O2: Así para cualquier operación de senos y cosenos que se realice para dar la solución.
#Una vez obtenido el resultado debe mostrar su grafica
#O3: En el segundo se muestra la parte imaginaria de la función para ver como si es correcta 
#una está grafica se debe ver un lado hacia arriba y otra hacia abajo.
	#N1 Para graficar estas dos es graficar el seno y el coseno de la función que se obtenga.
#O4: En un archivo de tipo .txt debe de haber 1024 valores, los cuales el programa debe de leer, 
#ingresarlos al programa, hacer las operaciones, mostrar la función del seno y coseno y las gráficas.
#O5: De ese archivo .txt se deben tomar los valores e ingresarlos al programa para que se resuelvan y 
#se haga el proceso como con los demás, muestra operación seno y coseno y hace graficas.

nMuestras=1024
#Funciones de entrada
def inInt(message,messageError):#Valida entrada de un entero
	correcto=False
	while correcto==False:
		try:
			vInt=int(input(message))
			correcto=True
		except ValueError:
			print(messageError)
	return vInt
def inFloat(message,messageError):#Valida la entrada de un flotante
	correcto=False
	while correcto==False:
		try:
			vFloat=float(input(message))
			correcto=True
		except ValueError:
			print(messageError)
	return vFloat
def inMenu():#Muestra y valida las opciones del menu, devolviendo la opcion válida seleccionada
	correcto=False
	while correcto==False:
		'''El menú tiene:
		A) Cambiar el número de muestras 2^N (por defecto es 1024) = 2^10 con valor máximos de 12
		B) Mostrar la gráfica de la transformada rápida de Fourier (SEN)
		C) Mostrar la gráfica de la transformada rápida de Fourier (COS)
		D) Mostrar la gráfica de la transformada rápida de Fourier (ABS)
		'''
		os.system("cls")
		message="\n---Menú---\nSelecciona una opción:\n"
		message=message+f"A) Cambiar el número de muestras 2^N (por defecto es {nMuestras}) = 2^10 con valor máximo de 12\n"
		message=message+"B) Mostrar la gráfica de la FFT del módulo\n"
		message=message+"C) C\n"
		message=message+"D) D\n"
		message=message+"E) E\n"
		message=message+"F) F\n"
		message=message+"G) G\n"
		message=message+"S) Salir\n"
		opc=input(message).upper()#Pasamos a mayúsculas
		if(opc=="A" or opc=="B" or opc=="C" or opc=="D" or opc=="E" or opc=="F" or opc=="G" or opc=="S"):
			correcto=True
	if correcto==True:
		return opc
def inMuestras():#Solicita el número de muestras potencia de 2
	correcto=False
	while correcto==False:
		vMuestras=inInt("Ingresael valor de N (para 2^N): ","Solo puedes ingresar valores enteros")
		if(vMuestras<=12 and vMuestras>=1):
			correcto=True
		else:
			print("Solo puedes ingresar valores de 1 a 12")
	return vMuestras
def soutFFT0():#Imprimirá el módulo de la FFT de los valores dados
	tam = -1
	while tam<1:
		tam = inInt("Ingresa el tamaño de la señal: ","Ingresa un valor entero")
		#llenamos la lista
	inList=[]
	x=[]
	aux=0
	for i in range(tam):
		inList.append(inFloat(f"Ingresa el valor {i+1} de la señal: ","Ingresa un número"))
		x.append(aux)
		aux+=1
	#Ahora pasamos a la parte de los cálculos
	xKList=[]#Lista de la gráfica de la suma del valor real con el imaginario (magnitud). En valor absoluto al ser una magnitud
	rList=[]#Lista de valores reales
	iList=[]#Lista de valores imaginarios
	k=0
	while k<tam:
		print(f"\nk={k}\n")
		n=0#Cada que termina con una k, reiniciamos n=0
		#Sumamos cada término en parte real e imaginaria con sus valores absolutos:
		real=0
		imaginaria=0
		while n<tam:
			print(f"\tn={n}\n");
			aux=0#Almacena el valor del cálculo
			#Calculamos para cada n el valor real e imaginario
			aux=(k*n*2*3.14159265)/tam
			real+=mt.cos(aux)*inList[n]
			imaginaria+=mt.sin(aux)*inList[n]
			#Redondeo
			imaginaria=round(imaginaria,5)
			real=round(real,5)
			print(f"\t\t->aux={aux}\n")
			print(f"\t\t->in[{n}]={inList[n]}\n")
			print(f"\t\t->cos({aux})={mt.cos(aux)}\n")
			print(f"\t\t->sin({aux})={mt.sin(aux)}\n")
			print(f"\t\t->Real(acumulada)={real}\n")
			print(f"\t\t->Imaginaria(acumulada)={imaginaria}\n")
			n+=1
		#Pasamos a cada vector los valores
		rList.append(real)
		iList.append(imaginaria)
			#Pasando al vector de la magnitud
		absR=0
		absI=0
		if(rList[k]<0):
			absR-=rList[k]
		else:
			absR+=rList[k]

		if(iList[k]<0):
			absI-=iList[k]
		else:
			absI+=iList[k]
		aux=absR+absI
		xKList.append(aux)
		print(f"\n{k}) Parte real: {real}\nParte imaginaria: {imaginaria}\n\n\n")
		k+=1
	n=0
	while n<tam:
		print(f"\t\t->Posición F[{n}]: {xKList[n]}\n")
		print(f"\t\t->Posición número {n} del vector X: {x[n]}\n")
		n+=1
	#Gráfica de la entrada
	plt.plot(x,inList,'ro',label="Señal de entrada F[m]")
	plt.legend(loc=9)
	plt.title("Señal F[m]")
	plt.ylabel("F[m]")
	plt.xlabel("m")
	plt.show()
	#Gráfica 1, del módulo o magnitud
	plt.plot(x,xKList,'c^',label="Módulo de F(k)")
	plt.legend(loc=9)
	plt.title("Magnitud FFT")
	plt.ylabel("|F(k)|")
	plt.xlabel("k")
	plt.show()
def soutFFT1():#Imprimirá el módulo de la FFT de una señal introducida
	print("\nFunción f(x)=A cos(Bx)\n")
	inList=[]
	x=[]
	aux=0
	#Llenamos el vector con las muestras N veces (con el valor de nMuestras)
	for i in range(nMuestras):
		inList.append(aux)
		x.append(aux)
		aux+=1
	#Ahora pasamos a la parte de los cálculos
	xKList=[]#Lista de la gráfica de la suma del valor real con el imaginario (magnitud). En valor absoluto al ser una magnitud
	rList=[]#Lista de valores reales
	iList=[]#Lista de valores imaginarios
	k=0
	while k<nMuestras:
		n=0#Cada que termina con una k, reiniciamos n=0
		#Sumamos cada término en parte real e imaginaria con sus valores absolutos:
		real=0
		imaginaria=0
		while n<nMuestras:
			aux=0#Almacena el valor del cálculo
			#Calculamos para cada n el valor real e imaginario
			aux=(k*n*2*3.14159265)/nMuestras
			real+=mt.cos(aux)*inList[n]
			imaginaria+=mt.sin(aux)*inList[n]
			#Redondeo
			imaginaria=round(imaginaria,5)
			real=round(real,5)
			n+=1
		#Pasamos a cada vector los valores
		rList.append(real)
		iList.append(imaginaria)
			#Pasando al vector de la magnitud
		absR=0
		absI=0
		if(rList[k]<0):
			absR-=rList[k]
		else:
			absR+=rList[k]
		if(iList[k]<0):
			absI-=iList[k]
		else:
			absI+=iList[k]
		aux=absR+absI
		if(k==0 or k==nMuestras-1):
			xKList.append(0)
		else:
			xKList.append(aux)
		k+=1
	n=0
	#Arreglos a la primera y ultima posición
	print(f"Klist:{len(xKList)} y x:{len(x)}")

	
	#Gráfica de la entrada
	plt.plot(x,inList,'ro',label="Señal de entrada F[m]")
	plt.legend(loc=9)
	plt.title("Señal F[m]")
	plt.ylabel("F[m]")
	plt.xlabel("m")
	plt.show()
	#Gráfica 1, del módulo o magnitud
	plt.plot(x,xKList,'c^',label="Módulo de F(k)")
	plt.legend(loc=9)
	plt.title("Magnitud FFT")
	plt.ylabel("|F(k)|")
	plt.xlabel("k")
	plt.show()
def soutFFT2():#Imprimirá el módulo de la FFT de los 1024 valores
	print("\nFunción f(x)=A cos(Bx)\n")
	inList=[]
	x=[]
	aux=0
	#Llenamos el vector con las muestras N veces (con el valor de nMuestras)
	for i in range(nMuestras):
		inList.append(aux)
		aux+=1
	#Leemos los argumentos A y B
	A=0
	B=0
	A=inFloat("Ingresa el valor de A: ","Debes ingresar un valor flotante")
	B=inFloat("Ingresa el valor de B: ","Debes ingresar un valor flotante")
	#Ahora pasamos a la parte de los cálculos, primero mostrando la gráfica con las muestras
	aux=0
	for i in range(nMuestras):
		x.append(A*mt.cos(B*inList[aux]))
		aux+=1
	#Funcion de gráficas
	#Gráfica 2 de Coseno
	plt.plot(inList,x,'co',label="Muestras del Coseno")
	plt.legend(loc=9)
	plt.title(f"Coseno")
	plt.ylabel("{A}*cos({B}*x)")
	plt.xlabel("x")
	plt.show()
	#EODef
def soutFFT3():#Imprimirá el módulo de la FFT de los 1024 valores
	print("\nFunción f(x)=A cos(Bx)\n")
	inList=[]
	x=[]
	aux=0
	#Llenamos el vector con las muestras N veces (con el valor de nMuestras)
	for i in range(nMuestras):
		inList.append(aux)
		aux+=1
	#Leemos los argumentos A y B
	A=0
	B=0
	A=inFloat("Ingresa el valor de A: ","Debes ingresar un valor flotante")
	B=inFloat("Ingresa el valor de B: ","Debes ingresar un valor flotante")
	#Ahora pasamos a la parte de los cálculos, primero mostrando la gráfica con las muestras
	aux=0
	for i in range(nMuestras):
		x.append(A*mt.cos(B*inList[aux]))
		aux+=1
	#Funcion de gráficas
	#Gráfica 2 de Coseno
	plt.plot(inList,x,'co',label="Muestras del Coseno")
	plt.legend(loc=9)
	plt.title(f"Coseno")
	plt.ylabel("{A}*cos({B}*x)")
	plt.xlabel("x")
	plt.show()
	#EODef


#"Ejecución"
	#Variables
potN=10#Para las 1024 muestras
dos=2
#Ciclo
while dos==2: 
	opc=inMenu()
	if opc=="A":
		aux=inInt("Ingresa el valor de N donde 2^N es el número de muestras (de 1 a 12): ","Error, valor no entero")
		while aux<1 or aux>12:
			aux=inInt("Error. Debes ingresar un valor de 1 a 12: ","Error, valor no entero")
		nMuestras=pow(2,aux)
		print(f"Numero de muestras actual: {nMuestras}")
	else:
		if opc=="B":
			soutFFT1()
		else:
			if opc=="C":
				soutFFT2()
			else: 
				if opc=="D":
					soutFFT3()
				else: 
					if opc=="E":
						soutFFT4()
					else:
						if opc=="F":
							soutFFT5()
						else:
							if opc=="G":
								soutFFT6()
							else:
								if opc=="S":
									print("Saliendo de la aplicación")
									dos=2+2

"""
#Ejecución
"""