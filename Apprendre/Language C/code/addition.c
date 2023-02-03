#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A = 0;
    int B = 0;
    int resultat = 0;

    printf("Addition de A+B\n\nVeuillez définir A: ");
    scanf("%d",&A);
    printf("Veuillez définir B: ");
    scanf("%d",&B);
    
    resultat = A + B;
    
    printf("\n%d+%d=%d\n", A, B, resultat);
}