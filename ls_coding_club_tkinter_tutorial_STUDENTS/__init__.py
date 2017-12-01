import tkinter as tk
from character.character import Character

root = tk.Tk()

C = tk.Canvas(root, bg="blue", height=500, relief="sunken", width=600)

coords = 10, 50, 240, 210
chara = Character(C, coords)

frame = tk.Frame(root, width=100, height=100)
frame.bind("<KeyPress>", chara.key)
frame.pack()
frame.focus_set()

C.pack()
root.mainloop()