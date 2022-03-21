/* autor: Klaudia Korczak
(5A) Problem Producenta i konsumenta
przy pomocy potokow nazwanych */

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

char *pipeName;
void producer(char *, char *);
void consumer(char *, char *);
void close_pipe();

int main(int argc, char *argv[])
{
    /* argumenty wywolania:
        1) plik do odczytu
        2) plik do zapisu
        3) potok nazwany
    */
    if (argc != 4) 
    { //zla ilosc argumentow
        printf("Zla ilosc argumentow!\n"
            "Prosze podac: plik do odczytu, zapisu, potok\n");
        exit(1);
    }

    char *inFileName = argv[1];
    char *outFileName = argv[2];
    pipeName = argv[3];

    //tworzenie nazwanego potoku
    if (mkfifo(pipeName, 0777) == -1)
    {
        perror("mkfifo error");
        exit(1);
    }


    //obsluga ctrl-C
    //usunie potok w przypadku przerwania
    if (signal(SIGINT, close_pipe) == SIG_ERR) {
        perror("signal error");
        exit(2);
    }

    //podzial procesu
    switch (fork())
    {
    case -1:
        perror("fork error");
        exit(3);
    case 0:
        /* Proces potomny - PRODUCENT */
        producer(inFileName, pipeName);
        break;

    default:
        /* Proces macierzysty - KONSUMENT */
        consumer(outFileName, pipeName);
        wait(0);
        break;
    }
    //usuniencie potoku przy wyjsciu z programu
    if(atexit(close_pipe) != 0) {
        perror("atexit error");
        exit(1);
    }
    
    return 0;
}
//usuwa potok
void close_pipe() {
    unlink(pipeName);
}


void producer(char *inFileName, char *pipeName)
{
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
}

void consumer (char *outFileName, char *pipeName) {
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
}
