#include "shm_lib.h"

//tworzy i otwiera lub otwiera istniejacy obiekt pamieci dzielonej
int open_shared_memory (const char* name, int flags, mode_t mode) {
    int open_resault = shm_open(name, flags, mode);
    if (open_resault == -1) {
        perror("shm_open error");
        exit(1);
    }
    return open_resault; // deskryptor obiektu
}

//ustawia dlugosc obiektu pamieci dzielonej
void set_len (int fd, off_t length) {
    if (ftruncate(fd, length) == -1) {
        perror("ftruncate error");
        exit(2);
    }
}

//zamykanie obiektu pamieci dzielonej
void close_shered_memory (int fd) {
    if(close(fd) == -1){
        perror("close error");
        exit(3);
    }
}
