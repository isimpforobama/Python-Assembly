import time
import sqlite3

# Create a Database to store the filepath the user enters
conn = sqlite3.connect('filepath.db')
c = conn.cursor()



def readinput():
    c.execute('CREATE TABLE IF NOT EXISTS filepath (path TEXT)')
    # Get the Filepath from the User if the Filepath is not in the Database
    if c.execute('SELECT * FROM filepath').fetchone() == None:
        filepath = input('Enter the Filepath of the input.txt file: ')
    else:
        filepath = c.execute('SELECT * FROM filepath').fetchone()[0]
    # Insert the Filepath into the Database
    c.execute('INSERT INTO filepath VALUES (?)', (filepath,))
    conn.commit()
    # Open the File and Read the Contents
    with open(filepath, 'r') as file:
        data = file.read()
    return data

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



code = []

# Code Length
code_length = 0

# Available Memory Locations
AVAILABLEMEMORY = 1024 # Does not actually take real memory, this Variable is just for the sake of the program
RAM = [0] * AVAILABLEMEMORY

# Last Operation
last_operation = ''

# Last Operation Result
last_operation_result = 0

# SUM is set to zero at the start of the program
SUM = 0

def ADD(a, b, c):
    global last_operation, last_operation_result, RAM, SUM
    SUM = a + b
    RAM[c] = SUM
    last_operation = 'ADD'
    last_operation_result = SUM

def SUB(a, b, c):
    global last_operation, last_operation_result, RAM, SUM
    SUM = a - b
    RAM[c] = SUM
    last_operation = 'SUB'
    last_operation_result = SUM

def MUL(a, b, c):
    global last_operation, last_operation_result, RAM, SUM
    SUM = a * b
    RAM[c] = SUM
    last_operation = 'MUL'
    last_operation_result = SUM

def DIV(a, b, c):
    global last_operation, last_operation_result, RAM, SUM
    SUM = a / b
    RAM[c] = SUM
    last_operation = 'DIV'
    last_operation_result = SUM
