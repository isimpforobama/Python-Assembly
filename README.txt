Tutorial Video https://youtu.be/8VG2NYoaTHw

When opening main.py for the first time, ensure filepath.db doesn't exist. Then, when prompted, paste the filepath for input.txt by left-right clicking on the file and selecting 'Copy as Path'. 
Open main.py again, press CTRL + V to paste the filepath (remove any surrounding commas). Subsequently, you won't need to repeat this unless the folder is relocated.

# Language Syntax.
# ADD - Takes a input of 2 Memory Locations and stores the sum of the two Memory Location Values a into a third Memory Location
# SUB - Same as ADD but subtracts the two Memory Location Values
# MUL - Same as ADD but multiplies the two Memory Location Values
# DIV - Same as ADD but divides the two Memory Location Values
# JEQ - Takes a input Number and jumps to that line Number in the code if the two Memory Locations are equal
# JMP - Takes a input Number and jumps to that line Number in the code
# JNE - Takes a input Number and jumps to that line Number in the code if the two Memory Locations are not equal
# JLT - Takes a input Number and jumps to that line Number in the code if the first Memory Location is less than the second Memory Location
# JGT - Takes a input Number and jumps to that line Number in the code if the first Memory Location is greater than the second Memory Location
# BIZ - Takes 1 input Number and jumps to that line Number in the code if the last ADD or the last SUB or the last MUL or the last DIV operation equals 0
# LOD - Takes 2 Inputs A and B and stores the value of the Input B into the Memory Location A
# STR - Takes 2 Inputs A and B and stores the value of the Memory Location B into the Memory Location A
# PRT - Takes a string as input which can be a combination of literal strings and memory location references. Literal strings are printed as is, while memory 
#     - location references (enclosed in '{' and '}') are replaced with the value stored in the corresponding memory location. 
#     - If multiple strings are to be printed, they can be concatenated using the '+' operator. 
#     - When Calling Variables in the PRT Operation, the variable must be enclosed in curly braces and not have any Spaces.
#     - Example: "PRT +Current Number is +{0}" will print "Current Number is 10" if the value of the Memory Location 0 is 10.
#     - The final string is then printed to the console.
# HLT - Stops the Program
# NOP - No Operation
# SLP - Sleeps for a certain amount of time in Milliseconds


# Common issues
One common issues is when Using the PRT Statement and getting an error when calling it, For example
"PRT {0}" is incorrect Because There needs to be a + at the start after the first space of the PRT Statement For example
"PRT +{0}" is the Corrected Version
Another PRT Statement issues is the following
"PRT +Your Number is+ {0}" is incorrect Because There Cannot be a space between a + and a Variable Call
"PRT +Your Number is+{0}" is the Corrected Version



there is already a test script inside of input.txt. it simply counts from 1 to 100 and when it reaches 100 it exits the program.