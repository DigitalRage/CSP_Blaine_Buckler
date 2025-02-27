// Blaine Buckler, Financial Calculator C
#include <stdio.h>

int main(void){
    float income, rent, utilities, groceries, transportation, savings, expenses, total; 
    float prent, putilities, pgroceries,  ptransportation, psavings, pexpenses, left; 
    printf("Hello and welcome to our budget calculator\n"); 
    printf("How much do you make each month?");
    scanf("%f", &income); 
    printf("How is your rent?");
    scanf("%f", &rent); 
    printf("How are your utilities?");
    scanf("%f", &utilities); 
    printf("How are your groceries?");
    scanf("%f", &groceries);
    printf("How is your transportation?");
    scanf("%f", &transportation); 
    expenses = rent + utilities + groceries + transportation; 
    savings = income * .2; 
    total = income - savings - expenses; 
    printf("\nYour monthly income is $%.2f\n", income); 
    printf("\nYour monthly expenses is $%.2f\n", expenses); 
    printf("\nYour monthly savings is $%.2f\n", savings); 
    printf("\nYou have $%.2f\n left over\n", total); 
    prent = rent/income *100; 
    putilities = utilities/income *100; 
    pgroceries = groceries/income *100; 
    ptransportation =transportation/income *100; 
    pexpenses = expenses/income *100; 
    psavings = savings/income *100; 
    left = 100 - pexpenses - psavings; 
    printf("\nYour exspenses are %.f%% of your income\n", pexpenses); 
    printf("within your exspenses is: \n"); 
    printf("    %.f%% is your rent\n", prent); 
    printf("    %.f%% is your utilities\n", putilities); 
    printf("    %.f%% is your groceries\n", pgroceries); 
    printf("    %.f%% is your transportation\n", ptransportation); 
    printf("\nYour savings are %.f%% of your income\n", psavings); 
    printf("\nMeaning you will have %.f%% left over\n", left); 
    return 0;
}