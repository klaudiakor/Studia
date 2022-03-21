/* wywolac funkcje fork 3x i wypisac identyfikatory dla procesu macierzystego oraz wszystkich procesow potomnych. 
Przy pomocy funkcji wait sprawic, aby proces macierzysty zaczekal na zakończenie procesów potomnych */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int process_id()
{
    printf("UID = %d, GID = %d, PID = %d, PPID = %d, PGID = %d\n",
           getuid(), getgid(), getpid(), getppid(), getpgrp());
    return 0;
}

int main()
{
    int i;
    int j;
    printf("\n[PROCES MACIERZYSTY]: ");
    process_id(); /*wypisuje id dla procesu macierzystego*/

    for (i = 0; i < 3; i++)
    {
        switch (fork())
        {
        case -1:
            perror("fork error");
            exit(1);
        case 0:
            /*akcja dla procesu potomnego*/
            for (j = 0; j < i; j++)
            {
                printf("\t");
            }
            printf("[%d]: ", i + 1);
            process_id();
            break;

        default:
            /*akcja dla procesu macierzystego*/
            wait(0);
            break;
        }
    }
    return 0;
}