current_line = 0
def main():
    global code, last_operation_result, last_operation, RAM, code_length, current_line
    # Iterate Through Each Line in the Input File
    input_file = readinput()
    
    for line in input_file.split('\n'):
        code.append(line)
    for line in code:
        code_length += 1
    # Current Line Number
    current_line = 0

    # Loop Through Each Line in the Code
    while current_line <= code_length:
        # Sleep for 0.01 Seconds if the program is laggy
        # time.sleep(0.01)
        # Split the Line into a list
        LINEVALUES = code[current_line].split(' ')
        # Get the Operation the line is calling
        OPERATION = LINEVALUES[0]

        # print(last_operation)
        # ADD Operation
        if OPERATION == 'ADD':
            # Get the Memory Locations
            a = RAM[int(LINEVALUES[1])]
            b = RAM[int(LINEVALUES[2])]
            c = int(LINEVALUES[3])
            # Call the ADD Function
            ADD(a, b, c)
            last_operation = 'ADD'
        
        # SUB Operation
        elif OPERATION == 'SUB':
            # Get the Memory Locations
            a = RAM[int(LINEVALUES[1])]
            b = RAM[int(LINEVALUES[2])]
            c = int(LINEVALUES[3])
            # Call the SUB Function
            SUB(a, b, c)
            last_operation = 'SUB'
        
        # MUL Operation
        elif OPERATION == 'MUL':
            # Get the Memory Locations
            a = RAM[int(LINEVALUES[1])]
            b = RAM[int(LINEVALUES[2])]
            c = int(LINEVALUES[3])
            # Call the MUL Function
            MUL(a, b, c)
            last_operation = 'MUL'
        
        # DIV Operation
        elif OPERATION == 'DIV':
            # Get the Memory Locations
            a = RAM[int(LINEVALUES[1])]
            b = RAM[int(LINEVALUES[2])]
            c = int(LINEVALUES[3])
            # Call the DIV Function
            DIV(a, b, c)
            last_operation = 'DIV'
        
        # JMP Operation
        elif OPERATION == 'JMP':
            # Get the Line Number
            if int(LINEVALUES[1]) <= code_length:
                current_line = int(LINEVALUES[1])
                last_operation = 'JMP'
                current_line -= 2
            else:
                # Find the starting posistion char of the third number
                start = code[current_line].find(LINEVALUES[1]) + len(LINEVALUES[1]) + 1
                # Find the ending posistion char of the third number
                end = code[current_line].find(' ', start)
                # Raise an Exception
                raise Exception('\n' + ' ' * (start - 1) + '^' + '~' * (end - start) + '\n' + 'Line ' + str(current_line + 1) + ': ' + 'Line Number ' + LINEVALUES[1] + ' is out of range\n\n')

        # JNE Operation
        elif OPERATION == 'JNE':
            if int(LINEVALUES[3]) <= code_length:
                a = RAM[int(LINEVALUES[1])]
                b = RAM[int(LINEVALUES[2])]
                if a != b:
                    current_line = int(LINEVALUES[3])
                    last_operation = 'JNE'
                    current_line -= 2
            else:
                # Find the starting posistion char of the third number
                start = code[current_line].find(LINEVALUES[3]) + len(LINEVALUES[3]) + 1
                # Find the ending posistion char of the third number
                end = code[current_line].find(' ', start)
                # Raise an Exception
                raise Exception('\n' + ' ' * (start - 1) + '^' + '~' * (end - start) + '\n' + 'Line ' + str(current_line + 1) + ': ' + 'Line Number ' + LINEVALUES[1] + ' is out of range\n\n')

        
        # JLT Operation
        elif OPERATION == 'JLT':
            if int(LINEVALUES[3]) <= code_length:
                a = RAM[int(LINEVALUES[1])]
                b = RAM[int(LINEVALUES[2])]
                if a < b:
                    current_line = int(LINEVALUES[3])
                    last_operation = 'JLT'
                    current_line -= 2
            else:
                # Find the starting posistion char of the third number
                start = code[current_line].find(LINEVALUES[3]) + len(LINEVALUES[3]) + 1
                # Find the ending posistion char of the third number
                end = code[current_line].find(' ', start)
                # Raise an Exception
                raise Exception('\n' + ' ' * (start - 1) + '^' + '~' * (end - start) + '\n' + 'Line ' + str(current_line + 1) + ': ' + 'Line Number ' + LINEVALUES[1] + ' is out of range\n\n')
            
        # JGT Operation
        elif OPERATION == 'JGT':
            if int(LINEVALUES[3]) <= code_length:
                a = RAM[int(LINEVALUES[1])]
                b = RAM[int(LINEVALUES[2])]
                if a > b:
                    current_line = int(LINEVALUES[3])
                    last_operation = 'JGT'
                    current_line -= 2
            else:
                # Find the starting posistion char of the third number
                start = code[current_line].find(LINEVALUES[3]) + len(LINEVALUES[3]) + 1
                # Find the ending posistion char of the third number
                end = code[current_line].find(' ', start)
                # Raise an Exception
                raise Exception('\n' + ' ' * (start - 1) + '^' + '~' * (end - start) + '\n' + 'Line ' + str(current_line + 1) + ': ' + 'Line Number ' + LINEVALUES[1] + ' is out of range\n\n')
        

        # JEQ Operation
        elif OPERATION == 'JEQ':
            if int(LINEVALUES[3]) <= code_length:
                a = RAM[int(LINEVALUES[1])]
                b = RAM[int(LINEVALUES[2])]
                if a == b:
                    current_line = int(LINEVALUES[3])
                    last_operation = 'JEQ'
                    current_line -= 2
            else:
                # Find the starting posistion char of the third number
                start = code[current_line].find(LINEVALUES[3]) + len(LINEVALUES[3]) + 1
                # Find the ending posistion char of the third number
                end = code[current_line].find(' ', start)
                # Raise an Exception
                raise Exception('\n' + ' ' * (start - 1) + '^' + '~' * (end - start) + '\n' + 'Line ' + str(current_line + 1) + ': ' + 'Line Number ' + LINEVALUES[1] + ' is out of range\n\n')
    
        # BIZ Operation
        elif OPERATION == 'BIZ':
            if int(LINEVALUES[1]) <= code_length:
                if last_operation_result == 0:
                    current_line = int(LINEVALUES[1])
                    last_operation = 'BIZ'
                    current_line -= 2
            else:
                # Find the starting posistion char of the third number
                start = code[current_line].find(LINEVALUES[1]) + len(LINEVALUES[1]) + 1
                # Find the ending posistion char of the third number
                end = code[current_line].find(' ', start)
                # Raise an Exception
                raise Exception('\n' + ' ' * (start - 1) + '^' + '~' * (end - start) + '\n' + 'Line ' + str(current_line + 1) + ': ' + 'Line Number ' + LINEVALUES[1] + ' is out of range\n\n')
        # HLT Operation
        elif OPERATION == 'HLT':
            # Stop the Program
            break
        
        # PRT Operation
        elif OPERATION == 'PRT':
            # Get the value of the Inputed Variable B
            Function_given = code[current_line]
            plus_split= Function_given.split("+")

            print_statement = ''

            for i in range(len(plus_split)):
                if plus_split[i] == 'PRT ':
                    pass
                elif plus_split[i][0] == '{':
                    print_statement += str(RAM[int(plus_split[i][1:-1])])
                else:
                    print_statement += plus_split[i]
            print(print_statement)

        # LOD Operation
        elif OPERATION == 'LOD':
            # Get the Memory Locations
            a = int(LINEVALUES[1])
            b = int(LINEVALUES[2])
            # Store the value of the Input B into the Memory Location A
            RAM[a] = b
            last_operation = 'LOD'

        # SLP OPERATION
        elif OPERATION == 'SLP':
            time.sleep(int(LINEVALUES[1]) / 1000)
            last_operation = 'SLP'

        # STR Operation
        elif OPERATION == 'STR':
            # Get the Memory Locations
            a = int(LINEVALUES[1])
            b = int(LINEVALUES[2])
            # Store the value of the Memory Location B into the Memory Location A
            RAM[a] = RAM[b]
            last_operation = 'STR'

        # current_line should always be at the bottom of the loop
        current_line += 1

    

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(code[current_line] + ' ' + str(e))

print('Program Finished')
i = input('Press Enter to Exit')