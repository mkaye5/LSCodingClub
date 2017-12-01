from PIL import ImageTk, Image

class Character():
    def __init__(self, c, coords, type="circle", image="none"):
        """ initializes an object of the Database class.
                Parameters
                ----------
                root : the tk class object defined
                canvas : the canvas made
                coords : the starting coordinates for the character
                type : optional; the type of the object. Will change to item.
                image : optional; the image for the object to have
                """
        self.canvas = c
        if type == "circle":
            self.chara = self.canvas.create_oval(coords, outline="#f11", fill="#1f1", width=2)
        else:
            self.chara = self.canvas.create_oval(coords, outline="#f11", fill="#1f1", width=2)

    def key(self, event):
        '''
        Here's your assignment!
        Create a little program that checks what key the user is
        pressing down, and then move the character.
        You can use WASD or the arrow keys, whichever you'd prefer!

        HINTS:
            The computer will automatically give you the
            key you're pressing when you type event.char
            For example, if you press the w key event.char will give you 'w'
            Is there a way to see if event.char is equal to a certain character...?

            To move the character, use this function:
            self.canvas.move(self.chara, (how much to move side to side), (how much to move down))
            EXAMPLE:
                self.canvas.move(self.chara, 5, 10) will move the character
                5 spaces to the right and 10 spaces up.

            computer-speak for the arrow keys is a little different.
            Down: '\uf700'
            Up: '\uf701'
            Left: '\uf702'
            Right: '\uf703'

        '''
        #Your code here!