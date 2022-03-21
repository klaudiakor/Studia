.SUFFIXES: .c .cpp .o .x .h

DIR = `basename $(CURDIR)`

SRCA = Zad5A.c
OBJSA = $(SRCA:%.c=%.o) 
HEADSA = 
EXECA  = A.x
LIBSA  =  

SRCB = producent.c
OBJSB = $(SRCB:%.c=%.o) 
HEADSB = 
EXECB  = producent.x
LIBSB  = 

SRCC = konsument.c
OBJSC = $(SRCC:%.c=%.o) 
HEADSC = 
EXECC  = konsument.x
LIBSC  = 

 
CFLAGS = -Wall -std=c99 -pedantic -O -fPIC
LFLAGS = -Wall -std=c99 -pedantic -O
LDLIBS = -lm

CO = gcc
LD = $(CO)


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

.PHONY: runA
runA: $(EXECA)  
	./$(EXECA) $(ARGin) $(ARGout) $(ARGpipe)
	diff -s $(ARGin) $(ARGout)

.PHONY: runB
runB: $(EXECB) $(EXECC)
	mkfifo -m 644 $(ARGpipe)
	xterm -hold -title PRODUCENT -e ./$(EXECB) $(ARGin) $(ARGpipe) &
	xterm -hold -title KONSUMENT -e ./$(EXECC) $(ARGout) $(ARGpipe)
	diff -s $(ARGin) $(ARGout)
	rm $(ARGpipe)

.PHONY: clean
clean:                                                     
	rm -f *.o  *~ *.a *.so *.x core core* a.out

.PHONY: tar
tar: clean
	(cd ../; tar -cvzf $(DIR).tar.gz  $(DIR) )
