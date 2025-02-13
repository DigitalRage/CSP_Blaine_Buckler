//Blaine Buckler, c practice assignment
#include <stdio.h> 

char name[] = "Blaine"; 
int age = 14;
float pi = 3.14;
int num = 7;
int hun_to_thou = 256;
char breakfast[] = "Lucky Charms"; 
char color[] = "Navy Blue"; 
char subject[] = "Digital Media"; 

int main(void){
    printf("Hello I'm %s my age is %d and my favorite number between one and ten is %d. \nIf i would chose a number between 100 and 1000 I would chose %d, what I had for breakfast was %s. \nMy favorite color is %s and favorite subject is %s. ", name, age, num, hun_to_thou, breakfast, color, subject);
    return 0;
}