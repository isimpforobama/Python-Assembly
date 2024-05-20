import time, json, os, math

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


code = []

# Code Length
code_length = 0

# Available Memory Locations
AVAILABLEMEMORY = json_config_memory # Does not actually take real memory, this Variable is just for the sake of the program
AVAILABLEMEMORY = AVAILABLEMEMORY / 3
AVAILABLEMEMORY = math.floor(AVAILABLEMEMORY)
RAM = [0] * int(math.floor(AVAILABLEMEMORY / 3))
RAM_POINTERS = {i: 0 for i in range(AVAILABLEMEMORY)}
CODE_POINTERS = {i: 0 for i in range(AVAILABLEMEMORY)}
for i in CODE_POINTERS:
    CODE_POINTERS[i] = ['', '']

AVAILABLEMEMORY = str(AVAILABLEMEMORY)

if Debugging == True:
    print('Config Settings are\nAvailable Memory: ' + str(json_config_memory) + '\nRAM POINTERS: ' + AVAILABLEMEMORY + '\nCODE POINTERS: ' + AVAILABLEMEMORY + '\nRAM: ' + AVAILABLEMEMORY + '\nSleep at Loop: ' + str(json_config_sleepatloop) + '\nSleep Time: ' + str(json_config_sleeptime) + '\nRequire Halt: ' + str(json_config_requirehalt))

AVAILABLEMEMORY = int(AVAILABLEMEMORY)

# Last Operation
last_operation = ''

# Last Operation Result
last_operation_result = 0

# SUM is set to zero at the start of the program
SUM = 0

def throw_error(error, codeline, current_line, requiredargs=3, inputedargs=2):
    current_line += 1
    errors={
        '100': f'{codeline}\nException in Line: {current_line}\nError: Variable Not Found Error',
        '101': f'{codeline}\nException in Line: {current_line}\nError: Index Out of Range Error',
        '102': f'{codeline}\nException in Line: {current_line}\nError: Not Enough Memory Error',
        '103': f'{codeline}\nException in Line: {current_line}\nError: Not Enough Args Error, Got {inputedargs}, Required {requiredargs}',
        '104': f'{codeline}\nException in Line: {current_line}\nError: Too Many Args Error, Got {inputedargs}, Required {requiredargs}',
        '105': f'{codeline}\nException in Line: {current_line}\nError: Division By Zero',
        '106': f'{codeline}\nException in Line: {current_line}\nAttempt to Jump to Line: {inputedargs}\nError: Jump Destination out of Reach Error',
        '107': f'{codeline}\nException in Line: {current_line}\nDuplicate Code Pointer',
    }
    e = errors.get(error)
    raise Exception(e)


# Function To return the value of a Pointers Index to access the variable inside of a pointer
def GET_POINTER_VALUE(P, dictionary=RAM_POINTERS):
    for key, value in dictionary.items():
        if value == P:
            return(RAM[key])
    return None

def GET_KEY_FROM_POINTER(P, dictionary=RAM_POINTERS):
    for key, value in dictionary.items():
        if value == P:
            return(key)
    return None

def search_dict(dictionary, target, return_index=False):
    for index, (key, value) in enumerate(dictionary.items()):
        if isinstance(value, dict):
            if search_dict(value, target):
                if return_index is False:
                    return True
                elif return_index is True:
                    return index
        elif isinstance(value, list):
            if target in value:
                if return_index is False:
                    return True
                elif return_index is True:
                    return index
        elif value == target:
            if return_index is False:
                    return True
            elif return_index is True:
                return index
    return False

