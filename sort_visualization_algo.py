from tkinter import * 
from tkinter import ttk 
import random 
from bubble_sort import bubblesort
from quick_sort import quicksort
from merge_sort import mergesort

root=Tk()# It is the main window of GUI. 
root.title("Sorting Visualisation algorithms")
width=root.winfo_screenwidth()# setting the width according to screen width.
height=root.winfo_screenheight()# setting the height according to screen height.
root.geometry("%dx%d" %(width,height))
root.config(bg='#082A46')
selected_algorithm=StringVar() # this function holds a string
data=[]
def drawData(data,color):
    canvas.delete("all")
    c_height=650 # setting height
    c_width=1490 #setting width
    x_width=c_width/(len(data)+1)
    offset=30
    spacing=10
    scaleddata=[i/max(data) for i in data] # down scaling the data  
    for b,height in enumerate(scaleddata):
        x0=b*x_width+offset+spacing
        y0=c_height-height*340 #upscaling the data.
        x1=(b+1)*x_width+offset
        y1=c_height

        canvas.create_rectangle(x0,y0,x1,y1,fill=color[b])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[b]))
    root.update_idletasks()# used to complete the pending tasks .



    

def Generate():
    #data=[10,20,30,40]
    global data

    mini=int(minentry.get()) # getting the minimum value
   
   
    maxi=int(maxentry.get()) # getting the maximum value
    

    
    size=int(sizeentry.get()) # getting the size of array
   
    
    data=[]
    for _ in range(size):
        data.append(random.randrange(mini,maxi+1)) # appending random numbers in the data array
    


    drawData(data,['black' for x in range(len(data))]) # initially setting up the whole array as black.
def Startalgorithm():
    global data
    if not data:return
    if(algomenu.get()=='Bubble Sorting'):
       bubblesort(data,drawData,speedscale.get()) # calling bubble sort function
    elif(algomenu.get()=='Quick Sorting'):
        quicksort(data,0,len(data)-1,drawData,speedscale.get())  # calling quick sort function
    elif(algomenu.get()=='Merge Sorting'):
        mergesort(data,drawData,speedscale.get())  # calling merge sort function
    drawData(data,['green' for x in range(len(data))])# returning the sorted array after finishing sorting. 


     



UI_frame=Frame(root, width=1490,height=650,bg='grey')# setting the geometry of root frame.
UI_frame.grid(row=0,column=0,padx=10,pady=5)# orientation in x and y axis

canvas = Canvas (root,width=1490,height=650,bg='white')# this is used to create separate windows in main window
canvas.grid(row=1,column=0,padx=10,pady=5)


#row[0]
Label(UI_frame,text="Sorting Algorithm: ",bg='grey').grid(row=0,column=0,padx=5,pady=5,sticky=W)
algomenu=ttk.Combobox(UI_frame,textvariable=selected_algorithm,values=['Bubble Sorting','Merge Sorting','Quick Sorting'])
# Combobox provides a drop down menu and various other options which user can choose. 
algomenu.grid(row=0,column=1,padx=5,pady=5)
algomenu.current(0)
speedscale=Scale(UI_frame,from_=0.1,to=3.0,length=200,digits=2,resolution=0.2,orient=HORIZONTAL,label="Select speed [s]")
# scale is used to provide a slide bar through which user can set value to visualize algo accordingly. 
speedscale.grid(row=0,column=2,padx=5,pady=5)
Button(UI_frame,text="Start",command=Startalgorithm,bg='red').grid(row=0,column=3,padx=5,pady=10)
# button on clicking goes to the function written after command and performs accordingly.

sizeentry=Scale(UI_frame,from_=3,to=30,resolution=1,orient=HORIZONTAL,label="Size of Data")
sizeentry.grid(row=1,column=0,padx=5,pady=5)
# slide bar for the size of the array

minentry=Scale(UI_frame,from_=1,to=100,resolution=1,orient=HORIZONTAL,label="Minimum value")
minentry.grid(row=1,column=1,padx=5,pady=5)
# slide bar for setting the  minimum value of the array

maxentry=Scale(UI_frame,from_=1,to=100,resolution=1,orient=HORIZONTAL,label="Maximum value")
maxentry.grid(row=1,column=2,padx=5,pady=5)
# slide bar for setting the  maximum value of the array
#row[1]
Button(UI_frame,text="Generate",command=Generate,bg='red').grid(row=1,column=3,padx=5,pady=10)
root.mainloop()