/* 1.a wypisuje identyfikatory dla danego procesu. */

#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main () {
    printf(" UID = %d\n GID = %d\n PID = %d\n PPID = %d\n PGID = %d\n",
        getuid(), getgid(), getpid(), getppid(), getpgrp()); 

    return 0;
}