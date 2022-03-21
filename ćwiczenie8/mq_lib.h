#ifndef LIB_H
#define LIB_H

#include <fcntl.h>
#include <sys/stat.h>
#include <mqueue.h>
#include <stdlib.h>
#include <stdio.h>

mqd_t MQcreate(const char *name, int oflag, mode_t mode, struct mq_attr *attr);
mqd_t MQopen(const char *name, int oflag);
void MQclose(mqd_t mqdes);
void MQunlink(const char *name);
void MQsend(mqd_t mqdes, const char *msg_ptr, size_t msg_len, unsigned int msg_prio);
int MQreceive(mqd_t mqdes, char *msg_ptr, size_t msg_len, unsigned int *msg_prio);

#endif