#import packages required
import tkinter as tk
from tkinter import StringVar, Frame

#defined the main window && setup the size
main_window = tk.Tk()
main_window.geometry("312x324") # set up size
#give it a name
main_window.title("My_Calculator")

#defined global variables -> this will be used in the functions, ensuring no out of scope error
expression = ""
input_text = StringVar() # stringVar is like an interpreter. get updated values

#creating functions 3
# #func handling numbers/operator click
def btn_click(item):
     global expression
     expression = expression + str(item) # string concat
     input_text.set(expression)

#func to clear input field
def btn_clear():
     global expression
     expression = ""
     input_text.set("")

#def func to evaluate the expression
def btn_equal():
     global expression
     try:
         result = str(eval(expression)) # evaluate the computation or expression
         input_text.set(result)
         expression = "" # clear the expression and ready for next operation
     except:
         input_text.set('Error')
         expression = ""

#build the widgets
input_frame: Frame = tk.Frame(main_window, width=312 , height=50, bd=0, highlightbackground='black', highlightcolor='black', highlightthickness=1) # top frame

#pack the frame using pack()
input_frame.pack(side = 'top') # use pack to align or set where you want the frame to be

#entry widget( inputs field)
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

#create bottom frame and widget
btns_frame = tk.Frame(main_window, width=312, height=272.5, bg='grey')
btns_frame.pack()

btn_clearing = tk.Button(btns_frame, text="Clear", fg= 'black' , width= 32, height=3, bd=0, bg="#eee", cursor= 'hand2' ,
                         command=btn_clear)
#position the bttn clear in the grid
btn_clearing.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
#create button for the operators ( /, *, +, -)
btn_div = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor= 'hand2' ,
                    command=lambda: btn_click("/")) # connect to the click func and it shows there
btn_div.grid(row=0, column=3,padx=1, pady=1)

#Third row includes 4 buttons, 7,8,9 and Multiply (*)
tk.Button(btns_frame, text= "7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor= 'hand2',
          command=lambda: btn_click("7")).grid(row=1, column=0, padx=1, pady=1)

tk.Button(btns_frame, text= "8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor= 'hand2',
          command=lambda: btn_click("8")).grid(row=1, column=1, padx=1, pady=1)
tk.Button(btns_frame, text= "9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor= 'hand2',
          command=lambda: btn_click("9")).grid(row=1, column=2, padx=1, pady=1)
tk.Button(btns_frame, text= "*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor= 'hand2',
          command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

#Second row includes 4 buttons, 4,5,6 and Substraction (-)
tk.Button(btns_frame, text= "4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor= 'hand2',
          command=lambda: btn_click("4")).grid(row=2, column=0, padx=1, pady=1)

tk.Button(btns_frame, text= "5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor= 'hand2',
          command=lambda: btn_click("5")).grid(row=2, column=1, padx=1, pady=1)
tk.Button(btns_frame, text= "6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor= 'hand2',
          command=lambda: btn_click("6")).grid(row=2, column=2, padx=1, pady=1)
tk.Button(btns_frame, text= "-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor= 'hand2',
          command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

#First row includes 4 buttons, 1,2,3 and Addition (+)
tk.Button(btns_frame, text= "1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor= 'hand2',
          command=lambda: btn_click("1")).grid(row=3, column=0, padx=1, pady=1)

tk.Button(btns_frame, text= "2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor= 'hand2',
          command=lambda: btn_click("2")).grid(row=3, column=1, padx=1, pady=1)
tk.Button(btns_frame, text= "3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor= 'hand2',
          command=lambda: btn_click("3")).grid(row=3, column=2, padx=1, pady=1)
tk.Button(btns_frame, text= "+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor= 'hand2',
          command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

#Last Row include 0,.,=
tk.Button(btns_frame, text= "0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor= 'hand2',
          command=lambda: btn_click("0")).grid(row=4, column=0, columnspan=2,  padx=1, pady=1)
tk.Button(btns_frame, text= ".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor= 'hand2',
          command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
tk.Button(btns_frame, text= "=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor= 'hand2',
          command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)



main_window.mainloop()