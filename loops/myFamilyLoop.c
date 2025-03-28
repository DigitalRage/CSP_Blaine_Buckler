#include <stdio.h>
#include <string.h>

int main(void) {
    printf("These are some of my family members: "); 

    char famMembers[][20] = {"Sam, ", "Bruce, ", "Kitsune, ", "Meika, ", "Fletcher, ", "Christina"};
    
    strcpy(famMembers[5], " and Christina."); 

    int m = 0; 
    int mlength = sizeof(famMembers) / sizeof(famMembers[0]); 

    while (m < mlength) {
        printf("%s", famMembers[m]); 
        m++; 
    }

    return 0;
}
