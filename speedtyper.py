from time import time

def typeerror(terminal):
    global inputwords
    words=terminal.spilt()  # words into list
    errors=0

    for i in range(len(inputwords)):
        if i in (0,len(inputwords)-1):
            if inputwords[i]==words[i]:
                continue
            else:
                errors=errors+1
        else:
            if inputwords[i]==words[i]:
                if(inputwords[i+1]==words[i+1]&(inputwords[i-1]==words[i-1])):
                    continue
                


