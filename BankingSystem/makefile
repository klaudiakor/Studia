CC         := g++-10
CFLAGS     := -c -std=c++2a -Wpedantic
SRC 	   := $(wildcard src/*.cpp) \
			  $(wildcard src/*/*.cpp) \
			  $(wildcard src/*/*/*.cpp)
INC_DIR    := -Isrc -Ilibraries
OBJ_DIR    := obj
OBJECTS    := $(SRC:%.cpp=$(OBJ_DIR)/%.o)
EXE_NAME   := bank
OUT_FOLDER := out
EXECUTABLE := $(OUT_FOLDER)/$(EXE_NAME)

.PHONY: all
all: clean $(EXECUTABLE)

.PHONY: run
run: $(EXECUTABLE)
	cd $(OUT_FOLDER) ; ./$(EXE_NAME)
	
.PHONY: clean
clean:
	-rm -f -r $(OBJ_DIR)/*
	-rm -f -r $(EXECUTABLE)
 
$(OUT_FOLDER):
	mkdir -p $@

#link into exe
$(EXECUTABLE): $(OUT_FOLDER) $(OBJECTS)
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@

#compile
$(OBJ_DIR)/%.o: %.cpp
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@
	