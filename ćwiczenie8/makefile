
.SUFFIXES: .c .cpp .o .x .h

DIR = `basename $(CURDIR)`

LIB_NAME = MessageQueueFunctions
LIB_DIR = mq_lib
# Biblioteka statyczna
LIB_STAT = lib$(LIB_NAME).a
LIB_OBJS = mq_lib.o
LIB_HEAD = mq_lib.h

SRCA = serwer.c
OBJSA = $(SRCA:%.c=%.o) 
HEADSA = 
EXECA  = serwer.x
LIBSA  = $(LIB_DIR)/$(LIB_STAT)
HEADSA = $(LIB_HEAD)

SRCB = klient.c
OBJSB = $(SRCB:%.c=%.o) 
HEADSB = 
EXECB  = klient.x
LIBSB  = $(LIB_DIR)/$(LIB_STAT)
HEADSB = $(LIB_HEAD)


CFLAGS = -Wall -std=c99 -pedantic -O -fPIC
LFLAGS = -Wall -std=c99 -pedantic -O 
LDLIBS = -lm -lrt

CO = gcc
LD = $(CO)

AR = ar
ARFLAGS = rsv

$(LIB_OBJSA): $(LIB_HEAD)

%.o: %.c %.h
	$(CO) $(CFLAGS) -c $<
%.o: %.c
	$(CO) $(CFLAGS) -c $<

	

.PHONY: all
all: $(EXECA) $(EXECB) 


$(LIB_STAT): $(LIB_OBJS)
	$(AR) $(ARFLAGS) $@ $?
	mkdir -p $(LIB_DIR)
	mv $(LIB_STAT) $(LIB_DIR)

$(EXECA): $(OBJSA) $(LIB_STAT) 
	$(LD) -o $@ $(LFLAGS) $(OBJSA) -L $(LIB_DIR) -l $(LIB_NAME) $(LDLIBS) 

$(EXECB): $(OBJSB) $(LIB_STAT) 
	$(LD) -o $@ $(LFLAGS) $(OBJSB) -L $(LIB_DIR) -l $(LIB_NAME) $(LDLIBS)

.PHONY: run
run: $(EXECA) $(EXECB)
	xterm -hold -title SERWER -bg lightgreen -e ./$(EXECA) &
	xterm -hold -title KLIENT1 -bg lightblue -e ./$(EXECB) &
	xterm -hold -title KLIENT2 -bg lightblue -e ./$(EXECB) &
	xterm -hold -title KLIENT3 -bg lightblue -e ./$(EXECB) &

.PHONY: clean
clean:                                                     
	rm -f *.o  *~ *.a *.so *.x core core* a.x; rm -rf ${LIB_DIR}

.PHONY: tar
tar: clean
	(cd ../; tar -cvzf $(DIR).tar.gz  $(DIR))
