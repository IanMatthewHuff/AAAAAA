CXX = g++
CXXFLAGS = -Wall -c -std=c++0x
EXE = Assembler

all: $(EXE)

$(EXE): Assembler.o
	$(CXX) $< $(LDFLAGS) -o $@

Assembler.o: main.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm *.o && rm $(EXE)