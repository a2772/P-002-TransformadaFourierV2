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
		message=message+"A) Gráfica de Seno\n"
		message=message+"B) Gráfica de Coseno\n"
		message=message+"Y) Actualiza las muestras del .txt y cambia el valor de A y B\n"
		message=message+"Z) Seleccionar una función distinta\n"
		message=message+"S) Salir\n"
		opc=input(message).upper()#Pasamos a mayúsculas
		if(opc=="A" or opc=="B" or opc=="Y" or opc=="Z" or opc=="S"):
			correcto=True
	if correcto==True:
		return opc
def inMuestras():#Solicita el número de muestras potencia de 2
	correcto=False
	while correcto==False:
		vMuestras=inInt("Ingresa el valor de N (para 2^N): ","Solo puedes ingresar valores enteros")
		if(vMuestras<=12 and vMuestras>=1):
			correcto=True
		else:
			print("Solo puedes ingresar valores de 1 a 12")
	return vMuestras
def realFT(y,n,isign):
		n2=n+2;wi=0.0;wr=1.0;
		theta=3.14159265358979/n
		wtemp=mt.sin(0.5*theta)
		wpr = -2.0*wtemp*wtemp
		wpi=mt.sin(theta)
		y[1]=0.0;
		j=2
		while j<=((n>>1)+1):
			wr=(wtemp)*wpr-wi*wpi+wr;
			wi=wi*wpr+wtemp*wpi+wi;
			y1=wi*(y[j]+y[n2-j]);
			y2=0.5*(y[j]-y[n2-j]);
			y[j]=y1+y2;
			y[n2-j]=y1-y2;		
			j+=1
		realFT(y,n,1)
		y[1]*=0.5;
		suma=y[2]=0.0;
		j=1
		while j<=(n-1):
			suma += y[j];
			y[j]=y[j+1];
			y[j+1]=suma;
			j+=2
def sinFT(y,n):
	realFT(y,n,1)
def soutFFT2():#Gráfica Coseno
	#Fase 1: Impresiones e inicializaciones
	print("\nFunción f(x)=A * cos(Bx)\n")
	print(f"\nDonde f(x)={A} * cos({B}x)\n")
	x=[]#Valores de la función trigonométrica
	aux=0
	#
	#
	#Fase 2: Ahora pasamos a la parte de los cálculos
	#
	#Cálculos A) Para la gráfica trigonométrica sencilla de las muestras
	for i in range(nMuestras):
		x.append(A*mt.cos(B*inList[aux]))
		aux+=1
	#
	#Cálculo B) Para el módulo (Valor absoluto de la suma de real e imaginaria) e incluye las partes separadas Real e Imaginaria
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
			aux=((A*mt.cos(B*k*n))*2*3.14159265)/nMuestras
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
	#Arreglos a la primera y ultima posición (prueba) print(f"Klist:{len(xKList)} y x:{len(x)}")
	#
	#Fase 3: Gráficas
	#
	x=inList
	sinFT(x,len(x))
	#Gráfica A) de la función trigonométrica
	plt.plot(inList,x,'c^',label=f"Muestras del Coseno")
	plt.legend(loc=9)
	plt.title(f"Gráfica A*cos(Bx)")
	plt.ylabel(f"{A}*cos({B}*x)")
	plt.xlabel("x")
	plt.show()
	#
	#Gráfica B) De la parte Real
	#
	plt.plot(inList,rList,'co',label="Parte real")
	plt.legend(loc=9)
	plt.title(f"Gráfica A*cos(Bx)")
	plt.ylabel(f"{A}*cos({B}*x)")
	plt.xlabel("x")
	plt.show()
	#
	#Gráfica C) De la parte Imaginaria
	#
	plt.plot(inList,iList,'co',label="Parte Imaginaria")
	plt.legend(loc=9)
	plt.title(f"Gráfica A*cos(Bx)")
	plt.ylabel(f"{A}*cos({B}*x)")
	plt.xlabel("x")
	plt.show()
	#
	#Gráfica D) Del módulo
	#
	plt.plot(inList,xKList,'c^',label="Módulo de F(k)")
	plt.legend(loc=9)
	plt.title(f"Gráfica A*cos(Bx). Magnitud")
	plt.ylabel(f"|F(k)|")
	plt.xlabel("k")
	plt.show()

