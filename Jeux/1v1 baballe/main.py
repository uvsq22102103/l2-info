import tkinter as tk

def move_player1(self):
    print(self)

def move_player2(self):
    print(self)

def move(tagOrId):
    pass

HEIGHT, WIDTH = 300, 500
PLAYER_SIZE = 40

root = tk.Tk()
root.title("Jeu de la baballe")
root.config(height=HEIGHT, width=WIDTH)

canvas = tk.Canvas(root,bg="black",height=HEIGHT,width=WIDTH)

canvas.grid(row=0,column=0)

#Create players#
player1 = canvas.create_rectangle(5,(HEIGHT/2)+PLAYER_SIZE,15,HEIGHT/2,fill="green")
player2 = canvas.create_rectangle(WIDTH-15,(HEIGHT/2)+PLAYER_SIZE,WIDTH-5,HEIGHT/2,fill="green")
################
#canvas.moveto(player1)
#canvas.moveto(player2)

root.bind("<z>", lambda self:move_player1(self))
root.bind("<s>", lambda self:move_player1(self))

root.bind("<Up>", lambda self:move_player2(self))
root.bind("<Down>", lambda self:move_player2(self))
root.mainloop()