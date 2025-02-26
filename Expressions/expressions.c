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
    int numOneFour = 17;
    int numTwoFour = 6;
    int numThreeFour = 2; 
    int numFiveFour = 4; 
    int numSixFour = 3;

    int resultFour = (numOneFour - numTwoFour / numThreeFour) + numFiveFour * numSixFour; 

    printf("%d\n", resultFour);

    int numOneFive = -2;
    int numTwoFive = 1;
    int numThreeFive = 4; 
    int numFourFive = 2; 
    int numFiveFive = 2;
    int numSixFive = 6; 
    int numSevenFive = 2; 
    int numEightFive = 3; 

    int resultFive = numOneFive * (numTwoFive * numThreeFive - numFourFive / numFiveFive) + (numSixFive + numSevenFive - numEightFive); 

    printf("%d\n", resultFive);

    int numOneSix = -1; 
    int numTwoSix = 3; 
    int numThreeSix = 4; 
    int numFourSix = 7; 
    int numFiveSix = 5; 
    int numSixSix = 2; 
    int numSevenSix = 24; 
    int numEightSix = 6; 

    int resultSix = numOneSix * ((numTwoSix - numThreeSix * numFourSix) / numFiveSix) - numSixSix * numSevenSix / numEightSix; 

    printf("%d\n", resultSix); 

    int numOneSeven = 3; 
    int numTwoSeven = 5; 
    int numThreeSeven = 15; 
    int numFourSeven = 5; 
    int numFiveSeven = 2; 

    int resultSeven = (numOneSeven * (int)pow(numTwoSeven, exponentOfTwo) / numThreeSeven) - (numFourSeven - (int)pow(numFiveSeven, exponentOfTwo)); 

    printf("%d\n", resultSeven); 

    int numOneEight = 1; 
    int numTwoEight = 2; 
    int numThreeEight = 3; 
    int numFourEight = 2; 
    int numFiveEight = 4; 

    int resultEight = ((int)pow(numOneEight, exponentOfFour) * (int)pow(numTwoEight, exponentOfTwo) + (int)pow(numThreeEight, exponentOfThree)) - (int)pow(numFourEight, exponentOfFive) / numFiveEight; 

    printf("%d\n", resultEight); 

    int numOneNine = 22; 
    int numTwoNine = 2; 
    int numThreeNine = 2; 
    int numFourNine = 5; 
    int numFiveNine = 4; 
    int numSixNine = 6; 
    int numSevenNine = 6; 

    int resultNine = (int)pow((numOneNine / numTwoNine - numThreeNine * numFourNine), exponentOfTwo) + (int)pow((numFiveNine - numSixNine / numSevenNine), exponentOfTwo); 

    printf("%d\n", resultNine); 

    return 0; 
}
