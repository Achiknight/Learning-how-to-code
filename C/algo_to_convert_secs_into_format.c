#include <stdio.h>

int main() {
    
    int in_sec = 3870;
    int hours,mins,secs;

    // hours = in_sec/3600;
    // mins = (in_sec%3600)/60;
    // secs = (in_sec%3600)%60;

    hours = in_sec/3600;
    in_sec = in_sec%3600;
    mins = in_sec/60;
    secs = in_sec%60;


    printf("In HH:MM:SS %d %d %d \n",hours,mins,secs);


    return 0;
}