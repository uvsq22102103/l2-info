#include <stdio.h>

int main() {
    unsigned int stop = 0;
    unsigned long somme = 0;
    unsigned int compteur = 0;
    
    printf("Somme des entiers jusqu'à : ");
    scanf("%d", &stop);
    
    while (compteur < stop)
    {
        compteur ++;
        somme += compteur;
        printf("Somme n°%d : %ld\n",compteur,somme);
    }
    
    return 0;
}