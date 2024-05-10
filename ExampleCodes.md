Fibonacci Sequence. Displays the First ten Digits.
LOAD 0 0
LOAD 1 1
LOAD 2 1
LOAD 3 1
LOAD 4 10
PRINT +{0}
PRINT +{1}
:LOOP 0
ADD 2 3 2
ADD 0 1 0
ADD 0 1 1
PRINT +{0}
PRINT +{1}
JEQ 2 4 16
JUMP LOOP
HALT

Basic Incrementer to 100
LOAD 0 1
LOAD 1 1
LOAD 2 10
:Loop 0
ADD 0 1 0
PRINT +{0}
JEQ 0 2 End_Loop
JUMP Loop
:End_Loop 1
HALT