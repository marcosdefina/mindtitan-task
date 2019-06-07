#include <stdio.h>
#include <time.h>

int busy_sleep(float time){
    clock_t begin;
    double time_spent;
    unsigned int i;

    begin = clock();
    for (i = 0; 1; i++)
    {
        time_spent = (double)(clock() - begin) / CLOCKS_PER_SEC;
        if (time_spent >= time)
            break;
    }
    return (0);
}