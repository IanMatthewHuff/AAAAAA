/*

Assembler

The Assembler class is the base class for all of our automated art assembly. 

Full documentation for this class and the relation to other classes is found in the Assembler-Overview text document
in the documents folder

*/

#include <string>

class Assembler
{
public:
	Assembler();
	~Assembler();	

	std::string GetTestString();
};