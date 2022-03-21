
.SUFFIXES: .c .cpp .o .x .h

DIR = `basename $(CURDIR)`

SRCA = Zad1a.c
OBJSA = $(SRCA:%.c=%.o) 
HEADSA = 
EXECA  = A.x
LIBSA  = 
HEADSA = 

SRCB = Zad1b.c
OBJSB = $(SRCB:%.c=%.o) 
HEADSB = 
EXECB  = B.x
LIBSB  = 
HEADSB = 

SRCC = Zad1c.c
OBJSC = $(SRCC:%.c=%.o) 
HEADSC = 
EXECC  = C.x
LIBSC  = 
HEADSC = 

SRCD = Zad1d.c
OBJSD = $(SRCD:%.c=%.o) 
HEADSD = 
EXECD = D.x
LIBSD  = 
HEADSD = 

SRCE = Zad1e.c
OBJSE = $(SRCE:%.c=%.o) 
HEADSE = 
EXECE  = E.x
LIBSE  = 
HEADSE = 


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
all: $(EXECA) $(EXECB) $(EXECC) $(EXECD) $(EXECE)

$(EXECA): $(OBJSA) $(LIBSA) 
	$(LD) -o $@ $(LFLAGS) $^

$(EXECB): $(OBJSB) $(LIBSB) 
	$(LD) -o $@ $(LFLAGS) $^

$(EXECC): $(OBJSC) $(LIBSC) 
	$(LD) -o $@ $(LFLAGS) $^

$(EXECD): $(OBJSD) $(LIBSD) 
	$(LD) -o $@ $(LFLAGS) $^

$(EXECE): $(OBJSE) $(LIBSE) 
	$(LD) -o $@ $(LFLAGS) $^

.PHONY: runA
runA: $(EXECA)
	./$(EXECA) 

.PHONY: runB
runB: $(EXECB)
	./$(EXECB)

.PHONY: runC
runC: $(EXECC)
	./$(EXECC)

.PHONY: runD
runD: $(EXECD)
	./$(EXECD)

.PHONY: runE
runE: $(EXECE)
	./$(EXECE)

.PHONY: clean
clean:                                                     
	rm -f *.o  *~ *.a *.so *.x core core* a.x; rm -rf ${LIB_DIR}

.PHONY: tar
tar: clean
	(cd ../; tar -cvzf $(DIR).tar.gz  $(DIR) )
