.PHONY: all

SOURCES := $(wildcard *.txt)
OBJECTS  := $(patsubst %.txt, %.csv, $(SOURCES))

all: $(OBJECTS)

%.csv : %.txt
	./makeCsvs.py $<
