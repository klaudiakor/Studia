//autor: Klaudia Korczak
//PRODUCENT

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <sys/param.h>
#include <sys/stat.h> /*open*/
#include <fcntl.h>    /*open*/
#include <sys/types.h>
#include <unistd.h> /*read*/
#include <sys/wait.h>
#include <string.h>
#include <time.h>

int main(int argc, char *argv[])
{
    if(argc != 3){
        printf("Zla ilosc argumentow!\n");
        exit(1);
    }
    char *inFileName = argv[1]; //nazwa pliku do czytania
    char *pipeName = argv[2]; //nazwa potoku

    // otwiera plik do czytania
    // 400 - wlasciciel prawo do odczytu
    int inFile = open(inFileName, O_RDONLY, 400);
    if (inFile == -1)
    {
        perror("open() error");
        exit(5);
    }
    else
    {
        if(write(1,"otworzono plik do odczytu\n",27) == -1) {
            perror("write error");
            exit(1);
        }
    }

    //otwiera potok do pisania
    int pipe_fd = open(pipeName, O_WRONLY); 
    if (pipe_fd == -1)
    {
        perror("open error");
        exit(6);
    }

    char buf[3];      // bufor do wczytywania znakow
    int read_resault; // to co zwraca funkcja read
    srand(time(0));   // dla funkcji rand

    //wykonuje sie dopoki jest cos w pliku
    while ((read_resault = read(inFile, buf, 3 * sizeof(char))) > 0)
    {

        sleep(rand() % 3); //losowy czas uspienia

        if (read_resault == -1)
        {
            perror("read error");
            exit(6);
        }

        //komunikaty
        if (write(STDOUT_FILENO, "\n[PRODUCENT]: ", 15) == -1)
        {
            perror("write error");
            exit(7);
        }

        // wypisuje na ekran co przesyla
        if (write(STDOUT_FILENO, buf, read_resault) == -1)
        {
            perror("write error");
            exit(8);
        }
        // przesylam do potoku
        if (write(pipe_fd, buf, read_resault) == -1)
        {
            perror("write error");
            exit(9);
        }
    }

    //zamykam plik we
    if (close(inFile) == -1)
    {
        perror("file close error");
        exit(10);
    }
    //zamykam potok
    if (close(pipe_fd) == -1)
    {
        perror("close error");
        exit(11);
    }
    printf("\nZakonczono wysylanie.\n");
    return 0;
}

