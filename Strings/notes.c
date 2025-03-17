#include <stdio.h>
#include <string.h>

int main(void) {
    char lname[] = " LaRose";
    char fname[] = "Vienna";
    char prefix[] = "Ms.";
    strcat(prefix, fname); 
    printf("%s\n", prefix); 
    strcat(prefix, lname); 
    printf("%s\n", prefix); 
    printf("%lu\n", sizeof(prefix)); 
    return 0;
}
