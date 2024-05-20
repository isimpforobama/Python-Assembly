Tutorial Video https://youtu.be/8VG2NYoaTHw

# Language Syntax.
# ADD     - Takes three inputs A, B, C it Adds A and B together and puts the sum into the address of C
# SUB     - Same as ADD but subtracts the two Memory Location Values
# MUL     - Same as ADD but multiplies the two Memory Location Values
# DIV     - Same as ADD but divides the two Memory Location Values
# JUMP    - Takes a Input A and jumps to that line in the code
# JEQ     - Takes Three inputs A, B, C if A and B are Equal it will jump to the line C in the code
# JNE     - Takes Three inputs A, B, C if A and B are Not Equal it will jump to the line C in the code
# JLT     - Takes Three inputs A, B, C if A is less than B it will jump to the line C in the code
# JGT     - Takes Three inputs A, B, C if A is Greater than B it will jump to the line C in the code
# BIZ     - Takes one input A if the last math operation resulted in zero it will Jump to the line A in the code
# LOAD    - Takes Two Inputs A and B It Stores the Value of B into the Address of A
# STORE   - Takes 2 Inputs A and B and Copys the value of A at the Address of a and Pastes it at the Address of B
# PRINT   - Works Differently than the default Python printfunction Furthur Documentation is below.
# HALT    - Stops the Program
# NOP     - No Operation
# SLEEP   - Takes One Input A and Stops the program from running for that time in milliseconds
# CLS     - Clears the Terminal of any text past or present
# POINTER - Pointers are Very useful when needing readability inside of your code
# :marker - Makers are Extremely useful when making loops inside of your code



# PRINT Syntax
For these examples 0 will be assigned with a value of 10 and X will be assigned with 0's Value(10)
Printing a Word
- PRINT +Hello World!
# Output: Hello World!

# Printing a Address
- PRINT +{0}
Output: 10

# Printing a Word and a Address
- PRINT +Count is: +{0}
Output: Count is: 10

# Printing a Pointer
- PRINT +{X}
Output: 10

# Printing using \n
- PRINT +Hello+\n+World!
Output: Hello
        World



# POINTER Syntax
For these examples we will Assign no inital values
# Assigning a Pointer
- POINTER (0 = X)
Output: 

# Assigning a Pointer and printing it out
- POINTER (0 = X)
- PRINT +{X}
Output: 0

# Assigning multiple Pointers
- POINTER (0 = X)
- POINTER (1 = Y)
- POINTER (2 = SUM)
# Output: 0
These above Pointers Reference Memory address's
Whenever you call upon a memory Address in Python Assembly,
you can call a Pointer if it's assigned to that memory address



# LOAD Syntax And Printing
Loading a Value into a Address
- LOAD 0 10
Output:
#henever you Load a value into something in Python Assembly make sure you call the address first 
then give it the value you want
# Printing a Loaded Value
- LOAD 0 100
- PRINT +{0}
# Output: 100

# Printing a Loaded Value
- LOAD 0 1000000
- PRINT +{0}
Output: 1000000
# Printing a Loaded Value
- LOAD 1 10
- PRINT +{1}
Output: 10
# Printing a Loaded Value
- LOAD 0 10
- LOAD 1 20
- PRINT +{0}
Output: 10

Adding Numbers together with ADD

- Basic ADD operation
-
LOAD 0 10
LOAD 1 20
ADD 0 1 2
PRINT +{2}
-
Output: 30

Add takes three inputs, the first two are A and B both of which can take a Memory Address or a Pointer
the Third input C is the Outputed Memory address OR pointer that of which is the Sum of a + b
c = a + b
2 = 0 + 1

- ADD Operation with Pointers
-
LOAD 0 10
LOAD 1 20

POINTER (0 = First_Number)
POINTER (1 = Second_Number)
POINTER (2 = SUM)

ADD First_Number Second_Number SUM

PRINT +{SUM}
-
Output: 30

This is why Pointers are so Useful it's because they are Very Capable of calling your memory Address's with Ease



JUMP Syntax and Common Errors with Markers

for This demonstration im going to announce the theoretical line number that you will have when you
are coding this inside your input.txt file.

