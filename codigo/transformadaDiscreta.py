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

nMuestras=0
nFuncion=2#Hay dos funciones activas, seno y coseno
A=0
B=0
inList=[]#Valores de entrada
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
		pMessage=""
		if nFuncion==1:
			pMessage="A * SEN(B*x)"
		else:
			pMessage="A * COS(B*x)"
		os.system("cls")
		message=f"\n\n\n\n\n\n\n\n\n---Menú---\nFunción actual: {pMessage}\nA={A}; B={B}; Muestras={nMuestras}\n\nSelecciona una opción:\n\n\n"
		message=message+"A) Gráfica de Seno/Coseno de la función actual\n"
		message=message+"B) Módulo de la función actual\n"
		message=message+"C) FFT (no de la funcion, sino solo de los valores del txt)\n"
		message=message+"Y) Actualiza las muestras del .txt y cambia el valor de A y B\n"
		message=message+"Z) Seleccionar una función distinta\n"
		message=message+"S) Salir\n"
		opc=input(message).upper()#Pasamos a mayúsculas
		if(opc=="A" or opc=="B"  or opc=="C" or opc=="Y" or opc=="Z" or opc=="S"):
			correcto=True
	if correcto==True:
		return opc
def soutFFT0():#Imprimirá el módulo de la FFT de los valores dados
	xKList=[]#Lista de la gráfica de la suma del valor real con el imaginario (magnitud). En valor absoluto al ser una magnitud
	rList=[]#Lista de valores reales
	iList=[]#Lista de valores imaginarios
	counter=[]#Lista del conteo de los valores, empieza en 1
	k=0
	tam=nMuestras
	while k<tam:
		n=0#Cada que termina con una k, reiniciamos n=0
		#Sumamos cada término en parte real e imaginaria con sus valores absolutos:
		real=0
		imaginaria=0
		while n<tam:
			aux=0#Almacena el valor del cálculo
			#Calculamos para cada n el valor real e imaginario
			aux=(k*n*2*3.14159265)/tam
			real+=mt.cos(aux)*inList[n]
			imaginaria-=mt.sin(aux)*inList[n]
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
		xKList.append(aux)
		k+=1
	n=0
	aux=0
	for i in range(len(inList)):
		counter.append(aux)
		aux+=1
	#Gráficas
	fig,axes=plt.subplots(3,1)
	#Número de gráficas
	for i in range(1,4):#3 gráficas
		ax=plt.subplot(3,1,i)
		#Estilos
		ax.set_facecolor("mediumspringgreen")
		if i==1:
			plt.plot(counter,rList,'ro',label="Parte Real")
			plt.legend(loc=9)
			plt.title("Coseno (real)")
			plt.xlabel("n")
		if i==2:
			plt.plot(counter,iList,'ro',label="Parte Imaginaria")
			plt.legend(loc=9)
			plt.title("Seno (Imaginaria)")
			plt.xlabel("n")
		if i==3:
			plt.plot(counter,xKList,'c^',label="Módulo de F(k)")
			plt.legend(loc=9)
			plt.title("Magnitud FFT")
			plt.ylabel("|F(k)|")
			plt.xlabel("k")
	fig.tight_layout()
	plt.show()
def soutFFT1():#Gráfica Seno
	#Fase 1: Impresiones e inicializaciones
	print("\nFunción f(x)=A * sen(Bx)\n")
	print(f"\nDonde f(x)={A} * sen({B}x)\n")
	x=[]#Valores de la función trigonométrica
	counter=[]#Valores para X
	aux=0
	#
	#
	#Fase 2: Ahora pasamos a la parte de los cálculos
	#
	#Cálculos A) Para la gráfica trigonométrica sencilla de las muestras
	for i in range(nMuestras):
		x.append(A*mt.sin(B*inList[aux]))#Es la señal
		aux+=1
	#
	#Cálculo B) Para el módulo (Valor absoluto de la suma de real e imaginaria) e incluye las partes separadas Real e Imaginaria
	rList=[]#Lista de valores reales
	iList=[]#Lista de valores imaginarios
	rList = np.real(np.fft.fft(x))
	iList = np.imag(np.fft.fft(x))
    #LLenar contador
	aux=0
	for i in range(len(inList)):
		counter.append(aux)
		aux+=1
	#Arreglos a la primera y ultima posición (prueba) print(f"Klist:{len(xKList)} y x:{len(x)}")
	#
	#Fase 3: Gráficas
	#
	fig,axes=plt.subplots(3,1)
	#Número de gráfhhicas
	for i in range(1,4):#3 gráficas
		ax=plt.subplot(3,1,i)
		#Estilos
		ax.set_facecolor("powderblue")
		if i==1:
			#Gráfica A) de la función trigonométrica
			plt.plot(counter,x,'c^',label=f"Muestras del Seno")
			plt.legend(loc=9)
			plt.title(f"Gráfica A*sen(Bx)")
			plt.ylabel(f"{A}*sen({B}*x)")
			plt.xlabel("x")
		if i==2:
			#Gráfica B) De la parte Real
			plt.plot(counter,rList,'co',label="Parte real")
			plt.legend(loc=9)
			plt.title(f"Gráfica A*sen(Bx)")
			plt.ylabel(f"{A}*sen({B}*x)")
			plt.xlabel("x")
		if i==3:
			#Gráfica C) De la parte Imaginaria
			plt.plot(counter,iList,'co',label="Parte Imaginaria")
			plt.legend(loc=9)
			plt.title(f"Gráfica A*sen(Bx)")
			plt.ylabel(f"{A}*sen({B}*x)")
			plt.xlabel("x")
	fig.tight_layout()
	plt.show()
	#
