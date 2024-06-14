from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(400, 200)
window.config(padx=30, pady=30)

myLabelWeight = Label(text="Enter Your Weight(kg):   ")
myLabelWeight.grid(row=0, column=0)

myEntryWeight = Entry(width=20)
myEntryWeight.grid(row=0, column=1)


def breakSpace(row, column):
    myLabelBreak = Label(text="---------------")
    myLabelBreak.grid(row=row, column=column)


def calculation():
    try:
        myHeight=float(myEntryHeight.get())
        myWeight = float(myEntryWeight.get())
        if myHeight >= 10.0 and myWeight>=10.0:
            BMI=myWeight/pow(myHeight/100,2)
            if BMI <= 18.4:
                BMIResult="Underweight"
            elif BMI <= 24.9 and BMI>=18.5:
                BMIResult = "Normal"
            elif BMI <= 39.9 and BMI>=25.0:
                BMIResult = "Overweight"
            else:
                BMIResult = "Obese"

            myLabelResult.config(text="BMI: {0}\n Result: {1}".format(BMI,BMIResult))
        else:
            myLabelResult.config(text="Please enter correct values\nThe Datas must be over 10.0")
    except:
        myLabelResult.config(text="Please do not enter\na data except number")

def clearAll():
    myEntryWeight.delete(0,'end')
    myEntryHeight.delete(0, 'end')
    myLabelResult.config(text="")

breakSpace(1, 0)

myLabelHeight = Label(text="Enter Your Height(cm):   ")
myLabelHeight.grid(row=2, column=0)

myEntryHeight = Entry(width=20)
myEntryHeight.grid(row=2, column=1)

breakSpace(3, 0)

myButton = Button(text="Calculate", command=calculation)
myButton.grid(row=4, column=0)
myClearButton = Button(text="Clear All", command=clearAll)
myClearButton.grid(row=4, column=1)

breakSpace(5, 0)

myLabelResult = Label(text="")
myLabelResult.grid(row=6, column=0)

window.mainloop()
