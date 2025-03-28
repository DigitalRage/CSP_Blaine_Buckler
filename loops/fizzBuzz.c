//Blaine Buckler, Fizz Buzz C
#include <stdio.h>

int main() {
    int num = 1;          
    int multiplier = 3; 
    int multiplierT = 5; 

    while (num < 51) {
        if (num % multiplier == 0 && num % multiplierT == 0) {
            printf("FizzBuzz\n"); 
        } else if (num % multiplier == 0) {
            printf("Fizz\n"); 
        } else if (num % multiplierT == 0) {
            printf("Buzz\n"); 
        } else {
            printf("%d\n", num); 
        }
        num++; 
    }

    return 0; 
}
