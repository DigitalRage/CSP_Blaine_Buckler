//Blaine Buckler, silly sentences c
#include <stdio.h>

#include <string.h>

int main(void){
    char sentence[200] = "As a "; //all strings for the sentence end up here in the end
    char name[50];
    char noun[50];
    char adverb[50];
    char verb[50];

    printf("Please tell me your name: \n"); 
    scanf("%s", name);
    printf("Hello %s this is like a MadLib\nPlease answer the questions.\n", name);

    printf("Please tell me a noun: ");
    scanf("%s", noun);

    printf("Please tell me a adverb: ");
    scanf("%s", adverb);

    printf("Please tell me a past tense verb: ");
    scanf("%s", verb);

    strcat(sentence, noun);
    strcat(sentence, " ");
    strcat(sentence, adverb); 
    strcat(sentence, " walked by another "); 
    strcat(sentence, noun); 
    strcat(sentence, " it "); 
    strcat(sentence, adverb);
    strcat(sentence, " back ");
    strcat(sentence, adverb);
    strcat(sentence, ". ");

    printf("%s", sentence); 

    return 0;
}
