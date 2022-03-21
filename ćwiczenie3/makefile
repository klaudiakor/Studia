
.SUFFIXES: .c .cpp .o .x .h

DIR = `basename $(CURDIR)`

SRCA = Zad3a.c
OBJSA = $(SRCA:%.c=%.o) 
HEADSA = 
EXECA  = A.x
LIBSA  = 
HEADSA = 

SRCB = Zad3b.c
OBJSB = $(SRCB:%.c=%.o) 
HEADSB = 
EXECB  = B.x
LIBSB  = 
HEADSB = 

SRCC = Zad3c.c
OBJSC = $(SRCC:%.c=%.o) 
HEADSC = 
EXECC  = C.x
LIBSC  = 
HEADSC = 

CFLAGS = -Wall -std=c99 -pedantic -O -fPIC
LFLAGS = -Wall -std=c99 -pedantic -O
LDLIBS = -lm

CO = gcc
LD = $(CO)

AR = ar
ARFLAGS = rsv


%.o: %.c %.h
	$(CO) $(CFLAGS) -c $<
%.o: %.c
	$(CO) $(CFLAGS) -c $<

.PHONY: all
all: $(EXECA) $(EXECB) $(EXECC) 

$(EXECA): $(OBJSA) $(LIBSA) 
	$(LD) -o $@ $(LFLAGS) $^

$(EXECB): $(OBJSB) $(LIBSB) 
	$(LD) -o $@ $(LFLAGS) $^

$(EXECC): $(OBJSC) $(LIBSC) 
	$(LD) -o $@ $(LFLAGS) $^



.PHONY: clean
clean:                                                     
	rm -f *.o  *~ *.a *.so *.x core core* a.x; rm -rf ${LIB_DIR}

.PHONY: tar
tar: clean
	(cd ../; tar -cvzf $(DIR).tar.gz  $(DIR) )
