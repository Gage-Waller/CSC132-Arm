
import psutil
import time
import os
import tkinter as tk
from tkinter import ttk
import serial

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flush()

def readFile(file):
    statList = []
    finalstatList = []
    with open(file) as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                statList.append(line)
    for stat in statList:
        updatedStat = stat.rstrip('\n') and stat.rstrip()
        finalstatList.append(updatedStat)
    return finalstatList

file_to_read = r"/media/raspberry/16 GB Volume/Preset_maker/data.txt"
write_to_file = r"/home/raspberry/Desktop/PresetSelector/database.txt"

# Check if the source file exists and copy its contents
if os.path.exists(file_to_read):
    with open(file_to_read, "r", encoding="utf-8") as file:
        data = file.read()

    data = f'{data}\n'

    with open(write_to_file, "a", encoding="utf-8") as file:
        file.write(data)
        print("Added data from flash drive:", data)

class ListFrame(ttk.Frame):
    def __init__(self, parent, item_list, item_height):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        # widget data
        self.item_list = item_list
        self.item_number = len(item_list)
        self.list_height = self.item_number * item_height

        # canvas 
        self.canvas = tk.Canvas(self, background='red', scrollregion=(0, 0, self.winfo_width(), self.list_height))
        self.canvas.pack(expand=True, fill='both')

        # display frame
        self.frame = ttk.Frame(self)
        
        for item in self.item_list:
            self.create_item(item).pack(expand=True, fill='both', pady=4, padx=10)

        # scrollbar 
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

        # events
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
        self.bind('<Configure>', self.update_size)

    def update_size(self, event):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        else:
            height = self.winfo_height()
            self.scrollbar.place_forget()
        
        self.canvas.create_window(
            (0, 0), 
            window=self.frame, 
            anchor='nw', 
            width=self.winfo_width(), 
            height=height)

    def create_item(self, item):
        frame = ttk.Frame(self.frame)

        # grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 2), weight=1, uniform='a')

        # widgets 
        ttk.Label(frame, text=item, font=('Arial', 10)).grid(row=0, column=0, sticky='w', padx=10)
        ttk.Button(frame, text='Select', command=lambda i=item: self.select_preset(i)).grid(
            row=0, column=1, sticky='nsew', padx=5)
        ttk.Button(frame, text='Delete', command=lambda i=item: self.delete_preset(i)).grid(
            row=0, column=2, sticky='nsew', padx=5)

        return frame
    
    def select_preset(self, preset_name):
        print(f"Selected preset: {preset_name}")
        get_servo_values(preset_name)
        set_servo_values(values)
        time.sleep(1)
        
    
    def delete_preset(self, preset_name):
        print(f"Deleted preset: {preset_name}")


def unselect():
    ser.write("0,0,0,0,0,0,0\n".encode('utf-8'))
    return print("Grip Unselected")
    
        

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Preset Selector')

# uses the dictionary created from database to get each buttons respective list of values
def get_servo_values(name):
    values = (presetNames[name])
    print(type(values))
    return values

# sends the servo values to the arduino via serial communication
def set_servo_values(list):
    A1 = list[0]
    A2 = list[1]
    A3 = list[2]
    A4 = list[3]
    A5 = list[4]
    A6 = list[5]
    A7 = list[6]
    ser.write(f"{A1},{A2},{A3},{A4},{A5},{A6},{A7}\n".encode('utf-8'))
    print('servo data sent')
    return

# Checks if the file path exists of database.txt
# if so convert the string into a key dictionary of name and values, values being a list of all numbers
if os.path.exists(write_to_file):
    rawNames = readFile(write_to_file)
    print("Raw Names:", rawNames)
    presetNames = {
        
    }
    for seclist in rawNames:
        newSeclist = seclist.split(',')
        name = newSeclist[0]
        values = newSeclist[1:]
        presetNames[name] = values
    
    print(presetNames)
    

else:
    presetNames = []

# Create the list frame
list_frame = ListFrame(window, presetNames, 50)

unselect_button = ttk.Button(window, text="Unselect Grip", command=unselect)
unselect_button.pack(pady=10)

# run 
window.mainloop()