def soutFFT2():#Gráfica Coseno
	#Fase 1: Impresiones e inicializaciones
	print("\nFunción f(x)=A * cos(Bx)\n")
	print(f"\nDonde f(x)={A} * cos({B}x)\n")
	x=[]#Valores de la función trigonométrica
	counter=[]#Valores para X
	aux=0
	#
	#
	#Fase 2: Ahora pasamos a la parte de los cálculos
	#
	#Cálculos A) Para la gráfica trigonométrica sencilla de las muestras
	for i in range(nMuestras):
		x.append(A*mt.cos(B*inList[aux]))#Es la señal
		aux+=1
	#
	#Cálculo B) Para el módulo (Valor absoluto de la suma de real e imaginaria) e incluye las partes separadas Real e Imaginaria
	rList=[]#Lista de valores reales
	iList=[]#Lista de valores imaginarios
	rList = np.real(np.fft.fft(x))
	iList = np.imag(np.fft.fft(x))
    #LLenar contador
	aux=0
	for i in range(len(inList)):
		counter.append(aux)
		aux+=1
	#Arreglos a la primera y ultima posición (prueba) print(f"Klist:{len(xKList)} y x:{len(x)}")
	#
	#Fase 3: Gráficas
	#
	fig,axes=plt.subplots(3,1)
	#Número de gráfhhicas
	for i in range(1,4):#3 gráficas
		ax=plt.subplot(3,1,i)
		#Estilos
		ax.set_facecolor("powderblue")
		if i==1:
			#Gráfica A) de la función trigonométrica
			plt.plot(counter,x,'c^',label=f"Muestras del Coseno")
			plt.legend(loc=9)
			plt.title(f"Gráfica A*cos(Bx)")
			plt.ylabel(f"{A}*cos({B}*x)")
			plt.xlabel("x")
		if i==2:
			#Gráfica B) De la parte Real
			plt.plot(counter,rList,'co',label="Parte real")
			plt.legend(loc=9)
			plt.title(f"Gráfica A*cos(Bx)")
			plt.ylabel(f"{A}*cos({B}*x)")
			plt.xlabel("x")
		if i==3:
			#Gráfica C) De la parte Imaginaria
			plt.plot(counter,iList,'co',label="Parte Imaginaria")
			plt.legend(loc=9)
			plt.title(f"Gráfica A*cos(Bx)")
			plt.ylabel(f"{A}*cos({B}*x)")
			plt.xlabel("x")
	fig.tight_layout()
	plt.show()
	#
