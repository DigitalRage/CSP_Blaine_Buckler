// Blaine Buckler, budget C
#include <stdio.h>

int main(void){
    float income, remt, utilities, groceries, transportation, savings, expenses, total; 
    printf("Hello and welcome to our budget calculator\n"); 
    printf("How much do you make each month?");
    scanf("%f", &income); 
    printf("Your monthly income is $%.2f\n", income); 
    return 0;
}