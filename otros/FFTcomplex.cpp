/*
Nombre del Archivo:              fourier.cpp
Programador:	                 Avila S nchez Cristhian Alejandro.
Materia:                         Teor¡a de las Comunicaciones.
Fecha de Creaci¢n:               24 de abril de 2000.
Fecha de la £ltima Modificaci¢n: 24 de abril de 2000.
Descripci¢n:			 Programa que calcula la Transformada
				 Discreta de Fourier
//Versi¢n:			 mouse.
*/

#include <stdlib.h>
#include <string.h>
#include <time.h>
//#include <graphics.h>
#include <conio.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <dos.h>
#include <complex.h>
#include <mouse.h>
//#include "grphtext.h"


#define AMP1  32767.00
#define MAX   1686330.153
#define PI    3.14159
#define false 0
#define true  1

void Dibujar_Pantalla_Principal();
void Dibuja_Ejes_1();
void Dibuja_Ejes_2(double vmax);
void Dibujar_Graduacion_Y1();
void Dibujar_Graduacion_Y2(double vmax);
void Graduacion_Tiempo();
void Dibujar_Area_Tiempo();
void Dibujar_Area_Frecuencia(double vmax);
void Graficar_Bloque(int *xfun, unsigned n);
double *Calcular_TFD(int *f, unsigned N, double *max);
int *Leer_Bloque(FILE *fp, int *n, int *flag);
void Limpiar_Area_Tiempo();
void Graficar_TFD(double *xfun, unsigned n, double ampmax);
void MsgBloquen(unsigned i);
void Dibujar_Boton(int x3, int y3, int x4, int y4);
int Calcular_Y(double val, double max);
void Graduacion_Frecuencia();
void Triangulo_Vertical(int x, int y, int a);
void Triangulo_Horizontal(int x, int y, int a);
void Indicar_Voltaje(float vmax);
double *Calcular_FFT(int *f, unsigned N, double *max);
struct complex *Ordenamiento_Inversion_de_Bits(int *f, unsigned N);
unsigned Invertir_Bits(unsigned word);
struct complex *Crear_Familia_Pesos(unsigned N);
void Mariposa(struct complex *Fi, struct complex *Fk, unsigned i, unsigned k, unsigned mi, unsigned mk, struct complex *W, unsigned fact);


int void main()
{
 int gdriver= DETECT, gmode, gerror;
 char nomfp[80]= "voz.asc", op=' ';
 int *sblock, N=0, flag= false, b=0;
 double *fourier, vmax=0;
 time_t t1=0, t2=0;
 double seconds=0;
 FILE *fp;

/* if (argc!=2)
   exit(1);
 strcpy(nomfp, argv[1]);*/

 if ((fp= fopen(nomfp, "r"))==NULL)
   {
    printf("Imposible abrir el archivo");
    exit(1);
   }

 initgraph(&gdriver, &gmode, "c:\\borlandc\\bgi");
 gerror= graphresult();
 if (gerror<0)
   {
    printf("\nError inicializando gr ficos");
    printf("%s\n", grapherrormsg(gerror));
    exit(1);
   }


 Dibujar_Pantalla_Principal();

 while(1)
 {
  Dibujar_Area_Tiempo();
  sblock= Leer_Bloque(fp, &N, &flag);
  if (N==0)
    break;
//  fourier= Calcular_TFD(sblock, N, &vmax);
  t1= time(NULL);
  fourier= Calcular_FFT(sblock, N, &vmax);
  t2= time(NULL);
  seconds= difftime(t2, t1);
  setcolor(15);
  gprintfxy(500,20,"%f s", seconds);

  b++;
  MsgBloquen(b);

  Dibujar_Area_Frecuencia(vmax);
  Graduacion_Tiempo();
  Graficar_Bloque(sblock, N);
//  delay(5);
  Graficar_TFD(fourier, N, vmax);
  Graduacion_Frecuencia();
  Indicar_Voltaje(vmax);
  fflush(stdin);
  fflush(stdaux);
  free(sblock);
  free(fourier);
  if (flag==false)
    break;
  op= getch();
  if (op=='q' || op=='Q')
    break;
 }

 getch();
 getche();
 closegraph();
 return;
}

