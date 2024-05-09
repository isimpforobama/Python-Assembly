import time, json, os

def readinput():
    filepath = os.path.dirname(os.path.abspath(__file__))

    # Open the File and Read the Contents
    with open(filepath + '/' + 'input.txt', 'r') as file:
        data = file.read()
    return data

parent_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(parent_dir, "config.json")

with open(config_path, 'r') as f:
    config = json.load(f)

json_config_memory = config.get('memory')
json_config_sleepatloop = config.get('sleepatloop')
json_config_sleeptime = config.get('sleeptime')
json_config_requirehalt = config.get('requirehalt')
Debugging = config.get('Debugging')
displayprogramfinishmessage = config.get('Display_Program_finish_Message')

if Debugging == True:
    print('Config Settings are\nAvailable Memory: ' + str(json_config_memory) + '\nSleep at Loop: ' + str(json_config_sleepatloop) + '\nSleep Time: ' + str(json_config_sleeptime) + '\nRequire Halt: ' + str(json_config_requirehalt))

code = []

# Code Length
code_length = 0

# Available Memory Locations
AVAILABLEMEMORY = json_config_memory # Does not actually take real memory, this Variable is just for the sake of the program
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

    json_config_sleeptime
    if json_config_sleepatloop is True:
        sleeptime = json_config_sleeptime
    elif json_config_sleeptime is False:
        sleeptime = 0

    # Loop Through Each Line in the Code
    while current_line <= code_length:
        # Sleep for 0.01 Seconds if the program is laggy
        time.sleep(sleeptime)
        # Split the Line into a list
        LINEVALUES = code[current_line].split(' ')
        # Get the Operation the line is calling
        OPERATION = LINEVALUES[0]

        # print(last_operation)
        # ADD Operation
        if OPERATION == 'ADD':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 4:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 3 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
            # Get the Memory Locations
            a = RAM[int(LINEVALUES[1])]
            b = RAM[int(LINEVALUES[2])]
            c = int(LINEVALUES[3])
            # Call the ADD Function
            ADD(a, b, c)
            last_operation = 'ADD'
        
        # SUB Operation
        elif OPERATION == 'SUB':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 4:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 3 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
            # Get the Memory Locations
            a = RAM[int(LINEVALUES[1])]
            b = RAM[int(LINEVALUES[2])]
            c = int(LINEVALUES[3])
            # Call the SUB Function
            SUB(a, b, c)
            last_operation = 'SUB'
        
        # MUL Operation
        elif OPERATION == 'MUL':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 4:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 3 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
            # Get the Memory Locations
            a = RAM[int(LINEVALUES[1])]
            b = RAM[int(LINEVALUES[2])]
            c = int(LINEVALUES[3])
            # Call the MUL Function
            MUL(a, b, c)
            last_operation = 'MUL'
        
        # DIV Operation
        elif OPERATION == 'DIV':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 4:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 3 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
            # Get the Memory Locations
            a = RAM[int(LINEVALUES[1])]
            b = RAM[int(LINEVALUES[2])]
            c = int(LINEVALUES[3])
            # Call the DIV Function
            DIV(a, b, c)
            last_operation = 'DIV'
        
        # JUMP Operation
        elif OPERATION == 'JUMP':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 2:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 1  arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
            # Get the Line Number
            if int(LINEVALUES[1]) <= code_length:
                current_line = int(LINEVALUES[1])
                last_operation = 'JUMP'
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
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 4:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 3 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
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
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 4:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 3 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
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
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 4:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 3 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
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
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 4:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 3 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
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
        # HALT Operation
        elif OPERATION == 'HALT':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 1:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 0 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
            # Stop the Program
            break
        
        # PRINT Operation
        elif OPERATION == 'PRINT':

            plus_split=code[current_line].split("+")
            plus_split.pop(0)
            for i in range(len(plus_split)):
                if plus_split[i][0] == '{':
                    print(str(RAM[int(plus_split[i][1:-1])]), end='')
                elif plus_split[i] == '\\n':
                    print('\n')
                else:
                    print(str(plus_split[i]), end='')
            print()

        # LOAD Operation
        elif OPERATION == 'LOAD':
           # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 3:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 2 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
            # Get the Memory Locations
            a = int(LINEVALUES[1])
            b = int(LINEVALUES[2])
            # Store the value of the Input B into the Memory Location A
            RAM[a] = b
            last_operation = 'LOAD'

        # SLEEP OPERATION
        elif OPERATION == 'SLEEP':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 2:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 1 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
            time.sleep(int(LINEVALUES[1]) / 1000)
            last_operation = 'SLEEP'

        # STORE Operation
        elif OPERATION == 'STORE':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) != 3:
                raise Exception(str(code[current_line]) + '\n' + 'Line: ' + str(current_line + 1) + ' takes 2 positional arguments but ' + str(len(LINEVALUES) - 1) + ' were given')
            # Get the Memory Locations
            a = int(LINEVALUES[1])
            b = int(LINEVALUES[2])
            # Store the value of the Memory Location B into the Memory Location A
            RAM[a] = RAM[b]
            last_operation = 'STORE'

        # current_line should always be at the bottom of the loop
        current_line += 1

    

if __name__ == '__main__':
    main()

if displayprogramfinishmessage == True:
    print('Program Finished')
    i = input('Press Enter to Exit')
else:
    i = input('')
