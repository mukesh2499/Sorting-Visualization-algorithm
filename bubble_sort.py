import time
# importing time library to implement  
def bubblesort(data,drawData,timepause):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1] :
                data[j],data[j+1]=data[j+1],data[j]
                drawData(data,['red' if x==j or x==j+1 else 'black' for x in range(len(data))])
                time.sleep(timepause)# used to take a pause of time given as an argument.
    drawData(data,['red' for x in range(len(data))])
            
