import tkinter as tk
from character.character import Character

root = tk.Tk()

'''edit the code below'''

C = tk.Canvas(root, bg='''any background color you want''', height='''pick one''', relief="sunken", width='''pick one''')
coords = #where you want the character to start
my_chararacter = #create a character here!

'''don't touch this code'''
frame = tk.Frame(root, width=100, height=100)
frame.bind("<KeyPress>", my_chararacter.key)
frame.pack()
frame.focus_set()
C.pack()
root.mainloop()