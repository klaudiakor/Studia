/* autor: Klaudia Korczak */
/* program z 1b, tak aby komunikaty procesow potomnych byly
wypisywane przez program uruchamiany przez funkcje exec. 
Nazwe programu do uruchomienia przekazywac przez argumenty programu procesu macierzystego.*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>


int main(int argc, char *argv[]) {

    /*niepoprawna ilosc argumentow*/
    if (argc != 2) {
        printf("Zla liczba argumentow");
    }

    /*budowa napisu dla sciezki do programu (dla exec)*/
    size_t path_len = strlen(argv[1]) + 3;
    char *path = (char*) malloc(path_len);
    strncat(path, "./", path_len);
    strncat(path, argv[1], path_len);

    /*wypisuje identyfikatory dla procesu macierzystego*/
    printf("[PROCES MACIERZYSTY]: ");
    printf("UID = %d, GID = %d, PID = %d, PPID = %d, PGID = %d\n",
           getuid(), getgid(), getpid(), getppid(), getpgrp());
    int i;
    for (i = 0; i < 3; i++)
    {
        switch (fork())
        {
        case -1:
            /* blad funkcji fork */
            perror("fork error");   
            exit(1);
        case 0:
            /* akcja dla procesu potomnego */
            execl(path, argv[1], NULL);
            perror("execl error");
            exit(2);
        default:
            /* akcja dla procesu macierzystego */
            if(wait(0) == -1) {
                /* blad funkcji wait */
                perror("wait error");
                exit(3);
            }
            break;
        }
    }

    free(path); /*zwalniam pamiec*/
    return 0;
}