def compile_code(code):
    code = code.split('\n')
    for i, line in enumerate(code):
        if Debugging == True:
            print(f"Line {i}: {line}")
        for char in line:
            if char == ':':
                filenumber = int(line.split(':')[1].split(' ')[1])
                code_pointer = str(line.split(':')[1].split(' ')[0])
                if search_dict(CODE_POINTERS, code_pointer) != True:
                    CODE_POINTERS[filenumber][0] = str(i)
                    CODE_POINTERS[filenumber][1] = str(code_pointer)
                else:
                    throw_error('107', code[i], i)



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
    if b == 0:
        throw_error('105', code[current_line], current_line)
    SUM = a / b
    RAM[c] = SUM
    last_operation = 'DIV'
    last_operation_result = SUM


current_line = 0
def main():
    global code, last_operation_result, last_operation, RAM, RAM_POINTERS, CODE_POINTERS, code_length, current_line
    # Iterate Through Each Line in the Input File
    input_file = readinput()
    compile_code(input_file)
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
            if len(LINEVALUES) < 4:
                throw_error('103', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 4:
                throw_error('104', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            # Get the Memory Locations
            a = GET_POINTER_VALUE(P=str(LINEVALUES[1]))
            b = GET_POINTER_VALUE(P=str(LINEVALUES[2]))
            if LINEVALUES[3][0].isdigit() is False:
                c = int(GET_KEY_FROM_POINTER(P=str(LINEVALUES[3])))
            if a == None and LINEVALUES[1].isdigit():
                a = RAM[int(LINEVALUES[1])]

            if b == None and LINEVALUES[2].isdigit():
                b = RAM[int(LINEVALUES[2])]

            if LINEVALUES[3][0].isdigit():
                c = int(LINEVALUES[3])
            elif a != None and b != None and c != None and LINEVALUES[1].isdigit() and LINEVALUES[2].isdigit() and LINEVALUES[3].isdigit():
                throw_error('100', code[current_line], current_line)
            # Call the ADD Function
            ADD(a, b, c)
            last_operation = 'ADD'
        
        # SUB Operation
        elif OPERATION == 'SUB':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 4:
                throw_error('103', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 4:
                throw_error('104', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            # Get the Memory Locations
            a = GET_POINTER_VALUE(P=str(LINEVALUES[1]))
            b = GET_POINTER_VALUE(P=str(LINEVALUES[2]))
            if LINEVALUES[3][0].isdigit() is False:
                c = int(GET_KEY_FROM_POINTER(P=str(LINEVALUES[3])))
            if a == None and LINEVALUES[1].isdigit():
                a = RAM[int(LINEVALUES[1])]

            if b == None and LINEVALUES[2].isdigit():
                b = RAM[int(LINEVALUES[2])]

            if LINEVALUES[3][0].isdigit():
                c = int(LINEVALUES[3])
            elif a != None and b != None and c != None and LINEVALUES[1].isdigit() and LINEVALUES[2].isdigit() and LINEVALUES[3].isdigit():
                throw_error('100', code[current_line], current_line)
            # Call the ADD Function
            SUB(a, b, c)
            last_operation = 'SUB'
        
        # MUL Operation
        elif OPERATION == 'MUL':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 4:
                throw_error('103', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 4:
                throw_error('104', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            # Get the Memory Locations
            a = GET_POINTER_VALUE(P=str(LINEVALUES[1]))
            b = GET_POINTER_VALUE(P=str(LINEVALUES[2]))
            if LINEVALUES[3][0].isdigit() is False:
                c = int(GET_KEY_FROM_POINTER(P=str(LINEVALUES[3])))
            if a == None and LINEVALUES[1].isdigit():
                a = RAM[int(LINEVALUES[1])]

            if b == None and LINEVALUES[2].isdigit():
                b = RAM[int(LINEVALUES[2])]

            if LINEVALUES[3][0].isdigit():
                c = int(LINEVALUES[3])
            elif a != None and b != None and c != None and LINEVALUES[1].isdigit() and LINEVALUES[2].isdigit() and LINEVALUES[3].isdigit():
                throw_error('100', code[current_line], current_line)
            # Call the ADD Function
            MUL(a, b, c)
            last_operation = 'MUL'
        
        # DIV Operation
        elif OPERATION == 'DIV':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 4:
                throw_error('103', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 4:
                throw_error('104', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            # Get the Memory Locations
            a = GET_POINTER_VALUE(P=str(LINEVALUES[1]))
            b = GET_POINTER_VALUE(P=str(LINEVALUES[2]))
            if LINEVALUES[3][0].isdigit() is False:
                c = int(GET_KEY_FROM_POINTER(P=str(LINEVALUES[3])))
            if a == None and LINEVALUES[1].isdigit():
                a = RAM[int(LINEVALUES[1])]

            if b == None and LINEVALUES[2].isdigit():
                b = RAM[int(LINEVALUES[2])]

            if LINEVALUES[3][0].isdigit():
                c = int(LINEVALUES[3])
            elif a != None and b != None and c != None and LINEVALUES[1].isdigit() and LINEVALUES[2].isdigit() and LINEVALUES[3].isdigit():
                throw_error('100', code[current_line], current_line)
            # Call the ADD Function
            DIV(a, b, c)
            last_operation = 'DIV'
        
        # JUMP Operation
        elif OPERATION == 'JUMP':
            # if there are less than 1 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 2:
                throw_error('103', code[current_line], current_line, requiredargs=1, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 2:
                throw_error('104', code[current_line], current_line, requiredargs=1, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            # Get the Line Number
            if LINEVALUES[1] == str(LINEVALUES[1]) and LINEVALUES[1].isdigit() == False:
                    # Get the jump line from the code pointers
                    key = search_dict(CODE_POINTERS, str(LINEVALUES[1]), return_index=True)
                    current_line = int(CODE_POINTERS[key][0])
                    continue
            elif int(LINEVALUES[1]) <= code_length:
                if LINEVALUES[1].isdigit():
                    current_line = int(LINEVALUES[1])
                last_operation = 'JUMP'
                current_line -= 2
            else:
                throw_error('106', code[current_line], current_line, inputedargs=LINEVALUES[1])

        # JNE Operation
        elif OPERATION == 'JNE':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 4:
                throw_error('103', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 4:
                throw_error('104', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            a = GET_POINTER_VALUE(P=str(LINEVALUES[1]))
            b = GET_POINTER_VALUE(P=str(LINEVALUES[2]))
            if a == None and LINEVALUES[1].isdigit():
                a = RAM[int(LINEVALUES[1])]
            if b == None and LINEVALUES[2].isdigit():
                b = RAM[int(LINEVALUES[2])]
            if a != b:
                # Get the Line Number
                if LINEVALUES[3] == str(LINEVALUES[3]) and LINEVALUES[3].isdigit() == False:
                        # Get the jump line from the code pointers
                        key = search_dict(CODE_POINTERS, str(LINEVALUES[3]), return_index=True)
                        current_line = int(CODE_POINTERS[key][0])
                        last_operation = 'JNE'
                        current_line -= 1
                elif int(LINEVALUES[3]) <= code_length:
                    if LINEVALUES[3].isdigit():
                        current_line = int(LINEVALUES[3])
                        last_operation = 'JNE'
                        current_line -= 2
                else:
                    throw_error('106', code[current_line], current_line, inputedargs=LINEVALUES[1])
        
        # JLT Operation
        elif OPERATION == 'JLT':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 4:
                throw_error('103', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 4:
                throw_error('104', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            a = GET_POINTER_VALUE(P=str(LINEVALUES[1]))
            b = GET_POINTER_VALUE(P=str(LINEVALUES[2]))
            if a == None and LINEVALUES[1].isdigit():
                a = RAM[int(LINEVALUES[1])]
            if b == None and LINEVALUES[2].isdigit():
                b = RAM[int(LINEVALUES[2])]
            if a < b:
                # Get the Line Number
                if LINEVALUES[3] == str(LINEVALUES[3]) and LINEVALUES[3].isdigit() == False:
                        # Get the jump line from the code pointers
                        key = search_dict(CODE_POINTERS, str(LINEVALUES[3]), return_index=True)
                        current_line = int(CODE_POINTERS[key][0])
                        last_operation = 'JLT'
                        current_line -= 1
                elif int(LINEVALUES[3]) <= code_length:
                    if LINEVALUES[3].isdigit():
                        current_line = int(LINEVALUES[3])
                        last_operation = 'JLT'
                        current_line -= 2
                else:
                    throw_error('106', code[current_line], current_line, inputedargs=LINEVALUES[1])
            
        # JGT Operation
        elif OPERATION == 'JGT':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 4:
                throw_error('103', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 4:
                throw_error('104', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
                raise Exception(e)
            a = GET_POINTER_VALUE(P=str(LINEVALUES[1]))
            b = GET_POINTER_VALUE(P=str(LINEVALUES[2]))
            if a == None and LINEVALUES[1].isdigit():
                a = RAM[int(LINEVALUES[1])]
            if b == None and LINEVALUES[2].isdigit():
                b = RAM[int(LINEVALUES[2])]
            if a > b:
                # Get the Line Number
                if LINEVALUES[3] == str(LINEVALUES[3]) and LINEVALUES[3].isdigit() == False:
                        # Get the jump line from the code pointers
                        key = search_dict(CODE_POINTERS, str(LINEVALUES[3]), return_index=True)
                        current_line = int(CODE_POINTERS[key][0])
                        last_operation = 'JGT'
                        current_line -= 1
                elif int(LINEVALUES[3]) <= code_length:
                    if LINEVALUES[3].isdigit():
                        current_line = int(LINEVALUES[3])
                        last_operation = 'JGT'
                        current_line -= 2
                else:
                    throw_error('106', code[current_line], current_line, inputedargs=LINEVALUES[1])

        # JEQ Operation
        elif OPERATION == 'JEQ':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 4:
                throw_error('103', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 4:
                throw_error('104', code[current_line], current_line, requiredargs=3, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
                raise Exception(e)
            a = GET_POINTER_VALUE(P=str(LINEVALUES[1]))
            b = GET_POINTER_VALUE(P=str(LINEVALUES[2]))
            if a == None and LINEVALUES[1].isdigit():
                a = RAM[int(LINEVALUES[1])]
            if b == None and LINEVALUES[2].isdigit():
                b = RAM[int(LINEVALUES[2])]
            if a == b:
                # Get the Line Number
                if LINEVALUES[3] == str(LINEVALUES[3]) and LINEVALUES[3].isdigit() == False:
                        # Get the jump line from the code pointers
                        key = search_dict(CODE_POINTERS, str(LINEVALUES[3]), return_index=True)
                        current_line = int(CODE_POINTERS[key][0])
                        last_operation = 'JEQ'
                        current_line -= 1
                elif int(LINEVALUES[3]) <= code_length:
                    if LINEVALUES[3].isdigit():
                        current_line = int(LINEVALUES[3])
                        last_operation = 'JEQ'
                        current_line -= 2
                else:
                    throw_error('106', code[current_line], current_line, inputedargs=LINEVALUES[1])
    
        # BIZ Operation
        elif OPERATION == 'BIZ':
            # if there are less than 1 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 2:
                throw_error('103', code[current_line], current_line, requiredargs=1, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 2:
                throw_error('104', code[current_line], current_line, requiredargs=1, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            if last_operation_result == 0:
                # Get the Line Number
                if LINEVALUES[1] == str(LINEVALUES[1]):
                        # Get the jump line from the code pointers
                        key = search_dict(CODE_POINTERS, str(LINEVALUES[1]), return_index=True)
                        current_line = int(CODE_POINTERS[key][0])
                        current_line -= 1
                        continue
                elif int(LINEVALUES[1]) <= code_length:
                    if LINEVALUES[1].isdigit():
                        current_line = int(LINEVALUES[1])
                    last_operation = 'JUMP'
                    current_line -= 2
                else:
                    throw_error('106', code[current_line], current_line, inputedargs=LINEVALUES[1])
        # HALT Operation
        elif OPERATION == 'HALT':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 1:
                throw_error('103', code[current_line], current_line, requiredargs=0, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 1:
                throw_error('104', code[current_line], current_line, requiredargs=0, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            # Stop the Program
            break
        
        # PRINT Operation
        elif OPERATION == 'PRINT':
            if len(LINEVALUES) < 2:
                throw_error('103', code[current_line], current_line, requiredargs=1, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            plus_split=code[current_line].split("+")
            plus_split.pop(0)
            for i in range(len(plus_split)):
                if plus_split[i][0] == '{':
                    if plus_split[i][1:-1].isdigit():
                        print(str(RAM[int(plus_split[i][1:-1])]), end='')
                    elif GET_POINTER_VALUE(P=plus_split[i][1:-1]) == None:
                        e = str(code[current_line]) + '\n' + 'Exception in Line: ' + str(current_line + 1) + '\n' + 'Error: Variable Not Found Error'
                        raise Exception(e)
                    else:
                        print(str(GET_POINTER_VALUE(P=plus_split[i][1:-1])), end='')
                elif plus_split[i] == '\\n':
                    print('\n')
                else:
                    print(str(plus_split[i]), end='')
            print()

        # LOAD Operation
        elif OPERATION == 'LOAD':
           # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 3:
                throw_error('103', code[current_line], current_line, requiredargs=2, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 3:
                throw_error('104', code[current_line], current_line, requiredargs=2, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            # Get the Memory Locations
            a = int(LINEVALUES[1])
            b = int(LINEVALUES[2])
            # Store the value of the Input B into the Memory Location A
            RAM[a] = b
            last_operation = 'LOAD'

        # POINTER Operation
        elif OPERATION == 'POINTER':
            input = code[current_line]
            parts = input.split()
            memoryreference = parts[1].strip('()')
            pointer = parts[3].strip(')')
            if memoryreference.isdigit():
                RAM_POINTERS[int(memoryreference)] = pointer
        
        # SLEEP OPERATION
        elif OPERATION == 'SLEEP':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 2:
                throw_error('103', code[current_line], current_line, requiredargs=1, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 2:
                throw_error('104', code[current_line], current_line, requiredargs=1, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            time.sleep(int(LINEVALUES[1]) / 1000)
            last_operation = 'SLEEP'

        # STORE Operation
        elif OPERATION == 'STORE':
            # if there are less than 3 variables in LINEVALUES, raise an exception
            if len(LINEVALUES) < 3:
                throw_error('103', code[current_line], current_line, requiredargs=2, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 3:
                throw_error('104', code[current_line], current_line, requiredargs=2, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            # Get the Memory Locations
            a = GET_KEY_FROM_POINTER(P=str(LINEVALUES[1]))
            b = GET_KEY_FROM_POINTER(P=str(LINEVALUES[2]))
            if a == None:
                a = RAM[int(LINEVALUES[1])]
            if b == None:
                b = RAM[int(LINEVALUES[2])]
            # Store the value of the Memory Location B into the Memory Location A
            RAM[a] = RAM[b]
            last_operation = 'STORE'

        # CLS Operation
        elif OPERATION == 'CLS':
            if len(LINEVALUES) < 2:
                throw_error('103', code[current_line], current_line, requiredargs=1, inputedargs=len(LINEVALUES) - 1) # Not Enough Args Error
            if len(LINEVALUES) > 2:
                throw_error('104', code[current_line], current_line, requiredargs=1, inputedargs=len(LINEVALUES) - 1) # Too Many Args Error
            os.system('cLs')

        # current_line should always be at the bottom of the loop
        current_line += 1

if __name__ == '__main__':
    main()

if displayprogramfinishmessage == True:
    print('Program Finished')
    i = input('Press Enter to Exit')
else:
    i = input('')
