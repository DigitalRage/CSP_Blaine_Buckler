// Blaine Buckler Name decorator, C
#include <stdio.h>
#include <string.h>

int main(void){
    char name[50]; 
    char smile[100] = "(: ";
    char smileT[4] = " :)";
    char hash[100] = "##"; 
    char hashT[3]= "##"; 
    char arrow[100] = "<><>";
    char arrowT[5] = "<><>";
    printf("Please tell me your name: ");
    scanf("%s", name);

    strcat(smile, name); 
    strcat(smile, smileT); 
    strcat(hash, name); 
    strcat(hash, hashT); 
    strcat(arrow, name); 
    strcat(arrow, arrowT); 

    printf("%s\n", smile); 
    printf("%s\n", hash); 
    printf("%s\n", arrow); 
    

    return 0; 
}