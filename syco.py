import re, sys

s = sys.stdin.read()
reserved_tokens = ["print", "reverse", "toupper", "tolower", "append_a"]
functions = dict()
lines = [s.split("\n")][0]
flag = 0
abc = []
output = []
def checkLine(line, abc):
    for i in abc:
        if line >= i[0] and line <= i[1]:
            return False
    return True

def pro(operator, operand):
    if operator == "print":
        output.append(operand)
        return None

    elif operator == "reverse":
        return operand[::-1]
    elif operator == "toupper":
        return operand.upper()
    elif operator == "tolower":
        return operand.lower()
    elif operator == "append_a":
        return operand+"a"

def functionOperation(func, operand):
    print functions[func]
    stack = [operand]
    for i in range(functions[func][0]+1, functions[func][1]):
        temp = lines[i].split()
        stack = temp[:-1] + stack
        v1 = stack.pop()
        v2 = stack.pop()
        print v2, v1
        if v2 in reserved_tokens:
            returnValue = pro(v2, v1)
            if returnValue is not None:
                stack.append(returnValue)
            else:
                if len(stack) > 0:
                    return "ERROR"
        elif v2 in functions:
            print "in function again call"
            frv = functionOperation(v2, v1)
            if frv == "ERROR":
                return "ERROR"
            print stack
    return stack

# Collect all the functions present in the code 
for i in range(len(lines)):
    temp = lines[i].split()
    print temp

    # Check for function definitions
    if len(temp) >= 2 and temp[0]== "define":
        start = i 
        name = temp[1]
        while(True):
            i += 1
            temp = lines[i].split()
            if temp[0] == "end":
                end = i
                break 
        functions[name]= [start,end]
        abc.append([start, end])


print functions

# Perform the operations
error = False
for i in range(len(lines)):
    if not checkLine(i, abc):
        continue

    # Create a stack and get the 
    stack= lines[i].split()

    j = len(stack)
    while len(stack) > 1: 
        v1 = stack.pop()
        v2 = stack.pop()
        print "print the values of v1 and v2"
        print v1 , v2
        if v1[0] == '"':
            v1 = v1[1:-1]
        if v2 in reserved_tokens:
            returnValue = pro(v2, v1)
            if returnValue is not None:
                stack.append(returnValue)
            else:
                if len(stack) > 0:
                    error = True
                    break
        
        elif v2 in functions: 
            print "0000000000000000000000000"
            funRetVal = functionOperation(v2, v1)
            if funRetVal == "ERROR":
                error = True
            else :
                stack = stack + funRetVal
        else:
            error = True
            break  
    if len(stack) == 1:
        output.append(stack[0])

print "Processing khatam"
if error == True:
    print "ERROR"
else :
    for i in output:
        print i
            
