from tkinter import *

# Elements that will be shown on screen and changes will be made
SCREEN = ''

def press(element: str):
    # Add element to screen
    # If added element is an operation
    # And the previos one is an operation too
    # Then last pressed operation will be added
    # And previous one will be removed
    global SCREEN

    if SCREEN and not SCREEN[-1] in ('(',')') and not SCREEN[-1].isnumeric() \
        and not element.isnumeric() and not element in ('(',')'):
        s = len(SCREEN) - 1
        SCREEN = SCREEN[0:s]
    
    SCREEN += element
    t.set(SCREEN)

def clear():
    # Remove last added element from screen
    global SCREEN
    
    s = len(SCREEN) - 1
    SCREEN = SCREEN[0:s]
    t.set(SCREEN)

def equal():
    # Show result of the operations
    # And return 'error'
    # If error ocurres
    global SCREEN   

    try:
        total = str(eval(SCREEN.strip()))
        SCREEN = total
        t.set(SCREEN)
    
    except:
        total = 'error'
        SCREEN = ''
        t.set(total)

def clear_all():
    # Clear all elements on screen
    global SCREEN

    SCREEN = ''
    t.set(SCREEN)

window = Tk()
window.title('Calculator')
window.configure(bg='black')

# String variable to show on screen
t = StringVar()

# Main screen
entry = Entry(window,
textvariable=t,
font=('monospace',30),
foreground='green',
background='black'
)
entry.grid(row=1,column=1,columnspan=4,pady=20)

# First row of buttons
btn1 = Button(window,
text='1',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('1')
)
btn1.grid(row=2,column=1,pady=20)

btn2 = Button(window,
text='2',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('2')
)
btn2.grid(row=2,column=2)

btn3 = Button(window,
text='3',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('3')
)
btn3.grid(row=2,column=3)

btnmul = Button(window,
text='*',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('*')
)
btnmul.grid(row=2,column=4)

# Second row of buttons
btn4 = Button(window,
text='4',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('4')
)
btn4.grid(row=3,column=1,pady=20)

btn5 = Button(window,
text='5',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('5')
)
btn5.grid(row=3,column=2)

btn6 = Button(window,
text='6',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('6')
)
btn6.grid(row=3,column=3)

btndiv = Button(window,
text='/',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('/')
)
btndiv.grid(row=3,column=4)

# Third row of buttons
btn7 = Button(window,
text='7',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('7')
)
btn7.grid(row=4,column=1,pady=20)

btn8 = Button(window,
text='8',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('8')
)
btn8.grid(row=4,column=2)

btn9 = Button(window,
text='9',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('9')
)
btn9.grid(row=4,column=3)

btnadd = Button(window,
text='+',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('+')
)
btnadd.grid(row=4,column=4)

# Fourth row of buttons
btnp1 = Button(window,
text='(',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('(')
)
btnp1.grid(row=5,column=1,pady=20)

btnp2 = Button(window,
text=')',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press(')')
)
btnp2.grid(row=5,column=2)

btn0 = Button(window,
text='0',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('0')
)
btn0.grid(row=5,column=3)

btnsub = Button(window,
text='-',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('-')
)
btnsub.grid(row=5,column=4)

# Fifth row of buttons
btndot = Button(window,
text='.',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: press('.')
)
btndot.grid(row=6,column=1,pady=20)

btnc = Button(window,
text='<-',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: clear()
)
btnc.grid(row=6,column=2)

btnclear = Button(window,
text='C',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: clear_all()
)
btnclear.grid(row=6,column=3)

btnequals = Button(window,
text='=',
background='black',
foreground='red',
activeforeground='green',
activebackground='black',
font=('monospace',20),
command = lambda: equal()
)
btnequals.grid(row=6,column=4)

# You can delete this part
label = Label(window,
text = 'https://github.com/JosephJuska',
font = ('monospace',30),
background='black',
foreground='green'
)
label.grid(row=7,column=1,columnspan = 4)

# Start the programme
window.mainloop()