void Dibujar_Pantalla_Principal()
{
 setcolor(15);
 gprintfxy(180, 10, "Transformada de Rapida de Fourier");
 Dibujar_Area_Tiempo();
 Dibujar_Area_Frecuencia(AMP1);
}

void Dibujar_Area_Tiempo()
{
 Limpiar_Area_Tiempo();
 Dibuja_Ejes_1();
}

void Dibuja_Ejes_1()
{
 Dibujar_Graduacion_Y1();
 setcolor(7);
 line(65, 36, 65, 292); // Eje y
 line(55, 164, 585, 164);  //Eje x
 Triangulo_Vertical(65, 292, 2);
 Triangulo_Horizontal(585, 164, 2);
}

void Dibujar_Graduacion_Y1()
{
 int i=0, avz=0, z=2048;

 setcolor(7);
 settextstyle(2, HORIZ_DIR, USER_CHAR_SIZE);
 setusercharsize(9, 10, 3, 4);

 for (i=160; i>36; i=i-4)
    line(64, i, 66, i);

 for (i=168; i<292; i=i+4)
    line(64, i, 66, i);

 for (i=156; i>36; i=i-8)
    {
     setcolor(10);
     line(63, i, 67, i);
     setcolor(14);
     avz=avz+z;
     gprintfxy(20, i-4, "%d", avz);
    }

 avz=0;

 for (i=172; i<292; i=i+8)
    {
     setcolor(10);
     line(63, i, 67, i);
     setcolor(14);
     avz=avz-z;
     gprintfxy(20, i-4, "%d", avz);
    }
}

void Dibujar_Area_Frecuencia(double vmax)
{
 setfillstyle(SOLID_FILL, 0);
 bar(5, 315, 635, 475);
 setcolor(1);      //461
 rectangle(5, 315, 635, 475);
 Dibuja_Ejes_2(vmax);
}

void Dibuja_Ejes_2(double vmax)
{
 Dibujar_Graduacion_Y2(vmax);
 setcolor(7);
 line(65, 324, 65, 452); //y
 line(55, 452, 585, 452);  //x
 Triangulo_Vertical(65, 324, 2);
 Triangulo_Horizontal(585, 452, 2);

}

void Dibujar_Graduacion_Y2(double vmax)
{
 int i=0;
 double avz=0;

 setcolor(7);
 settextstyle(2, HORIZ_DIR, USER_CHAR_SIZE);
 setusercharsize(9, 10, 3, 4);

 for (i=448; i>324; i=i-4)
    line(64, i, 66, i);

 for (i=444; i>324; i=i-8)
    {
     setcolor(10);
     line(63, i, 67, i);
     setcolor(14);
     avz= (double) 452-i;
     avz= (double) avz/128;
     avz= (double) vmax*avz;
     gprintfxy(20, i-4, "%.0lf", avz);
    }
}

int *Leer_Bloque(FILE *fp, int *n, int *flag)
{
 unsigned i=0;
 int data=0, *arrvolt;
 *n=0;
 arrvolt= (int *) malloc(256*sizeof(int));

 *flag=true;

 arrvolt[0]=0;

 for(i=0; i<256;i++)
 {
  if (fscanf(fp, "%d", &data)==EOF)
    {
     *flag=false;
     break;
    }
  arrvolt[i]=data;
 }

 for ( ;i<256; i++)
    arrvolt[i]=0.0;

 *n=i;

 return(arrvolt);
}


void Graficar_Bloque(int *xfun, unsigned n)
{
 int i=0, x=65, y=0, yant=0;
 float val=0;


//se¤al
 setcolor(14);
 for (i=0; i<n; i++)
    {
     yant=y;
     val= (float) 128;
     val= (float) val*(xfun[i]);
     val= (float) val/AMP1;
     y= (int) val;
     y= (int) 164-y;
     if (x!=65)
       line(x-1, yant, x+1, y);
     putpixel(x+1,y,14);

     x=x+2;
    }
}

