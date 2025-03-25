// Blaine Buckler, Old Enough C
#include <stdio.h>
#include <string.h> 

int main(void){
    int age; 
    printf("Please tell me your age: "); 
    scanf("%d", &age); 

    if(age >= 18){
        printf("You are old enough to vote. \n"); 
    }else if (age >= 16){
        printf("You are old enough to drive. \n"); 
    }else if (age >= 15){
        printf("You are old enough to have a drivers permit. \n"); 
    }else if (age >= 5){
        printf("You are old enough to go to school. \n"); 
    }else{
        printf("You are not old enough to go to school. \n"); 
    }
    return 0;
} 
