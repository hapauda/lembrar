#include <stdio.h>

int main() {
  // Create an int and a char variable
  int myNum;
  char myChar [20] ;

  // Ask the user to type a number AND a character
  printf("Type a number AND a character and press enter: \n");

  // Get and save the number AND character the user types
  scanf("%d %s", &myNum, myChar);

  // Print the number
  printf("Your number is: %d, char is: %s\n", myNum, myChar);

  // Print the character
  
  return 0;
}