def soutFFTMod():#Gráfica Módulo (segun OPC seno o coseno)
	#Fase 1: Impresiones e inicializaciones
	if(nFuncion==1):
		#Función seno
		print("\nFunción f(x)=A * sen(Bx)\n")
		print(f"\nDonde f(x)={A} * sen({B}x)\n")
	else:
		print("\nFunción f(x)=A * cos(Bx)\n")
		print(f"\nDonde f(x)={A} * cos({B}x)\n")
	x=[]#Valores de la función trigonométrica
	counter=[]
	aux=0
	if(nFuncion==1):
		for i in range(nMuestras):
			x.append(A*mt.sin(B*inList[aux]))
			aux+=1
	else:
		for i in range(nMuestras):
			x.append(A*mt.cos(B*inList[aux]))
			aux+=1
	#
	#Cálculo B) Para el módulo (Valor absoluto de la suma de real e imaginaria) e incluye las partes separadas Real e Imaginaria
	xKList=[]#Lista de la gráfica de la suma del valor real con el imaginario (magnitud). En valor absoluto al ser una magnitud
	xKList = np.abs(np.fft.fft(x))
	aux=0
	for i in range(len(inList)):
		counter.append(aux)
		aux+=1
	#Arreglos a la primera y ultima posición (prueba) print(f"Klist:{len(xKList)} y x:{len(x)}")
	#
	#Fase 3: Gráficas
	#
	fig,axes=plt.subplots(2,1)
	#Número de gráficas
	for i in range(1,3):#2 gráficas
		ax=plt.subplot(2,1,i)
		#Estilos
		ax.set_facecolor("powderblue")
		if i==1:
			#Gráfica A) de la función trigonométrica
			if(nFuncion==1):
				plt.plot(counter,x,'c^',label=f"Muestras del Seno")
				plt.title(f"Gráfica A*sen(Bx)")
				plt.ylabel(f"{A}*sen({B}*x)")
			else:
				plt.plot(counter,x,'c^',label=f"Muestras del Coseno")
				plt.title(f"Gráfica A*cos(Bx)")
				plt.ylabel(f"{A}*cos({B}*x)")
			plt.legend(loc=9)
			plt.xlabel("x")
		if i==2:
			#Gráfica B) De la parte Real
			plt.plot(counter,xKList,'c^',label="Módulo de F(k)")
			plt.legend(loc=9)
			if(nFuncion==1):
				plt.title(f"Gráfica A*sen(Bx). Magnitud")
			else:
				plt.title(f"Gráfica A*cos(Bx). Magnitud")
			plt.ylabel(f"|F(k)|")
			plt.xlabel("k")
	fig.tight_layout()
	plt.show()
#"Ejecución"
	#Variables
dos=2
#
#Inicializar la lista de valores
inList=[]
contador=1#Contador de valores del archivo
aux=""
with open("lista.txt") as archivo:
	for linea in archivo:
		for i in range(0, len(linea)):
			if linea[i] != " ":
				aux+=linea[i]
			else:
				contador+=1
				inList.append(float(aux))
				aux=""
#Guardamos el último valor en inList
inList.append(float(aux))
nMuestras=len(inList)
#Leemos A y B
print("\n->Bienvenid@ a la app. Función f(x)=A * cos(Bx)<-\n\n")
A=inFloat("Ingresa el valor de A: ","Debes ingresar un valor flotante")
B=inFloat("Ingresa el valor de B: ","Debes ingresar un valor flotante")
#Imprimimos lo cambiado
print(f"Numero de muestras actual: {nMuestras}\nValor de A: {A}\nValor de B: {B}\n")
#
#Ciclo
while dos==2: 
	opc=inMenu()
	if opc=="A":
		if nFuncion==1:
			soutFFT1()#Seno
		else:
			soutFFT2()#Coseno
	else:
		if opc=="B":
			soutFFTMod()
		else:
			if opc=="C":
				soutFFT0()
			else:
				if opc=="Y":
					#aux=inInt("Ingresa el valor de N donde 2^N es el número de muestras (de 1 a 12): ","Error, valor no entero")
					#while aux<1 or aux>12:
						#aux=inInt("Error. Debes ingresar un valor de 1 a 12: ","Error, valor no entero")
					#nMuestras=pow(2,aux)
					#Obtenemos el archivo de texto.
					inList=[]
					contador=1#Contador de valores del archivo
					aux=""
					with open("lista.txt") as archivo:
						for linea in archivo:
							for i in range(0, len(linea)):
								if linea[i] != " ":
									aux+=linea[i]
								else:
									contador+=1
									inList.append(float(aux))
									aux=""
					#Guardamos el último valor en inList
					inList.append(float(aux))
					#Leemos A y B
					A=inFloat("Ingresa el valor de A: ","Debes ingresar un valor flotante")
					B=inFloat("Ingresa el valor de B: ","Debes ingresar un valor flotante")
					nMuestras=len(inList)
					#Imprimimos lo cambiado
					print(f"Numero de muestras actual: {nMuestras}\nValor de A: {A}\nValor de B: {B}\n")
				else:
					if opc=="Z":
						nFuncion=inInt("Selecciona: \n1) Función Seno\n2) Función Coseno \n","Debes ingresar un valor numérico")
						while nFuncion!=1 and nFuncion!=2:
							print("Error. Debes seleccionar una opción válida\n\n")
							nFuncion=inInt("Selecciona: \n1) Función Seno\n2) Función Coseno\n","Debes ingresar un valor numérico")
					else:
						if opc=="S":
							print("Saliendo de la aplicación...")
							dos=2+2
