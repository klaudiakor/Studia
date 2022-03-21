#ifndef LIB_H
#define LIB_H

#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>

int open_shared_memory (const char* name, int flags, mode_t mode);
void set_len (int fd, off_t length);
void close_shered_memory (int fd);

#endif