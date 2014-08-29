CXX = g++
CXXFLAGS = -Wall -c -std=c++0x
EXE = Assembler

all: $(EXE)

$(EXE): main.o assembler.o
	$(CXX) main.o assembler.o -o $@

main.o: main.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

assembler.o: assembler.cpp
	$(CXX) $(CXXFLAGS) $< -o $@	

clean:
	rm *.o && rm $(EXE)