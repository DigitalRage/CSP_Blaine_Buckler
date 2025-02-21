//Blaine Buckler, Expressions Notes C
#include <stdio.h>
#include <math.h> 


int main(void){
    int num = 6;
    int numTwo = 13;
    int numThree = 16;
    int numFour = 2;

    int result = num + numTwo - numThree * numFour; 
    printf("%d\n", result);

//This is a new equation
    int numOne = 4;
    int numTwoOne = 2;
    int numThreeOne = 36;
    int numFourOne = 12;

    int resultTwo = (pow(numOne, numTwoOne)) - numThreeOne / numFourOne; 

    printf("%d\n", resultTwo);
}