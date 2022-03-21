/*grupowanie pokoleniami*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int process_id() {
    printf("UID = %d, GID = %d, PID = %d, PPID = %d, PGID = %d\n",
        getuid(), getgid(), getpid(), getppid(), getpgrp());
    return 0;
}

int main() {
    int i,j;
    int fork_status;
    printf("\n[PROCES MACIERZYSTY]: ");
    process_id(); /*wypisuje id dla procesu macierzystego*/

    for(i=0;i<3;i++) {
        fork_status = fork();
        sleep(1);
        switch (fork_status)
        {
        case -1:
            perror("fork error");
            exit(1);
        case 0:
            /*akcja dla procesu potomnego*/
            for(j = 0; j < i; j++) {
                printf("\t");
            }
            printf("[%d]: ",i+1);
            process_id();
            break;
        
        default:
            /*akcja dla procesu macierzystego*/
            break;
        }
    }
    return 0;
}