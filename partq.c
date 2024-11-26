#include <stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>

int main(){
  int *p;
  p = (int *) malloc(5*sizeof(int));
  printf("%d\n", p);
  printf("Holas amigo\n");
  free(p);
}