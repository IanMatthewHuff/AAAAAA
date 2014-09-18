// Library includes
#include <iostream>

// My includes
#include "assembler.h"

int main(int argc, char **argv)
{
	// Check that we are building right
	std::cout << "App Runs" << std::endl;

	// Check that we can load our Assembler
	Assembler myAssembler;
	std::cout << myAssembler.GetTestString() << std::endl;

	return 0;
}