- Basic JUMP Operation
-
Ln 1 PRINT +Hello World
Ln 2 JUMP 1
-
Output: Hello World (Forever)
the Jump operation is pretty self explanitory. it simply takes a number OR a marker
and runs that line of Code in the file and continues normal how it would from that line of code
so the Code runs Line 1 and it prints to the screen then it sees the Jump operation and
it jumps to Line 1 in the Code and continues Forever

- Understanding JUMP better
-
Ln 1 PRINT +Hello
Ln 2 JUMP 5
Ln 3 PRINT +Goodbye
Ln 4 PRINT +Goodbye
Ln 5 PRINT +World
-
Output: Hello 
        World
When the Program seen the JUMP Operation it read that it wants to go to line 5 and since code order does not
magicaly go back up the Program simply ends and the Goodbye prints never get executed

- Markers
Markers a little bit more difficult but easy once you understand
a marker is defined by starting off with a colen ":" and then your marker name followed by a number which you only
have to define once, For example
:My_Marker 0
Markers are case sensitive meaning you have to get your capitals right when calling them, the space followed by a 0,
is Necessary for how the program handles markers. All you have to remember when giving your marker a number is,
every marker cannot have the same last number and you have a certain amount of markers aswell(you shouldin't worry about) since the number is very large
every next number can be how ever much bigger may the next last number be either 1 bigger or 100 bigger it doesin't matter

- Basic Marker Jump
-
Ln 1 :My_Marker 0
Ln 2 PRINT +Hello World
Ln 3 JUMP My_Marker
-
Output: Hello World (Forever)

a Conditional JUMP Operation is very useful for loops and despite the complicated look they are very easy to understand.
For this example we will be using the JEQ Operation
a Conditional JUMP takes three inputs A, B, and C
A and B is the Conditional part while C is if the Condition is true C is where it will jump to in the program
JEQ Tests if A and B is Equal to Eachother
A and B can be either Memory Address's or Pointers

- Conditional JUMP Operations (True)
-
Ln 1 LOAD 0 10
Ln 2 LOAD 1 10
Ln 3 :My_Marker 0
Ln 4 PRINT +Hello World
Ln 5 JEQ 0 1 My_Marker
-
Output: Hello World (Forever)

In this case JEQ would return true therefor it would go to where we want in the code(My_Marker)

- Conditional JUMP Operations (False)
-
Ln 1 LOAD 0 10
Ln 2 LOAD 1 5
Ln 3 :My_Marker 0
Ln 4 PRINT +Hello World
Ln 5 JEQ 0 1 My_Marker
-
Output: Hello World

In this case JEQ would return false therefor it would print once and not jump in the code


Loops

Loops are by far one of the most things used in programming that's why it's essential to know how to use one

For a basic loop we will First learn how to make a incrementer
- Basic Incrementer
-
LOAD 0 1
LOAD 1 1
ADD 0 1 0
PRINT +{0}
-
Output: 2

So we are getting two values, 0 and 1.
we are adding 0 and 1 together and putting the sum of that back into 0
The Reason for this is simple, Instead of dumping the sum into another address rather, putting it back into the inital
address is so we can actually increment the address
think of the address 1 as the amount we increment 0 by

we can also modify this to loop
- Basic Loop Incrementer
-
LOAD 0 1
LOAD 1 1
:Loop 0
ADD 0 1 0
PRINT +{0}
JUMP Loop
-
Output: 1
        2
        3...(Forever)


Now this last part is a little challenging but here is a Loop with a Condition that if the count reaches 10 ten it will stop

- Conditional Loop Incrementer
-
LOAD 0 1
LOAD 1 1
LOAD 2 10
:Loop 0
ADD 0 1 0
PRINT +{0}
JEQ 0 2 End_Loop
JUMP Loop

:End_Loop
HALT
-

So First of, you might notice HALT in the End_Loop marker.

# HALT Should always be at the end of your program no matter what
# the reason for not including them in these short examples is solely for educational purposes. if you try to run these scripts they most likely won't work without the HALT at the end
Because if your program does not have it, then it could cause major issues for the linereader in main.py

Back to the main topic the actual code outside of End_Loop might Look scary but let me break down every line

LOAD 0 1 and LOAD 1 1 are for the incrementer while LOAD 2 10 is for the amount if times we want to increment 0
JEQ is comparing if we met the amount of times we needed to increment and if so then End_Loop
JUMP is simply restarting the loop if JEQ is false

