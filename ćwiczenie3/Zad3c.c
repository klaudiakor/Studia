/* Autor: Klaudia Korczak */
/*  W procesie macierzystym utworzyc proces potomny i sprawic, 
aby stal sie liderem nowej grupy procesow (funkcja setpgid),
a nastepnie uruchomic w nim kilka procesow potomnych wykonujacych program do obslugi sygnalow.
Z pierwszego procesu macierzystego wysylac sygnaly do calej grupy procesow potomnych po uprzednim
sprawdzeniu jej istnienia. Identyfikator tej grupy procesow uzyskac przypomocy funkcji getpgid. 
Proces bedacy liderem grupy procesow niech ignoruje sygnaly,
a na koncu czeka na zakonczenie wszystkich swoich procesow potomnych i wypisuje ich status 
zakonczenia zwracany przez funkcje wait. */

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
pid_t getpgid(pid_t);

int main(int argc, char *argv[])
{
    /*Zla ilosc argumentow */
    if (argc != 3)
    {
        printf("Nieprawidlowa ilosc argumentow!\n");
        printf("Nalezy podac: ./C.x  nr operacji   nr sygnalu\n");
        printf("Mozliwe operacje:\n"
               "\t 1 - operacja domyslna\n"
               "\t 2 - ignorowanie\n"
               "\t 3 - wlasna obsluga sygnalu\n");
        exit(-1);
    }
    char *option = argv[1];
    char *signal_num = argv[2];
    //int Option = atoi(argv[1]); /*nr opcji obslugi */
    int SignalNum = atoi(argv[2]); /*nr sygnalu*/

    printf("PID = %d, PPID = %d, PGID = %d [PROCES MACIERZYSTY]\n",
           getpid(), getppid(), getpgrp());

    int wait_status; /*przechowuje status funkcji waitpid*/
    int fork_resault = fork();
    switch (fork_resault)
    {
    case -1:
    /* blad funkcji fork */
        perror("fork error");
        exit(1);
    case 0:
    /*PROCES POTOMNY */
        /* uruchamia program ignorujacy sygnal */
        if (signal(SignalNum, SIG_IGN) == SIG_ERR)
        {
            perror("signal function error");
            exit(-1);
        }
        printf("PID = %d, PPID = %d, PGID = %d [POTOMEK]\n",
               getpid(), getppid(), getpgrp());
        /*staje sie liderem swojej gr procesow*/
        int lider_pid = getpid(); /* pid procesu który stanie się liderem swojej grupy*/
        setpgid(lider_pid, 0);
        printf("PID = %d, PPID = %d, PGID = %d [POTOMEK - LIDER]\n\n",
               getpid(), getppid(), getpgrp());

        /*tworzenie procesow potomnych, wykonujacych (A)*/
        int i;
        for (i = 0; i < 3; i++)
        {
            switch (fork())
            {
            case -1:
                perror("fork error");
                exit(1);
            case 0:
                /* proces potomny */
                printf("[POTOMEK %d]: \n", getpid());
                /*wykonuja program do obslugi sygnalow (A)*/
                execl("./A.x", "A.x", option, signal_num, NULL);
                perror("execl error");
                exit(-1);
                break;
            default:
                /*proces macierzysty*/
                /* czeka na potomkow */
                if (waitpid(-getpgrp(), &wait_status, 0) == -1)
                {
                    perror("waitpid error");
                    exit(-1);
                }
                printf("status zakonczenia: %d \n", WIFEXITED(wait_status));
                break;
                /*  WIFEXITED(wstatus) - returns true if the child terminated normally */
            }
        }
        break;
    default:
    /* PROCES MACIERZYSTY */
        sleep(1);
        int liderPID = getpgid(fork_resault); /* PID lidera grupy */
        /* czeka na procesy z grupy lidera */
        if (waitpid(-liderPID, &wait_status,0) == -1)
        {
            perror("waitpid error");
            exit(-1);
        }
        
        /*sprawdzam istnienie gr procesow */
        if (kill(-liderPID, 0) == ESRCH)
        {
            perror("group of processes doesn't exist");
            exit(-1);
        }
        else
        {
            printf("\nGrupa procesow istnieje.\n");
            printf("Wysylam sygnal %d do grupy procesow %d\n", SignalNum, liderPID);
            /*wysyla sygnał do całej grupy procesów */
            kill(-liderPID, SignalNum);
        }
        break;
    }
    return 0;
}
