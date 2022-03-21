// biblioteka funkcji do obsługi kolejek komunikatów

#include "mq_lib.h"

mqd_t MQcreate(const char *name, int oflag, mode_t mode, struct mq_attr *attr)
{
    mqd_t resault;
    resault = mq_open(name, oflag, mode, attr);
    if (resault == (mqd_t)-1)
    {
        perror("MQcreate error");
        exit(1);
    }
    else
    {
        return resault;
    }
}

mqd_t MQopen(const char *name, int oflag)
{
    mqd_t resault;
    resault = mq_open(name, oflag);
    if (resault == -1)
    {
        perror("mq_open error");
        exit(2);
    }
    else
    {
        return resault;
    }
}

void MQclose(mqd_t mqdes)
{
    if (mq_close(mqdes) == -1)
    {
        perror("mq_close error");
        exit(3);
    }
    else
    {
        printf("Zamkniento kolejke komunikatow o deskryptorze %d\n", mqdes);
    }
}
void MQunlink(const char *name)
{
    if (mq_unlink(name) == -1)
    {
        perror("mq_unlink error");
        exit(4);
    }
    else
    {
        printf("Usuniento kolejke komunikatow o nazwie %s\n", name);
    }
}

void MQsend(mqd_t mqdes, const char *msg_ptr, size_t msg_len, unsigned int msg_prio)
{
    if (mq_send(mqdes, msg_ptr, msg_len, msg_prio) == -1)
    {
        perror("mq_send error");
        exit(7);
    }
}

int MQreceive(mqd_t mqdes, char *msg_ptr, size_t msg_len, unsigned int *msg_prio)
{
    int reasult = mq_receive(mqdes, msg_ptr, msg_len, msg_prio);
    if (reasult == -1)
    {
        perror("mq_receive error");
        exit(8);
    }
    else
    {
        return reasult;
    }
}