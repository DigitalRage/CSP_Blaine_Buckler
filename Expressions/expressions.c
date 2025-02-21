//Blaine Buckler, Expressions Assignment C
#include <stdio.h> 
#include<math.h>
int main(void){

    int exponentOfTwo = 2; 
    int exponentOfThree = 3; 
    int exponentOfFour = 4; 
    int exponentOfFive = 5; 

    int numOne = 7; 
    int numTwo = 24; 
    int numThree = 8; 
    int numFour = 4; 
    int numFive = 6; 

    int result = numOne - numTwo / numThree * numFour + numFive; 

    printf("%d\n", result); 

    int numOneTwo = 18; 
    int numTwoOne = 3; 
    int numThreeOne = 7; 
    int numFourOne = 2; 
    int numFiveOne = 5; 

    int resultTwo = numOneTwo / numTwoOne - numThreeOne + numFourOne * numFiveOne; 

    printf("%d\n", resultTwo); 

    int numOneThree = 6; 
    int numTwoThree = 4; 
    int numThreeThree = 12; 
    int numFourThree = 72; 
    int numFiveThree = 8;
    int numSixThree = 9;  

    int resultThree = numOneThree * numTwoThree - numThreeThree + numFourThree / numFiveThree - numSixThree;

    printf("%d\n", resultThree);  
}
