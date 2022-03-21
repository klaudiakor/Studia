/* autor: Klaudia Korczak */
/* Program do obslugi sygnalow z mozliwosciami: 
    (1) wykonania operacji domyslnej 
    (2) ignorowania
    (3) przechwycenia i w lasnej obslugi sygnalu. 
Do oczekiwania na sygnal uzyc funkcji pause. */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <signal.h>
#include <unistd.h>

void my_sighandler(int);

int main(int argc, char *argv[])
{

    int option;     /* nr operacji do wykonania */
    int signal_num; /* nr sygnalu */

    if (argc != 3)
    {
        printf("Nieprawidlowa ilosc argumentow!\n");
        printf("Nalezy podac: ./A.x   nr operacji   nr sygnalu\n");
        printf("Mozliwe operacje:\n"
               "\t 1 - operacja domyslna\n"
               "\t 2 - ignorowanie\n"
               "\t 3 - wlasna obsluga sygnalu\n");
        exit(1);
    }

    option = atoi(argv[1]);
    signal_num = atoi(argv[2]);

    switch (option)
    {
    case 1:
        /*wykonanie operacji domyślnej*/
        if (signal(signal_num, SIG_DFL) == SIG_ERR)
        {
            perror("signal function error");
            exit(-1);
        }
        else
        {
            printf("Wykonano operacje domyslna.\n");
            exit(0);
        }
        break;
    case 2:
        /*ignorowanie*/
        if (signal(signal_num, SIG_IGN) == SIG_ERR)
        {
            perror("signal function error");
            exit(-1);
        } /*ignoruje sygnal o nr podanym w argumentach wywolania programu*/
        printf("PID = %d\n", getpid());
        printf("Czekam na sygnal ...\n");
        /*czeka na sygnal z terminala*/
        pause();
        break;
    case 3:
        /*przechwycenie i własna obsługa sygnału*/
        if (signal(signal_num, my_sighandler) == SIG_ERR)
        {
            perror("signal function error");
            exit(-1);
        }
        else
        {
            my_sighandler(signal_num);
            exit(1);
        }
        break;
    default:
        printf("Nie ma takiej opcji.\n");
        break;
    }
    return 0;
}

/* funkcja do własnej obslugi sygnalu */
void my_sighandler(int sig_num)
{
    printf("Wlasna obsluga sygnalu nr %d\n", sig_num);
}

