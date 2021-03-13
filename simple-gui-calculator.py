#!/usr/bin/env python3
from tkinter import *

root = Tk()
root.geometry('150x155')
root.title('Calc')

expression = ''

def eval_expression():
    global expression
    result = eval(expression)
    expression = str(result)
    expression_field.config(text = expression)

def append_expression(button_arg):
    global expression
    text = str(expression+button_arg)
    expression = text
    expression_field.config(text = expression)

def clear_expression():
    global expression
    expression = ''
    expression_field.config(text = expression)

def null():
    pass

eval_button = Button(root, text="=", command=eval_expression)
expression_field = Label(text=expression)

# Numbers
one_button          =   Button(   root, text="1", command= lambda: append_expression("1"))
two_button          =   Button(   root, text="2", command= lambda: append_expression("2"))
three_button        =   Button(   root, text="3", command= lambda: append_expression("3"))
four_button         =   Button(   root, text="4", command= lambda: append_expression("4"))
five_button         =   Button(   root, text="5", command= lambda: append_expression("5"))
six_button          =   Button(   root, text="6", command= lambda: append_expression("6"))
seven_button        =   Button(   root, text="7", command= lambda: append_expression("7"))
eight_button        =   Button(   root, text="8", command= lambda: append_expression("8"))
nine_button         =   Button(   root, text="9", command= lambda: append_expression("9"))
zero_button         =   Button(   root, text="0", command= lambda: append_expression("0"))

# Operators & Actions
plus_button         =   Button(   root, text="+", command= lambda: append_expression("+"))
minus_button        =   Button(   root, text="-", command= lambda: append_expression("-"))
divide_button       =   Button(   root, text="/", command= lambda: append_expression("/"))
multiply_button     =   Button(   root, text="*", command= lambda: append_expression("*"))
decimal_button      =   Button(   root, text=".", command= lambda: append_expression("."))
clear_button        =   Button(   root, text="C", command=clear_expression)

expression_field    .grid(column=0, row=0)
eval_button         .grid(column=2, row=4)
one_button          .grid(column=0, row=1)
two_button          .grid(column=1, row=1)
three_button        .grid(column=2, row=1)
four_button         .grid(column=0, row=2)
five_button         .grid(column=1, row=2)
six_button          .grid(column=2, row=2)
seven_button        .grid(column=0, row=3)
eight_button        .grid(column=1, row=3)
nine_button         .grid(column=2, row=3)
zero_button         .grid(column=1, row=4)
decimal_button      .grid(column=0, row=4)
clear_button        .grid(column=3, row=0, columnspan=1)
plus_button         .grid(column=3, row=1)
minus_button        .grid(column=3, row=2)
divide_button       .grid(column=3, row=3)
multiply_button     .grid(column=3, row=4)

root.bind("+", lambda x: append_expression("+") )

# Numbers
root.bind("1", lambda x: append_expression("1"))
root.bind("2", lambda x: append_expression("2"))
root.bind("3", lambda x: append_expression("3"))
root.bind("4", lambda x: append_expression("4"))
root.bind("5", lambda x: append_expression("5"))
root.bind("6", lambda x: append_expression("6"))
root.bind("7", lambda x: append_expression("7"))
root.bind("8", lambda x: append_expression("8"))
root.bind("9", lambda x: append_expression("9"))
root.bind("0", lambda x: append_expression("0"))

# Operators & Actions
root.bind("+", lambda x: append_expression("+"))
root.bind("-", lambda x: append_expression("-"))
root.bind("/", lambda x: append_expression("/"))
root.bind("*", lambda x: append_expression("*"))
root.bind(".", lambda x: append_expression("."))
root.bind("c", lambda x: clear_expression())
root.bind("<Return>", lambda x: eval_expression())
root.bind("=", eval_expression)

root.mainloop()
