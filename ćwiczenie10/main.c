#define _REENTRANT
#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>

//funkcja dla watku
void *start_fun(void *arg)
{
    printf("Moja funkcja\n");
    return NULL;
}

int main()
{
    int i;
    int max_thread_num = 5;
    pthread_t threads_id[max_thread_num]; //identyfikatory watkow
    pthread_attr_t attr;
    if (pthread_attr_init(&attr) != 0)
    {
        perror("pthread_attr_init error");
        exit(1);
    }
    void *arg = NULL;
    //tworzenie watkow
    for (i = 0; i < max_thread_num; i++)
    { // TODO: pre czy post inkrementacja?
        if (pthread_create(&threads_id[i], &attr, &start_fun, arg) != 0)
        {
            printf("pthread_create error\n");
            exit(2);
        }
    }
    int value[max_thread_num];
    int max_val = value[0];
    // szukam najwiekszej wartosci wsprod watkow
    for (i = 0; i < max_thread_num; i++)
    {
        if(max_val < value[i]){
            max_val = value[i];
        }
    }
    //value[thread] = max_val + 1;
    return 0;
}