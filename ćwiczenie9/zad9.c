//autor: Klaudia Korczak
//Wzajemne wykluczenie dla watkow: muteksy

/* dla semaforow
binary semaphore S=1;
//proces P_i
do {
    wlasne sprawy
    PB(S);
    sekcja krytyczna
    VB(S);
    reszta
} while(1)
*/

#define _REENTRANT
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int counter = 0;

int main(int argc, char *argv[]){

    if(argc != 3){
        printf("Zla liczba argumentow.\n");
        exit(1);
    }

    srand(time(0));

    //tworzenie watku
    pthread_t *pthreadID = NULL; //identyfikator watku
    const pthread_attr_t *attr;  //struktura atrybutow
    void *(*start_fun)(void *);  //funkcja dla watku
    void *arg;                   //argument funkcji
    int pthread_create_resault;
    pthread_create_resault = pthread_create(pthreadID, attr, start_fun, arg);
    if(pthread_create_resault != 0) {
        printf("pthread_create error\n");
        exit(1);
    }

    //muteks
    pthread_mutex_t myMutex = PTHREAD_MUTEX_INITIALIZER; //otwiera muteks i inicjuje na otwarty (0)

    pthread_mutex_lock(&myMutex);

    //SEKCJA KRYTYCZNA
    int private_counter = counter;
    private_counter++;
    sleep((rand()%2)/5);
    counter = private_counter;
    //KONIEC SEKCJI KRYTYCZNEJ
    //....

}