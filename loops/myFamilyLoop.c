// Blaine Buckler, My Family Loop C
#include <stdio.h>

int main(void){
    char famMembers[][20] ={"Sam", "Bruce", "Kitsune", "Meika", "Fletcher", "Christina"}; 
    int m = 0; 
    int mlength = sizeof(famMembers)/sizeof(famMembers[0]); 
    while(m < mlength){
        printf("%s\n", famMembers[m]); 
        m++; 
    }
}