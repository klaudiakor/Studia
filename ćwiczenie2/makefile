
.SUFFIXES: .c .cpp .o .x .h

DIR = `basename $(CURDIR)`

SRCA = Zad2.c 
OBJSA = $(SRCA:%.c=%.o) 
HEADSA = 
EXECA  = Zad2.x
LIBSA  = 
HEADSA = 

SRCB = process_id.c
OBJSB = $(SRCB:%.c=%.o) 
HEADSB = 
EXECB  = process_id.x
LIBSB  = 
HEADSB = 


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
all: $(EXECA) $(EXECB) 

$(EXECA): $(OBJSA) $(LIBSA) 
	$(LD) -o $@ $(LFLAGS) $^

$(EXECB): $(OBJSB) $(LIBSB) 
	$(LD) -o $@ $(LFLAGS) $^


.PHONY: run2
run2: $(EXECA) $(EXECB)
	./$(EXECA) $(EXECB)


.PHONY: clean
clean:                                                     
	rm -f *.o  *~ *.a *.so *.x core core* a.x; rm -rf ${LIB_DIR}

.PHONY: tar
tar: clean
	(cd ../; tar -cvzf $(DIR).tar.gz  $(DIR) )
