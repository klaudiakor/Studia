.SUFFIXES: .c .cpp .o .x .h

DIR = `basename $(CURDIR)`

SRCA = zad9.c
OBJSA = $(SRCA:%.c=%.o) 
HEADSA = 
EXECA  = zad9.x
LIBSA  =  

CFLAGS = -Wall -std=c99 -pedantic -O -fPIC
LFLAGS = -Wall -std=c99 -pedantic -O -lpthread
LDLIBS = -lm

CO = gcc
LD = $(CO)


%.o: %.c %.h
	$(CO) $(CFLAGS) -c $<
%.o: %.c
	$(CO) $(CFLAGS) -c $<

.PHONY: all
all: $(EXECA) 

$(EXECA): $(OBJSA) $(LIBSA) 
	$(LD) -o $@ $(LFLAGS) $^

.PHONY: run
runA: $(EXECA)
	./$(EXECA) 

.PHONY: clean
clean:                                                     
	rm -f *.o  *~ *.a *.so *.x core core* a.out

.PHONY: tar
tar: clean
	(cd ../; tar -cvzf $(DIR).tar.gz  $(DIR) )
