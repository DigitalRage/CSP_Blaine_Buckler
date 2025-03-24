#include <stdio.h>
    char nameOne[50]; 
    char nameTwo[50];
    char nameThree[50]; 
    char nameFour[50];
    char nameFive[50]; 

void getUserInput(char name[]) {
    scanf("%s", name);
    printf("Hello %s\nNext: ", name); 
}

int main (void){
    printf("Give me five names ");
    getUserInput(nameOne); 
    getUserInput(nameTwo); 
    getUserInput(nameThree); 
    getUserInput(nameFour);
    getUserInput(nameFive); 

    return 0; 
}