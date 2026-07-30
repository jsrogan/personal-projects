from tkinter import *

expr = ""
new = False

def press_number(key):
    global expr, new

    key = str(key)

    # If the last action was "=" and the user presses a number,
    # start a new calculation.
    if new:
        expr = key
        new = False
    else:
        expr += key

    display.set(expr)

def press_decimal():
    global expr, new

    # If the last action was "=" and the user presses ".",
    # start a new decimal number.
    if new:
        expr = "0."
        new = False
    else:
        expr += "."

    display.set(expr)

def press_operator(operator):
    global expr, new

    # If the last action was "=", keep the result and append the operator.
    # If not, just append the operator as usual.
    expr += operator
    new = False

    display.set(expr)

def equal():
    global expr, new

    try:
        result = str(eval(expr))
        display.set(result)

        # Store the result so the user can continue with another operator.
        expr = result
        new = True

    except:
        display.set("error")
        expr = ""
        new = False

def clear():
    global expr, new

    expr = ""
    new = False
    display.set("")

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="light blue")
    root.title("Simple Calculator")
    root.geometry("400x200")

    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=4, ipadx=140)

    # Number buttons
    btn1 = Button(root, text='1', fg='black', bg='light grey', command=lambda: press_number(1), height=1, width=7)
    btn1.grid(row=2, column=0)
    btn2 = Button(root, text='2', fg='black', bg='light grey', command=lambda: press_number(2), height=1, width=7)
    btn2.grid(row=2, column=1)
    btn3 = Button(root, text='3', fg='black', bg='light grey', command=lambda: press_number(3), height=1, width=7)
    btn3.grid(row=2, column=2)
    btn4 = Button(root, text='4', fg='black', bg='light grey', command=lambda: press_number(4), height=1, width=7)
    btn4.grid(row=3, column=0)
    btn5 = Button(root, text='5', fg='black', bg='light grey', command=lambda: press_number(5), height=1, width=7)
    btn5.grid(row=3, column=1)
    btn6 = Button(root, text='6', fg='black', bg='light grey', command=lambda: press_number(6), height=1, width=7)
    btn6.grid(row=3, column=2)
    btn7 = Button(root, text='7', fg='black', bg='light grey', command=lambda: press_number(7), height=1, width=7)
    btn7.grid(row=4, column=0)
    btn8 = Button(root, text='8', fg='black', bg='light grey', command=lambda: press_number(8), height=1, width=7)
    btn8.grid(row=4, column=1)
    btn9 = Button(root, text='9', fg='black', bg='light grey', command=lambda: press_number(9), height=1, width=7)
    btn9.grid(row=4, column=2)
    btn0 = Button(root, text='0', fg='black', bg='light grey', command=lambda: press_number(0), height=1, width=7)
    btn0.grid(row=5, column=0)

    # Operator buttons
    plus = Button(root, text='+', fg='black', bg='light grey', command=lambda: press_operator('+'), height=1, width=7)
    plus.grid(row=2, column=3)
    minus = Button(root, text='-', fg='black', bg='light grey', command=lambda: press_operator('-'), height=1, width=7)
    minus.grid(row=3, column=3)
    mult = Button(root, text='*', fg='black', bg='light grey', command=lambda: press_operator('*'), height=1, width=7)
    mult.grid(row=4, column=3)
    div = Button(root, text='/', fg='black', bg='light grey', command=lambda: press_operator('/'), height=1, width=7)
    div.grid(row=5, column=3)
    mod = Button(root, text='%', fg='black', bg='light grey', command=lambda: press_operator('%'), height=1, width=7)
    mod.grid(row=6, column=3)

    # Other buttons
    eq = Button(root, text='=', fg='black', bg='light grey', command=equal, height=1, width=7)
    eq.grid(row=5, column=2)
    clr = Button(root, text='Clear', fg='black', bg='light grey', command=clear, height=1, width=7)
    clr.grid(row=5, column=1)
    dot = Button(root, text='.', fg='black', bg='light grey', command=press_decimal, height=1, width=7)
    dot.grid(row=6, column=0)

    root.mainloop()
