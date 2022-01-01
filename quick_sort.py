import time

# the below function performs the partition and chooses the first element as border value 
#and performs quick sort algorithm. 
def partition(data,start,end,drawData,timepause):
    border=start
    pivot=data[end]
    drawData(data,Colorarray(len(data),start,end,border,border))# drawdata called to show current state 
    time.sleep(timepause)
    for i in range(start,end):
        if data[i]<pivot:
            drawData(data,Colorarray(len(data),start,end,border,i,True))
            time.sleep(timepause)
            data[border],data[i]=data[i],data[border]
            border+=1
        drawData(data,Colorarray(len(data),start,end,border,i))
        time.sleep(timepause)
    
    drawData(data,Colorarray(len(data),start,end,border,end,True))
    # to show the final state after finishing one partition 
    time.sleep(timepause)
    data[border],data[end]=data[end],data[border]

    return border



def quicksort(data,start,end,drawData,timepause):
    if start<end:

        partitionindex=partition(data,start,end,drawData,timepause)

        quicksort(data,start,partitionindex-1,drawData,timepause)
        quicksort(data,partitionindex+1,end,drawData,timepause)

# color array to separate the different sections.    
def Colorarray(datalength,start,end,border,currentindex,swapped=False):
    colorarray=[]
    for i in range(datalength):
        if i>=start and i<=end:
            colorarray.append('green')
        else:
            colorarray.append('white')
        if i==end:
            colorarray[i]='blue'
        elif i==border:
            colorarray[i]='red'
        elif i==currentindex:
            colorarray[i]='yellow'
        
        if swapped:
            if i==border or i==currentindex:
                colorarray[i]='green'
        
    return colorarray

        