void Indicar_Voltaje(float vmax)
{
 mouseobj mouse;
 int x=0, y=0;
 float fx=0.0, fy=0.0;

 if (!mouse.init())
   {
    mouse.hide();
    mouse.show();
   }
 mouse.hide();
 mouse.show();

 while(!kbhit())
 {
//  c= mouse.waitforinput(EITHER_BUTTON);
/*  if (mouse.buttonreleased(RIGHT_BUTTON))
    break;*/
  if (mouse.buttonreleased(LEFT_BUTTON))
    {
     mouse.getcoords(x,y);
     if (mouse.inbox(5, 25, 635, 305, x, y)==TRUE)
       {
	fy=(float) ((164-y)*32767.00)/128;
	fx=(float) (.48828)*((x-65)/2);
	setcolor(10);
	settextstyle(2, HORIZ_DIR, USER_CHAR_SIZE);
	setusercharsize(9, 10, 3, 4);
	gprintfxy(500, 15,"                         ");
	gprintfxy(500, 15,"%.3f æs : %.2f V", fx, fy);
       }

     if (mouse.inbox(5, 324, 635, 452, x, y)==TRUE)
       {
	fy= (float) 452-y;
	fy= (float) fy/128;
	fy= (float) vmax*fy;
	fx=(float) 31.25*((x-65)/2);
	setcolor(10);
	settextstyle(2, HORIZ_DIR, USER_CHAR_SIZE);
	setusercharsize(9, 10, 3, 4);
	gprintfxy(500, 15,"                         ");
	gprintfxy(500, 15,"%.2f Hz : %.2f V", fx, fy);
       }

    }
 }

 mouse.hide();
}

void Limpiar_Area_Tiempo()
{
 setfillstyle(SOLID_FILL, 0);
 bar(5, 25, 635, 305);
 setcolor(1);
 rectangle(5, 25, 635, 305);
}

void Graduacion_Tiempo()
{
 int i=0;

 for (i=65; i<=575; i=i+2)
    {
     setcolor(8);
     line(i, 162, i, 166); //y
     line(i, 450, i, 454); //y
    }

 setcolor(10);
 for (i=65; i<=575; i=i+16)
    line(i, 161, i, 167); //y
}

void Graduacion_Frecuencia()
{
 int i=0, x=0, f=0;

 for (i=65; i<=575; i=i+2)
    {
     if (x%32==0)
       {
	setcolor(7);
	gprintfxy(i, 456, "%d kHz", f);
	f++;
	setcolor(10);
	line(i, 449, i, 455); //y
       }

     x++;
    }

  i=577;
  setcolor(7);
  gprintfxy(i, 456, "%d kHz", 8);
  setcolor(10);
  line(i, 449, i, 455); //y
}

/*double *Calcular_TFD(int *f, unsigned N, double *max)
{
 double *F, cy=0;
// struct complex C, CF;
 struct complex C, CF;
 int m=0, n=0;

 F= (double *) malloc(N*sizeof(double));

 C= complex(0,0);
 *max=0;

 for (m=0; m<N; m++)
    {
     CF= complex(0,0);
     for (n=0; n<N; n++)
	{
	 cy= n*(-2*PI*m/N);
	 C= complex(0, cy);
	 CF= CF + f[n]*(exp(C));
	}
     F[m]= abs(CF);
     if (F[m]>*max)
       *max= F[m];
    }
 return(F);
} */

void Graficar_TFD(double *xfun, unsigned n, double ampmax)
{
 int i=0, x=65, y=0;

//se¤al
 setcolor(8);

 for (i=0; i<n; i++)
    {
     y= Calcular_Y(xfun[i], ampmax);
     line(x, 452, x, y);
     putpixel(x,y,15);
     x=x+2;
    }

// Indicar_Voltaje(AMP1);
}

void MsgBloquen(unsigned i)
{
 char num[80], cadena[80]="Bloque: ";

 settextstyle(2, HORIZ_DIR, USER_CHAR_SIZE);
 setusercharsize(11, 10, 4, 4);
 gprintfxy(20, 10, "                    ");
 itoa(i,num,10);
 strcat(cadena,num);

 Dibujar_Boton(10, 12, 18, 20);
 setcolor(9);
 gprintfxy(20, 10, "%s", cadena);
}

