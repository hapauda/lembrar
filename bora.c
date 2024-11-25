#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
// os mais importantes
int main() 
{
    char sprin[] = "Assim faz uma spring";
    printf("%s\n", sprin);
    printf("%d\n", strlen(sprin));
    char ch;
    char    s[100];
    char sen[100];
    scanf("%c", &ch);
    scanf("%s", &s);
    getchar(); // arrumar o prblema do \n usa getchar() ou scanf("\n") pois a proxima sentenç autiliza todas as afirmações ate ficar em momento NULL;
    scanf("%[^\n]%*c", sen);
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
    }
//   adicionar todos os caracteres que possam ser incluidos somente na variavel escolhida