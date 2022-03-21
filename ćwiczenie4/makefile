
.SUFFIXES: .c .cpp .o .x .h

DIR = `basename $(CURDIR)`

SRCA = Zad4.c
OBJSA = $(SRCA:%.c=%.o) 
HEADSA = 
EXECA  = Zad4.x
LIBSA  = 
HEADSA = 


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
all: $(EXECA)  

$(EXECA): $(OBJSA) $(LIBSA) 
	$(LD) -o $@ $(LFLAGS) $^


.PHONY: run
run: $(EXECA) 
	./$(EXECA) $(ARGin) $(ARGout)
	diff -s $(ARGin) $(ARGout)

.PHONY: clean
clean:                                                     
	rm -f *.o  *~ *.a *.so *.x core core* a.x; rm -rf ${LIB_DIR}

.PHONY: tar
tar: clean
	(cd ../; tar -cvzf $(DIR).tar.gz  $(DIR) )
