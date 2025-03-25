#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    setenv("TZ", "America/Denver", 1);
    tzset();

    time_t current = time(NULL);
    struct tm *utah_time = localtime(&current);

    int hour = utah_time->tm_hour;
    
    if (hour > 20 && (hour < 6 || hour < 24)) {
        printf("It is bed time.\n");
    } else if (hour == 7) {
        printf("Get to school!\n");
    } else if (hour >= 7 && hour <=  16) {
        printf("It is school time.\n");
    } else {
        printf("It is after school.\n");
    }
    
    return 0;
}