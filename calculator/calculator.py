from tkinter import *
calculator =  Tk()
calculator.title("CALCULATOR")
calculator.configure(background = "blue")
calculator.geometry('445x440')
expression = ""
def press(num): 
    global expression 
    expression = expression + num
    text.set(expression)
def equalpress(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        text.set(total)
        expression = ""
    except: 
        text.set("invalid expression") 
        expression = "" 
def clear(): 
    global expression 
    expression = "" 
    text.set("") 
text = StringVar()
#entry box
textinput = Entry (calculator, font = ("algerian",22),width = 26, textvariable = text)
textinput.grid(row=0,column=0,columnspan=6,pady=3)

#buttons and entry box
b1 = Button (calculator,text = '1',font = ('algerian',25), width = 5,height = 2 , bg = "white",fg = 'black',command = lambda:press('1'))
b1.grid(row = 3 ,column = 0)

b2 = Button (calculator,text = '2',font = ('algerian',25), width = 5,height = 2 ,bg = "white",fg = 'black',command = lambda:press('2'))
b2.grid(row = 3 ,column = 1)

b3 = Button (calculator,text = '3',font = ('algerian',25),width = 5,height = 2 , bg = "white",fg = 'black',command = lambda:press('3'))
b3.grid(row = 3 ,column = 2)

b4 = Button (calculator,text = '4',font = ('algerian',25), width = 5,height = 2 ,bg = "white",fg = 'black',command = lambda:press('4'))
b4.grid(row = 4 ,column = 0)

b5 = Button (calculator,text = '5',font = ('algerian',25),width = 5,height = 2 , bg = "white",fg = 'black',command = lambda:press('5'))
b5.grid(row = 4 ,column = 1)

b6 = Button (calculator,text = '6',font = ('algerian',25),width = 5,height = 2 , bg = "white",fg = 'black',command = lambda:press('6'))
b6.grid(row = 4 ,column = 2)

b7 = Button (calculator,text = '7',font = ('algerian',25),width = 5,height = 2 , bg = "white",fg = 'black',command = lambda:press('7'))
b7.grid(row = 5 ,column = 0)

b8 = Button (text = '8',font = ('algerian',25),width = 5,height = 2 , bg = "white",fg = 'black',command = lambda:press('8'))
b8.grid(row = 5 ,column = 1)

b9 = Button (text = '9',font = ('algerian',25),width = 5,height = 2 , bg = "white",fg = 'black',command = lambda:press('9'))
b9.grid(row = 5 ,column = 2)

b0 = Button (text = '0',font = ('algerian',25),width = 5,height = 2 , bg = "white",fg = 'black',command = lambda:press('0'))
b0.grid(row = 6 ,column = 0)

add= Button (text = '+',font = ('algerian',25),width = 5,height = 2 , bg = "white",fg = 'black',command = lambda:press('+'))
add .grid(row = 3 ,column = 3)

sub = Button (text = '- ',font = ('algerian',25),width = 5,height = 2 , bg = "white",fg = 'black',command = lambda:press('-'))
sub.grid(row = 4 ,column = 3)

div = Button (text = '/',font = ('algerian',25), width = 5,height = 2 ,bg = "white",fg = 'black',command = lambda:press('/'))
div.grid(row = 5 ,column = 3)

mul = Button (text = '*',font = ('algerian',25),width = 5,height = 2 , bg = "white",fg = 'black',command = lambda:press('*'))
mul.grid(row = 6,column = 3)

equal  = Button (text = '=',font = ('algerian',25), width = 5,height = 2 ,bg = "white",fg = 'black',command = equalpress)
equal.grid(row = 6,column = 2)

clear = Button (text = ' clear ',font = ('algerian',25),width = 5,height = 2 , bg = "white",fg = 'black',command = clear)
clear.grid(row = 6,column = 1)

calculator.mainloop()


