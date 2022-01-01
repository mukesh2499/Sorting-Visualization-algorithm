import time

def mergesort(data,drawData,timepause):
    merge_sorting_algo(data,0,len(data)-1,drawData,timepause)

def merge_sorting_algo(data,low,high,drawData,timepause):
    # this function just performs recursion for each partition and merges two parition.
        if low<high:
            mid=(low+high)//2
            merge_sorting_algo(data,low,mid,drawData,timepause)
            merge_sorting_algo(data,mid+1,high,drawData,timepause)
            merge(data,low,mid,high,drawData,timepause)

def merge(data,low,mid,high,drawData,timepause):
    drawData(data,Colorarray(len(data),low,mid,high)) # initially calling the drawdata array to show while merging
    time.sleep(timepause) # used to take a pause of time given as an argument.
      # below is the merging algorithm.
    left=data[low:mid+1]
    right=data[mid+1:high+1]
    leftidx=rightidx=0
    for dataidx in range(low,high+1):
        if leftidx<len(left) and rightidx<len(right):
            if left[leftidx]<=right[rightidx]:
                data[dataidx]=left[leftidx]
                leftidx+=1
            else:
                data[dataidx]=right[rightidx]
                rightidx+=1
        elif  leftidx<len(left):
                data[dataidx]=left[leftidx]
                leftidx+=1
        else:
                data[dataidx]=right[rightidx]
                rightidx+=1
    drawData(data,["green" if x>=low and x<=high else "white" for x in range(len(data))]) 
    # separating the partition and showing with different colors to visualize. 
    time.sleep(timepause)
# color array to separate the different sections.
def Colorarray(length,low,mid,high):
    colorarray=[]

    for i in range(length):
        if i>=low and i<=high:
            if i>=low and i<=mid:
                colorarray.append("orange")
            else:
                colorarray.append("yellow")
        else:
            colorarray.append("white")
        
    return colorarray
