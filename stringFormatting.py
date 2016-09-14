def formNumber(s, startingIndex):
    n = 0
    i = startingIndex +1
    try :
        while s[i].isdigit():
            n *= 10 
            n += int(s[i])
            i += 1
    except IndexError:
        pass
    return n, i

repArray = raw_input().split()
inputString = raw_input()
inputArray = inputString.split("%s")
# print repArray
# print inputArray
outputArray = []
k = 0
i = 0
# Add the first part of string to output
outputArray.append(inputArray[0])
k += 1
for j in range(k, len(inputArray)):
    # If the input gives the array index of replacement array
    try:
        # print inputArray[j]
        if inputArray[j] == '':
            outputArray.append(repArray[i])
            i += 1
            continue
        if inputArray[j][0] == '[':
            # print ("idhar aaya")
            # number denotes the number which is inside the square brackets
            # index gives the index till the closing square bracket
            number, index = formNumber(inputArray[j], 0)
            # print number, index
            if number == 0 :
                outputArray.append("%s" + inputArray[j])   
                continue;
            if inputArray[j][index+1] == ':':
                new_number, new_index = formNumber(inputArray[j], index+1)
                # print "in :"
                # print new_number, new_index
                outputArray.append(repArray[number][:new_number])
                outputArray.append(inputArray[j][new_index:])
            else:
                outputArray.append(repArray[number])
                outputArray.append(inputArray[j][index+1:])
        else:
            if inputArray[j][0] == ':':
                number, index = formNumber(inputArray[j], 0)
                if number == 0 :
                    outputArray.append("%s" + inputArray[j])
                    continue
                outputArray.append(repArray[i][:number])
                outputArray.append(inputArray[j][index:])
            else:
                outputArray.append(repArray[i])
                outputArray.append(inputArray[j])
            i += 1 
        # print outputArray
    except IndexError:
        outputArray.append("%s" + inputArray[j])
print "".join(outputArray)
            
