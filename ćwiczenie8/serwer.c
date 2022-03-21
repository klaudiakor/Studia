//Proces serwer
/* 
1. otwiera kolejke komunikatow w trybie do odbierania
(o nazwie zdefiniowanej we wpolnym pliku naglowkowym)
2. dziala w petli nieskonczonej - demon
  probujac odbierac komunikaty ze swojej kolejki
3. po odebraniu komunikatu:
    czyta pid klienta (atoi)
    otwiera kolejke klienta w trybie do nadawania komunikatow (o nazwie /PID) (sprintf)
    z komunikatu odczytuje odpowiednie dzialanie (sscanf)
    wykonuje je
    odsyla wynik w komunikacie (sprintf) do kolejki klienta
    zamyka kolejke

// proces mozna zakonczyc SIGINIT (ctrl c) - obsluga 
    zamkniecie i usuniencie wlasnej kolejki

*/

#include "mq_lib.h"
#include "config.h"
#include <signal.h>
#include <unistd.h> // sleep()
#include <time.h>

mqd_t s_mqdes;

void rm_fun()
{
    //zamkniecie i usuniencie wlasnej kolejki
    MQclose(s_mqdes);
    MQunlink(ServerMQ);
    _exit(1);
}
int main()
{
    // struktura atrybutow kolejki
    struct mq_attr attr;
    attr.mq_flags = 0;            // tryb blokujacy
    attr.mq_maxmsg = 10;          // max liczba komunikatow w kolejce
    attr.mq_msgsize = N_MAX + 15; // max rozmiar komunikatu w kolejce
    attr.mq_curmsgs = 0;          // liczba komunikatow aktualnie w kolejce

    printf("%s\n", ServerMQ);

    // otwieram kolejke serwera w trybie do odbierania
    s_mqdes = MQcreate(ServerMQ, O_CREAT | O_RDONLY, 0644, &attr);
    // wypisuje wiadomoci o kolejce
    printf("Utworzono kolejke %s o deskryptorze %d\n"
           "atrybuty:\n"
           "\tflagi: %ld\n"
           "\tmax liczba komunikatow: %ld\n"
           "\tmax rozmiar komunikatu: %ld\n"
           "\tliczba komunikatow aktualnie w kolejce: %ld\n",
           ServerMQ, s_mqdes, attr.mq_flags, attr.mq_maxmsg, attr.mq_msgsize, attr.mq_curmsgs);

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

    //bufor do umieszczenia komunikatu
    char message[N_MAX];
    int message_len;
    int ClientPID;
    char ClientMQ_name[15];
    double num1;
    double num2;
    char operator;
    double resault;
    int c_mqdes;
    char message_to_send[N_MAX];
    srand(time(NULL));

    while (1)
    { //proces demon
        //probuje odebrac komunikaty z kolejki
        message_len = MQreceive(s_mqdes, message, N_MAX + sizeof(ClientMQ_name), NULL);
        if (message_len > 0)
        {
            ClientPID = atoi(message);
            printf("[KOMUNIKAT]: %s", message);

            // otwiera kolejke klienta w trybie do nadawania komunikatow o nazwie /PID
            sprintf(ClientMQ_name, "/%d", ClientPID);
            printf("\t[KLIENT]: %s\n", ClientMQ_name);
            c_mqdes = MQopen(ClientMQ_name, O_WRONLY);

            // z komunikatu odczytuje wartosci
            if (sscanf(message, "%d %lg %c %lg", &ClientPID, &num1, &operator, & num2) == -1)
            {
                printf("sscanf error\n");
                exit(3);
            }

            sleep(rand() % 3);

            //wykonanie operacji
            if (operator== 43)
            { // + dodawanie
                resault = num1 + num2;
            }
            else if (operator== 45)
            { // - odejmowanie
                resault = num1 - num2;
            }
            else if (operator== 42)
            { // * mnozenie
                resault = num1 * num2;
            }
            else if (operator== 47)
            { // / dzielenie
                resault = num1 / num2;
            }
            else
            {
                printf("Bad operator\n");
                exit(4);
            }

            printf("\t[WYNIK]: %lg\n", resault);
            sprintf(message_to_send, "%lg", resault);

            //odsyla wynik do klienta
            MQsend(c_mqdes, message_to_send, sizeof(message_to_send), 1);
            // zamyka kolejke klienta
            MQclose(c_mqdes);
        }
    }

    return 0;
}