void Dibujar_Boton(int x3, int y3, int x4, int y4)
{
 setfillstyle(1, 7);

 bar3d(x3, y3, x4, y4, 0, 0);

 setcolor(15);
 line(x3, y3, x3, y4);
 line(x3, y3, x4, y3);

 setcolor(0);
 line(x3, y4, x4, y4);
 line(x4, y4, x4, y3);
}

int Calcular_Y(double val, double max)
{
 double aux=0;
 int y=0;

 aux= (double) 128;
 aux= (double) aux*val;
 aux= (double) aux/max;
 y= (int) aux;
 y= (int) 452-y;

 return(y);
}

void Triangulo_Vertical(int x, int y, int a)
{
 int points[6];

 points[0]= x-a/2;
 points[1]= y;
 points[2]= x;
 points[3]= y - (int) ((pow(a, 2)) - (pow(a/2, 2)));
 points[4]= x+a/2;
 points[5]= y;
 setfillstyle(SOLID_FILL, 10);
 setcolor(10);
 fillpoly(3, points);
}

void Triangulo_Horizontal(int x, int y, int a)
{
 int points[6];

 points[0]= x;
 points[1]= y-a/2;
 points[2]= x + (int) ((pow(a, 2)) - (pow(a/2, 2)));
 points[3]= y;
 points[4]= x;
 points[5]= y+a/2;
 setfillstyle(SOLID_FILL, 10);
 setcolor(10);
 fillpoly(3, points);
}

double *Calcular_FFT(int *f, unsigned N, double *max)
{
 double *F, aux=0;
 struct complex *Fc, *W;
 unsigned E=0, G=0, M=0, e=0, g=0, m=0, p=0, i=0;
 unsigned wn=0;


 F= (double *) malloc(N*sizeof(double));
 Fc= Ordenamiento_Inversion_de_Bits(f, N);
 W= Crear_Familia_Pesos(N);

 E= log(N)/log(2);
 G= N/2;
 M= 1;
 *max=0;

 for (e=1; e<=E; e++)
    {
     p=0;
     wn= N/G;
     for (g=0; g<G; g++)
	{
	 i= p;
	 for (m=0; m<M; m++)
	   {
	    Mariposa(&(Fc[i]), &(Fc[i+M]), i, i+M, m, m+M, W, G);
	    i++;
	   }
	 p=p+wn;
	}
     G= G/2;
     M= 2*M;
    }

  free(W);

  for (i=0; i<256; i++)
     {
      F[i]= abs(Fc[i]);
      if (F[i]>*max)
	*max= F[i];
     }

  free(Fc);
  return(F);
}

struct complex *Ordenamiento_Inversion_de_Bits(int *f, unsigned N)
{
 struct complex *fc;
 unsigned i=0, j=0;

 fc= (struct complex *) malloc(N*sizeof(struct complex));

 for (i=0; i<N; i++)
    {
     j= Invertir_Bits(i);
     fc[j]= complex(f[i],0);
    }
 return(fc);
}

unsigned Invertir_Bits(unsigned word)
{
 unsigned lowbit= 0x01, tp=0x00, wordf=0x00;
 int n=0;

 for (n=15; n>=0; n--)
    {
     tp= word & lowbit;
     tp= tp<<n;
     wordf= wordf | tp;
     word= word>>1;
    }
 wordf= wordf>>8;
 return(wordf);
}

struct complex *Crear_Familia_Pesos(unsigned N)
{
 struct complex *W, z;
 double cj=0, cm=0;
 int m=0;

 W= (struct complex *) malloc(N*sizeof(struct complex));

 cj= -2*PI/N;
 for (m=0; m<N; m++)
    {
     cm= cj*m;
     z= complex(0, cm);
     W[m]= (exp(z));
    }
 return(W);
}

void Mariposa(struct complex *Fi, struct complex *Fk, unsigned i, unsigned k, unsigned mi, unsigned mk, struct complex *W, unsigned fact)
{
 struct complex Fj;

 Fj= *Fi;

 *Fi= (*Fi)+(*Fk)*(W[mi*fact]);
 *Fk=  Fj+(*Fk)*(W[mk*fact]);
}

