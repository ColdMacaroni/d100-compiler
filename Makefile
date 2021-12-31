BIN=base
SRC=main.c

CC=clang
CC_FLAGS=-Wall -O3


all:
	$(CC) $(CC_FLAGS) $(SRC) -o $(BIN)
