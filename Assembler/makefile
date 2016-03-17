CXX = g++
CXXFLAGS = -Wall -c -std=c++0x
EXE = Assembler

all: $(EXE)

$(EXE): main.o assembler.o assemblerStage.o
	$(CXX) main.o assembler.o assemblerStage.o -o $@

main.o: main.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

assembler.o: assembler.cpp assembler.h stdafx.h.gch
	$(CXX) $(CXXFLAGS) $< -o $@	

assemblerStage.o: assemblerStage.cpp assemblerStage.h stdafx.h.gch
	$(CXX) $(CXXFLAGS) $< -o $@

# Build our precompiled header first
# this is not running currently, need to figure out
stdafx.h.gch: stdafx.h
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm *.o && rm $(EXE)
