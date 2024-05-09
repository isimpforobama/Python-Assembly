# The Rules for these Scripts are the following,
# Code Snippets cannot exceed 30 Lines of code


Fibonacci Sequence. Displays the First ten Digits.
LOAD 0 0
LOAD 1 1
LOAD 2 1
LOAD 3 1
LOAD 4 10
PRINT +{0}
PRINT +{1}
:LOOP
ADD 2 3 2
ADD 0 1 0
ADD 0 1 1
PRINT +{0}
PRINT +{1}
JEQ 2 4 16
JUMP 8
HALT

Basic Incrementer to 100
LOAD 0 100
LOAD 1 1
LOAD 2 1
:Loop
ADD 1 2 1
PRINT +{1}
JEQ 0 1 9
JUMP 4
HALT