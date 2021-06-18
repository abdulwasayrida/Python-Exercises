#Exercise 9.7
#Display an 8 X 8 Grid
#Rida Abdulwasay
#1/18/2018

from tkinter import *

class Grid:
    def __init__(self):
        window = Tk()
        window.title("Grid")

        width = 200
        height = 200
        
        self.canvas = Canvas(window, width = 200, height = 200)
        self.canvas.pack()
        
        for x in range (8):
            self. canvas.create_line(0, x * height / 8, width, x * height / 8, fill = "blue")
            self. canvas.create_line(x * width / 8, 0, x * width / 8, height, fill = "red")

        window.mainloop()
Grid ()