#"Ejecución"
	#Variables
potN=10#Para las 1024 muestras
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
				inList.append(int(aux))
				aux=""
#Guardamos el último valor en inList
inList.append(int(aux))
nMuestras=len(inList)
#
#Ciclo
while dos==2: 
	opc=inMenu()
	if opc=="A":
		soutFFT2()
	else:
		if opc=="B":
			y=inList
			sinFT(y,len(y)-2)
			#Gráfica A) de la función trigonométrica
			plt.plot(inList,y,'c^',label=f"Muestras del Coseno")
			plt.legend(loc=9)
			plt.title(f"Gráfica A*cos(Bx)")
			plt.ylabel(f"{A}*cos({B}*x)")
			plt.xlabel("x")
			plt.show()
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
								inList.append(int(aux))
								aux=""
				#Guardamos el último valor en inList
				inList.append(int(aux))
				#Leemos A y B
				A=inFloat("Ingresa el valor de A: ","Debes ingresar un valor flotante")
				B=inFloat("Ingresa el valor de B: ","Debes ingresar un valor flotante")
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

#Ejecución











'''
def soutFFT2():#Gráfica Coseno
	#Fase 1: Impresiones e inicializaciones
	print("\nFunción f(x)=A * cos(Bx)\n")
	print(f"\nDonde f(x)={A} * cos({B}x)\n")
	x=[]#Valores de la función trigonométrica
	aux=0
	#
	#
	#Fase 2: Ahora pasamos a la parte de los cálculos
	#
	#Cálculos A) Para la gráfica trigonométrica sencilla de las muestras
	for i in range(nMuestras):
		x.append(A*mt.cos(B*inList[aux]))
		aux+=1
	#
	#Cálculo B) Para el módulo (Valor absoluto de la suma de real e imaginaria) e incluye las partes separadas Real e Imaginaria
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
			aux=((A*mt.cos(B*k*n))*2*3.14159265)/nMuestras
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
	#Arreglos a la primera y ultima posición (prueba) print(f"Klist:{len(xKList)} y x:{len(x)}")
	#
	#Fase 3: Gráficas
	#
	#Gráfica A) de la función trigonométrica
	plt.plot(inList,x,'c^',label=f"Muestras del Coseno")
	plt.legend(loc=9)
	plt.title(f"Gráfica A*cos(Bx)")
	plt.ylabel(f"{A}*cos({B}*x)")
	plt.xlabel("x")
	plt.show()
	#
	#Gráfica B) De la parte Real
	#
	plt.plot(inList,rList,'co',label="Parte real")
	plt.legend(loc=9)
	plt.title(f"Gráfica A*cos(Bx)")
	plt.ylabel(f"{A}*cos({B}*x)")
	plt.xlabel("x")
	plt.show()
	#
	#Gráfica C) De la parte Imaginaria
	#
	plt.plot(inList,iList,'co',label="Parte Imaginaria")
	plt.legend(loc=9)
	plt.title(f"Gráfica A*cos(Bx)")
	plt.ylabel(f"{A}*cos({B}*x)")
	plt.xlabel("x")
	plt.show()
	#
	#Gráfica D) Del módulo
	#
	plt.plot(inList,xKList,'c^',label="Módulo de F(k)")
	plt.legend(loc=9)
	plt.title(f"Gráfica A*cos(Bx). Magnitud")
	plt.ylabel(f"|F(k)|")
	plt.xlabel("k")
	plt.show()




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
'''