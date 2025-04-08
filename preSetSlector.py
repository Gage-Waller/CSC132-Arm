from tkinter import *
from time import sleep
import os

filePath = 'data.txt' # PLACEHOLDER

#this is the initial time stamp for the data
firstTimeStamp = os.path.getmtime(filePath)


#reads new data

def readFile(file):
    DATA = []
    with open(file) as file:
        for line in file :
            DATA.append(line)
    
    return DATA


# check for changes in the data text file

data = readFile(filePath)

while(True):
    
    currentTimeStamp = os.path.getmtime(filePath)
    if(currentTimeStamp != firstTimeStamp):
        data = readFile(filePath)
        print(data)

    else:
        print(data)
        
    sleep(1) #pauses for one second

# updates GUI with info from DATA

#MAIN
window = Tk()

window.Geometry('Fullscreen')
window.title('Preset Selector')

window.mainloop()