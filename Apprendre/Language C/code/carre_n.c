#include <stdio.h>
#include <stdlib.h>

int puissance_n(int nbr, int n)
{
    if (n > 1)
    {
        return puissance_n(nbr, n-1) * nbr;
    }
    else
    {
        return nbr;
    }
}

int main()
{
    int nbr, n = 0;
    printf("Nombre : ");
    scanf("%d",&nbr);
    printf("Puissance : ");
    scanf("%d",&n);
    int resultat = puissance_n(nbr,n);
    printf("%d**%d=%d\n", nbr, n , resultat);
}