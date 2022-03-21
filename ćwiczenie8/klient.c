// Proces klient
/* 
1. utworzy kolejke komunikatow w trybie do odbierania o nazwie /PID (sprintf)
2. otwiera kolejke serwera w trybie do nadawania komunikatow 
3. w petli  wczytuje z klawiatury zadane dzialanie (fgets)
4. tworzy komunikat umieszczajac na poczatku swoj PID, a po nim wczytane wyrazenie (sprintf)
5. wysyla taki komunikat do kolejki serwera
// petle mozna zakonczyc EOF (ctrl D) -
6. po czym klient powinien zamknac i usunac wlasna kolejke 
7. zamknac kolejke serwera
*/

#include "mq_lib.h"
#include "config.h"

#include <unistd.h> //getpid(), sleep()
#include <signal.h>
#include <time.h>

mqd_t c_mqdes;
mqd_t s_mqdes;

char ClientMQ[15];

void rm_fun()
{
    //zamkniecie i usuniencie wlasnej kolejki
    MQclose(c_mqdes);
    MQunlink(ClientMQ);
    MQclose(s_mqdes);
    _exit(1);
}

int main()
{
    sleep(5); // chce miec pewnosc ze pierwsze otworzy sie kolejka serwera
              // (xterm nie zawsze otwiera okienka w dobrej kolejnosci)
    struct mq_attr attr;
    attr.mq_flags = 0;            // tryb blokujacy
    attr.mq_maxmsg = 10;          // max liczba komunikatow w kolejce
    attr.mq_msgsize = N_MAX + 15; // max rozmiar komunikatu w kolejce
    attr.mq_curmsgs = 0;          // liczba komunikatow aktualnie w kolejce

    // nazwa kolejki klienta /PID
    int PID = getpid();
    sprintf(ClientMQ, "/%d", PID);

    // otwiera kolejke w trybie do odbierania
    c_mqdes = MQcreate(ClientMQ, O_RDONLY | O_CREAT | O_TRUNC, 0644, &attr);
    // wypisuje nazwe, deskryptor i atrybuty kolejki
    printf("Utworzono kolejke %s o deskryptorze %d\n"
           "atrybuty:\n"
           "\tflagi: %ld\n"
           "\tmax liczba komunikatow: %ld\n"
           "\tmax rozmiar komunikatu: %ld\n"
           "\tliczba komunikatow aktualnie w kolejce: %ld\n",
           ClientMQ, c_mqdes, attr.mq_flags, attr.mq_maxmsg, attr.mq_msgsize, attr.mq_curmsgs);

    // otwiera kolejke serwera w trybie do nadawania komunikatow
    s_mqdes = MQopen(ServerMQ, O_WRONLY);

    //obsluga przerwania
    if (signal(SIGINT, rm_fun) == SIG_ERR)
    {
        perror("signal error");
        exit(1);
    }
    // przy zakonczeniu programu zakmknie i usunie kolejke
    if (atexit(rm_fun) != 0)
    {
        perror("atexit error");
        exit(2);
    }

    char buf[N_MAX];
    char message[N_MAX + 15];
    char *fgets_resault;
    char resault[N_MAX];
    srand(time(NULL));
    while (1)
    {
        //wczytywanie dzialania
        printf("Prosze podac dzialanie: ");
        fgets_resault = fgets(buf, N_MAX, stdin);
        if (fgets_resault == NULL)
        {
            //Ctrl D
            printf("Przerwanie\n");
            break;
        }
        // tworzenie komunikatu
        sprintf(message, "%d %s", PID, buf);
        // wysylanie komunikatu do kolejki serwera
        MQsend(s_mqdes, message, sizeof(message), 1);

        sleep((rand() % 3));

        //odbieranie komunikatu z wynikiem (z wlasnej kolejki)
        if (MQreceive(c_mqdes, resault, N_MAX + 15, NULL) >= 0)
        {
            printf("[WYNIK]: %s\n", resault);
        }
    }

    return 0;
}