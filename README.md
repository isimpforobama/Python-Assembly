Tutorial Video https://youtu.be/8VG2NYoaTHw

When opening main.py for the first time, ensure filepath.db doesn't exist. Then, when prompted, paste the filepath for input.txt by left-right clicking on the file and selecting 'Copy as Path'. 
Open main.py again, press CTRL + V to paste the filepath (remove any surrounding commas). Subsequently, you won't need to repeat this unless the folder is relocated.

# Language Syntax.
# ADD - Takes three inputs A B C it Adds A and B together and puts the sum into the address of C
# SUB - Same as ADD but subtracts the two Memory Location Values
# MUL - Same as ADD but multiplies the two Memory Location Values
# DIV - Same as ADD but divides the two Memory Location Values
# JUMP - Takes a Input A and jumps to that line in the code
# JEQ - Takes Three inputs A B C if A and B are Equal it will jump to the line C in the code
# JNE - Takes Three inputs A B C if A and B are Not Equal it will jump to the line C in the code
# JLT - Takes Three inputs A B C if A is less than B it will jump to the line C in the code
# JGT - Takes Three inputs A B C if A is Greater than B it will jump to the line C in the code
# BIZ - Takes one input A if the last math operation resulted in zero it will Jump to the line A in the code
# LOAD - Takes Two Inputs A and B It Stores the Value of B into the Address of A
# STORE - Takes 2 Inputs A and B and Copys the value of A at the Address of a and Pastes it at the Address of B
# PRINT - Takes a string as input which can be a combination of literal strings and memory location references. Literal strings are printed as is, while memory 
#     - location references (enclosed in '{' and '}') are replaced with the value stored in the corresponding memory location. 
#     - If multiple strings are to be printed, they can be concatenated using the '+' operator. 
#     - When Calling Variables in the PRINT Operation, the variable must be enclosed in curly braces and not have any Spaces.
#     - Example: "PRINT +Current Number is +{0}" will print "Current Number is 10" if the value of the Memory Location 0 is 10.
#     - It also supports newline characters such as "\n", Here is a Example
#     - "PRINT +\n" or "PRINT +Your Number +\n+{0}" Will print 
#       Your Number
#       10
#     - The final string is then printed to the console.
# HALT - Stops the Program
# NOP - No Operation
# SLP - Sleeps for a certain amount of time in Milliseconds

Error Supported Functions
# BIZ, JGT, JLT, JNE, JEQ, JUMP

# Common issues
One common issues is when Using the PRINT Statement and getting an error when calling it, For example
"PRINT {0}" is incorrect Because There needs to be a + at the start after the first space of the PRINT Statement For example
"PRINT +{0}" is the Corrected Version
Another PRINT Statement issues is the following
"PRINT +Your Number is+ {0}" is incorrect Because There Cannot be a space between a + and a Variable Call
"PRINT +Your Number is +{0}" is the Corrected Version



there is already a test script inside of input.txt. it simply counts from 1 to 100 and when it reaches 100 it exits the program.
