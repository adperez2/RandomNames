from tkinter.ttk import *
from tkinter import *
import random
from openpyxl import workbook, load_workbook
root= Tk()
root.title("Randomization lottery")
root.geometry("150x150")
root.resizable(0,0) #people cant expand
def randomname(event):
   wb = load_workbook("hello.xlsx")
   ws = wb.active
   rangeline = ws ["A2": "A19"]  #[] are to create a list
           #our list is names as rangeline above (we can name it anything)
   name = [] #creating an empty variable ready to take list
   for items in rangeline:  #this gave us cell value
       for subitems in items:   #I want what is inside the cell
           name.append(subitems.value) #change and save to variable called Name
   print(name)
   computer_action=random.choice(name)
   print("the computer randomly chose: " + computer_action)

   updateDisplay(computer_action)
def updateDisplay(abc):
   displayVariable.set(abc)

button_1 = Button(root, text ="Random Lottery Name")
button_1.bind("<Button-1>", randomname)
button_1.pack()
displayVariable = StringVar()
displayLabel=Label(root, textvariable=displayVariable)
displayLabel.pack()


mainloop()
