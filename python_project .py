from datetime import datetime
import schedule
import time
import tkinter as tk

window = tk.Tk()
window.title("Greetings")
window.geometry("400x400")


'''''
# Label
label1 = tk.Label1(text= "welcome to pay")
label1.grid(colunm=0,row=0)

# Button
button1=tk.Button1(text= "Click me! ")
button1.grid(colunm=0, row=0)

# Entry field
entry_field1=tk.entry()
entry_field1. grid(colunm=0,row=2)

'''
window.mainloop()

import csv

with open('pay.csv','w+') as csvfile:
    myfile=csv.writer(csvfile)
    myfile.writerow(["hours","rate","wage"])


# Defining the function
    def pay(hours):
        rate= 5
        wage = float(hours) * 5
        return wage
    # Collecting user input
    hours = input("Enter the hours: ")
    Currency ='USD'

    print()
    print(str(Currency)+ str(pay(hours)))





