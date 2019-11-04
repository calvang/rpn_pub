#!/usr/bin/env python3
from tkinter import *
import operator
import readline

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,  
    #'%': operator.mod
}

input = ""

def calculate(myarg):
    stack = list()
    # TODO convert matrix string into np.array
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            # TODO handle stack of brackets 
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def pressNum(number):
    global input
    input = input + str(number) + " "
    equation.set(input)

def pressOp(op):
    global input
    input = input + str(op)
    equation.set(input)

def pressEnter():
    global input
    result = str(calculate(input))
    equation.set(result)
    input = ""

def clearscreen():
    global input
    input = ""
    equation.set("")
'''
def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)
'''

if __name__ == '__main__':
    gui = Tk()
    gui.configure(background="black")
    gui.title("RPN Calculator")
    gui.geometry() #do I need values?
    equation = StringVar()
    inputField = Entry(gui, textvariable=equation)
    inputField.grid(columnspan=4, ipadx=70)
    equation.set("")

    button0 = Button(gui, text=' 0 ', fg='black', bg='white',command=lambda: pressNum(0), height=4, width=6)
    button0.grid(row=5, column=0)
    button1 = Button(gui, text=' 1 ', fg='black', bg='white',command=lambda: pressNum(1), height=4, width=6)
    button1.grid(row=2, column=0)
    button2 = Button(gui, text=' 2 ', fg='black', bg='white',command=lambda: pressNum(2), height=4, width=6)
    button2.grid(row=2, column=1)
    button3 = Button(gui, text=' 3 ', fg='black', bg='white',command=lambda: pressNum(3), height=4, width=6)
    button3.grid(row=2, column=2)
    button4 = Button(gui, text=' 4 ', fg='black', bg='white',command=lambda: pressNum(4), height=4, width=6)
    button4.grid(row=3, column=0)
    button5 = Button(gui, text=' 5 ', fg='black', bg='white',command=lambda: pressNum(5), height=4, width=6)
    button5.grid(row=3, column=1)
    button6 = Button(gui, text=' 6 ', fg='black', bg='white',command=lambda: pressNum(6), height=4, width=6)
    button6.grid(row=3, column=2)
    button7 = Button(gui, text=' 7 ', fg='black', bg='white',command=lambda: pressNum(7), height=4, width=6)
    button7.grid(row=4, column=0)
    button8 = Button(gui, text=' 8 ', fg='black', bg='white',command=lambda: pressNum(8), height=4, width=6)
    button8.grid(row=4, column=1)
    button9 = Button(gui, text=' 9 ', fg='black', bg='white',command=lambda: pressNum(9), height=4, width=6)
    button9.grid(row=4, column=2)

    add = Button(gui, text=' + ', fg='black', bg='white',command=lambda: pressOp("+"), height=4, width=6)
    add.grid(row=2, column=3)
    subtract = Button(gui, text=' - ', fg='black', bg='white',command=lambda: pressOp("-"), height=4, width=6)
    subtract.grid(row=3, column=3)
    multiply = Button(gui, text=' * ', fg='black', bg='white',command=lambda: pressOp("*"), height=4, width=6)
    multiply.grid(row=4, column=3)
    divide = Button(gui, text=' / ', fg='black', bg='white',command=lambda: pressOp("/"), height=4, width=6)
    divide.grid(row=5, column=3)
    power = Button(gui, text=' exp ', fg='black', bg='white',command=lambda: pressOp("^"), height=4, width=6)
    power.grid(row=6, column=3)

    enter = Button(gui, text=' Enter ', fg='black', bg='white',command=lambda: pressEnter(), height=4, width=18)
    enter.grid(row=6, column=0,columnspan=3)
    clear = Button(gui, text=' Clear ', fg='black', bg='white',command=lambda: clearscreen(), height=4, width=12)
    clear.grid(row=5, column=1,columnspan=2)
    gui.mainloop()
    #main()
