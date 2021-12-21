#include<iostream>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>

#define TAM 1024
using namespace std;

int main(){
	int i;
	printf("Generador del txt\n\n");
    FILE *fd;
    char buff[12];
    fd = fopen("lista.txt","a");
    if(fd != NULL){
        printf("\n  Se creo el archivo\n");
        for(i=0;i<TAM;i++){
        	fputs(itoa(i,buff,10),fd);
        	if(i+1!=TAM){
        		fputs(" ",fd);
			}
        }
    }
    else{
        printf("\n  No se pudo crear el archivo");
    }
    fclose(fd);
    return 0;
}
