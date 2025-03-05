// Blaine Buckler, Loops Notes C
#include <stdio.h>

int main(void){
    printf("Hello World"); 
    //1. What is a loop?
        //. A section of code that repeats
    //2. What are two types of loops?
        //For loops
        int x;
        for(x=0; x<10; x++){
            printf("Hello\n"); 
        }
        //While loops
        int i = 1;
        while(i<10){
            printf("%d\n", i); 
            i++;
        }
    //3. What is iteration?
        //The act of repeating
    //4. What are lists (arrays)?
        //A bunch of values in one variable

    //8. How do you make lists in C?
    int grades[] = {97, 95, 100, 70, 94, 98, 64}; 
        // In the brackets we say how list will be, if list is set brackets can be blank
        //Data type is the given as whatever is in the list (All list items must be the same data type)
        //List is surrounded by curly brackets{} with commas , between each item
    printf("%d\n", grades[3]); //To print one item we put the index number in the brackets we print
    grades[2] = 73; 
    printf("%d\n", grades[2]); // Update grades one at a time using the index number
    //Tells me the bytes  in my array(list)
    //printf(%lu, sizeof(grades)); 
    // How to get the size of an array(list)
    int length = sizeof(grades)/sizeof(grades[0]); 
    printf("%d\n", length); 
    //9. How do you make for Loops in C?
        //iterators should be x or i
    int t;
        // In parntheses 1. starting point 2. go until point 3. what we count by
    for(t=0;t<10;t+=2){
        printf("%d\n", t); 
    }
    int l; 
    for(l=0;l<length;l++){
        printf("%d\n", grades[1]); 
    }

    //10. How do you make wile loops in C? 
    // use iterator to set start point
    int iterator= 100; 
    //While line sets the stop point/ how long it goes
    while(iterator >=0){
        printf("%d\n", iterator); 
        //sets what I can count by
        iterator -= 10; 
    }


    char movies[][20] ={"Cinderella", "The Smerf Movie", "Transformers", "Cars", "Up", "1984"}; 
    int m = 0; 
    int mlength = sizeof(movies)/sizeof(movies[0]); 
    while(m < mlength){
        printf("%s\n", movies[m]); 
        m++; 
    }
        //sets what I can count by


    return 0;
}