CXX = g++
CXXFLAGS = -Wall -c -std=c++0x
EXE = Assembler

all: $(EXE)

$(EXE): main.o assembler.o assemblerStage.o
	$(CXX) main.o assembler.o assemblerStage.o -o $@

main.o: main.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

assembler.o: assembler.cpp
	$(CXX) $(CXXFLAGS) $< -o $@	

assemblerStage.o: assemblerStage.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

# Build our precompiled header first
# this is not running currently, need to figure out
stdafx.h.gch: stdafx.h
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm *.o && rm $(EXE)
