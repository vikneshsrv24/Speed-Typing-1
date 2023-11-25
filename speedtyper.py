from time import time

def typerror(terminal):
    global inputwords
    words=terminal.split()                       #  split words into list
    errors=0

    for i in range(len(inputwords)):            #logic to calculate input accuracy
        if i in (0,len(inputwords)-1):
            if inputwords[i]==words[i]:    # first and last letter not matches mean it increase error count by 1
                continue
            else:
                errors +=1
        else:
            if inputwords[i]==words[i]:
                if(inputwords[i+1]==words[i+1]&(inputwords[i-1]==words[i-1])):    #matching the adjacent elements after first or last element matching
                    continue
                else:
                    errors +=1
            else:
                errors +=1
        return errors

def speed(inputterminal,starttime,endtime):    #logic to calculate speed WPM
    global time
    global inputwords

    inputwords=inputterminal.split()
    twords=len(inputwords)
    speed=twords/time
    
    return speed

def timetaken(starttime,endtime):     #logic for calculating total time taken to write
    time=endtime-starttime
    return time

if __name__=='__main__':
    # enter the needed paragraph here
    terminal="This is a paragraph. You're reading a paragraph right now. This paragraph is three sentences long."
    print("Enter the paragraph below : ",terminal)
    print("*---------------------------*")
    input()                                                              #press enter
    
    starttime=time()                                                     #logic to record input time
    inputterminal=input()
    endtime=time()

    time=round(timetaken(starttime,endtime),2)            # return function values and time round off
    speed=speed(inputterminal,starttime,endtime)
    errors=typerror(terminal)
    print("*----------------------------*")
    print("Total time taken: ",time,"sec")
    print("Average typing speed: ",speed)
    print("Total errors: ",errors)

    
