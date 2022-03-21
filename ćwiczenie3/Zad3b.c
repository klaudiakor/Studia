/* Autor: Klaudia Korczak */
/*  Uruchomia program A poprzez funkcje exec w procesie potomnym innego
procesu i wysylac do niego sygnaly poprzez funkcje systemowa kill z procesu macierzystego. */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <signal.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>

#define _POSIX_C_SOURCE 200112L
#define _XOPEN_SOURCE 500

int kill(pid_t, int);

int main(int argc, char *argv[])
{

    /* argumnety:
        1) nr operacji
        2) nr sygnalu
    */

    /* Zla liczba argumentow */
    if (argc != 3)
    {
        printf("Nieprawidlowa ilosc argumentow!\n");
        printf("Nalezy podac: ./B.x   nr operacji   nr sygnalu\n");
        printf("Mozliwe operacje:\n"
               "\t 1 - operacja domyslna\n"
               "\t 2 - ignorowanie\n"
               "\t 3 - wlasna obsluga sygnalu\n");
        exit(-1);
    }

    int signal_num = atoi(argv[2]); /* nr sygnalu */

    int fork_status = fork();
    switch (fork_status)
    {
    case -1:
    /* blad funkcji fork */
        perror("fork error");
        exit(-1);
    case 0:
    /* akcja dla procesu potomnego */
        /* uruchomic funkcja exec program A */

        printf("Proces %d czeka na sygnal aby odpalic program\n", getpid());
        pause(); /*czeka na sygnal z procesu macierzystego*/
        execl("./A.x", "A.x", argv[1], argv[2], NULL);
        perror("execl error");
        exit(-1);

        break;

    default:
    /* akcja dla procesu macierzystego */
        sleep(1);
        /* sprawdzam czy proces istnieje */
        kill(fork_status, 0);
        if (errno == ESRCH)
        {
            perror("process doesn't exist");
            exit(-1);
        } /* Wysyłam do niego sygnał */
        else if (kill(fork_status, signal_num) == -1)
        {
            perror("kill error");
            exit(-1);
        }
        else
        {
            printf("Wysylam sygnal %d do procesu %d.\n", signal_num, fork_status);
        }
        /*czekam na zakonczenie procesow potomnych*/
        if (wait(0) == -1)
        {
            perror("wait error");
        }
        break;
    }

    return 0;
}