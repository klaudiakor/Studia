/* autor: Klaudia Korczak
Problem Producent-Konsument */

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

void producer(char *, int *);
void consumer(char *, int *);

int main(int argc, char *argv[])
{
    /* argumenty wywolania:
        1) plik do odczytu
        2) plik do zapisu
    */
    if (argc != 3)
    { //zla ilosc argumentow
        printf("Zla ilosc argumentow!\n"
               "Prosze podac: ./Zad4.x (nazwa pliku do odczytu) (nazwa pliku do zapisu)\n");
        exit(1);
    }

    char *inFileName = argv[1];
    char *outFileName = argv[2];

    //tworzenie nienazwanego potoku
    int pipefd[2]; //deskryptor pliku
    if (pipe(pipefd) == -1)
    {
        perror("pipe error");
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
        producer(inFileName, pipefd);
        break;

    default:
        /* Proces macierzysty - KONSUMENT */
        consumer(outFileName, pipefd);
        wait(0);
        break;
    }
    return 0;
}

void producer(char *inFileName, int pipefd[2])
{
    //zamyka odczyt z potoku
    if (close(pipefd[0]) == -1)
    {
        perror("close() error");
        exit(4);
    }

    /*budowa sciezki do pliku wejsciowego (napis)*/
    size_t path_len = strlen(inFileName) + 3;
    char *path_in = (char *)malloc(path_len);
    strncat(path_in, "./", path_len);
    strncat(path_in, inFileName, path_len);

    // otwiera plik do czytania
    // 400 - wlasciciel prawo do odczytu
    int inFile = open(path_in, O_RDONLY, 400);
    if (inFile == -1)
    {
        perror("open() error");
        exit(5);
    }
    else
    {
        printf("otworzono plik %s\n", inFileName);
    }

    free(path_in); //zwalniam pamiec 
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
        if (write(pipefd[1], buf, read_resault) == -1)
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
    //zamykam zapis do potoku
    if (close(pipefd[1]) == -1)
    {
        perror("pipe close error");
        exit(11);
    }
}

void consumer(char *outFileName, int pipefd[2])
{
    // zamykam zapis do potoku
    if (close(pipefd[1]) == -1)
    {
        perror("pipe close error");
        exit(12);
    }

    //budowa sciezki do pliku wyjsciowego (napis)
    size_t path_len = strlen(outFileName) + 3;
    char *path = (char *)malloc(path_len);
    strncat(path, "./", path_len);
    strncat(path, outFileName, path_len);

    // otwiera plik do pisania (jesli nie istnieje to go tworzy, jak istnieje obcina go do 0)
    // 200 - wlasciciel prawo do zapisu
    int outFile = open(path, O_WRONLY | O_CREAT | O_TRUNC, 200);
    if (outFile == -1)
    {
        perror("file open error");
        exit(13);
    }
    else
    {
        printf("\nOtworzono plik %s\n", outFileName);
    }
    free(path); // zwalniam pamiec
    char buf[3];      //bufor do zapisu znakow odczytanych z potoku
    int read_resault; // przechowuje to co zwraca funkcja read
    srand(time(0));   // dla funkcji rand

    while ((read_resault = read(pipefd[0], buf, 3 * sizeof(char))) > 0)
    {

        // losowy czas uspienia
        sleep(rand() % 2);

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
    //zamykam odczyt z potoku
    if (close(pipefd[0]) == -1)
    {
        perror("pipe close error");
        exit(19);
    }
}