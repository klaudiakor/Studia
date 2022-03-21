//autor: Klaudia Korczak
//KONSUMENT

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

int main (int argc, char *argv[])
{
    if(argc != 3){
        printf("Zla ilosc argumentow!\n");
        exit(1);
    }
    char *outFileName = argv[1]; //nazwa pliku do pisania
    char* pipeName = argv[2]; //nazwa potoku


    //otwiera potok do odczytu
    int pipe_fd = open(pipeName, O_RDONLY);
    if (pipe_fd == -1)
    {
        perror("open error");
        exit(6);
    }
    //otwiera plik do zapisu
    int outFile = open(outFileName, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (outFile == -1)
    {
        perror("file open error");
        exit(13);
    }
    else
    {
        if (write(1,"otworzono plik do zapisu\n",26) == -1) {
            perror("write error");
            exit(1);
        }
    }
    char buf[3];      //bufor do zapisu znakow odczytanych z potoku
    int read_resault; // przechowuje to co zwraca funkcja read
    srand(time(0));   // dla funkcji rand

    while ((read_resault = read(pipe_fd, buf, 3 * sizeof(char))) > 0)
    {

        // losowy czas uspienia
        sleep(rand() % 3);

        if ((read_resault) == -1)
        {
            perror("read error");
            exit(14);
        }
        //komunikaty
        if (write(STDOUT_FILENO, "\n[KONSUMENT]: ", 15) == -1)
        {
            perror("write error");
            exit(15);
        }
        // wypisuje na ekran
        if (write(STDOUT_FILENO, buf, read_resault) == -1)
        {
            perror("write error");
            exit(16);
        }
        // zapis do pliku wy
        if (write(outFile, buf, read_resault) == -1)
        {
            perror("write (to file) error");
            exit(17);
        }
    }

    //zamykam plik wy
    if (close(outFile) == -1)
    {
        perror("file close error");
        exit(18);
    }
    //zamykam potok
    if (close(pipe_fd) == -1)
    {
        perror("pipe close error");
        exit(19);
    }
    printf("\nZakonczono pobieranie.\n");
    return 0;
}
