//Blaine Buckler, first program c
#include <stdio.h>

int main(void){
    char name[50];
    int num, num_two;
    printf("What is your name: "); 
    scanf("%s", name); 

    printf("Hello %s\n", name);

    printf("Please give me a number: ");
    scanf("%d", &num);

    printf("Please give me a second number: "); 
    scanf("%d", &num_two);

    printf("Your numbers added together will be: %d\n", num+num_two);
    return 0; 
}