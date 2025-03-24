// Blaine Buckler, Financial Calculator C
#include <stdio.h>
    float income, rent, utilities, groceries, transportation, expenses, savings, total; 

void getUserInput(char type[], float *cash) {
    printf("How much %s? ", type);
    scanf("%f", cash);
    
}

void percent(char type[], int amount){
    int per = amount/ income *100; 

    printf("The percent of your income for %s is %d%%.\n", type, per); 
}

int main(void){
    printf("Hello and welcome to our budget calculator\n"); 
    getUserInput("do you make each month", &income);
    getUserInput("is your rent", &rent);
    getUserInput("are your utilities", &utilities);
    getUserInput("are your groceries?", &groceries);
    getUserInput("is your transportation?", &transportation);
    expenses = rent + utilities + groceries + transportation; 
    savings = income * .2; 
    total = income - savings - expenses; 
    printf("\nYour monthly income is $%.2f\n", income); 
    printf("\nYour monthly expenses is $%.2f\n", expenses); 
    printf("\nYour monthly savings is $%.2f\n", savings); 
    printf("\nYou have $%.2f left over\n", total); 
    percent("rent", rent); 
    percent("utilities", utilities); 
    percent("groceries", groceries); 
    percent("transportation", transportation); 
    percent("exspenses", expenses); 
    return 0;
}