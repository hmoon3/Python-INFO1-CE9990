"""
tkinterexample.py
assignment #3
draw the flag of Denmark using tkinter
"""

import math
import sys
import tkinter


height = 280
width = int(height * 37/38)

def drawPixel(x, y, color):
    """
    Color the pixel at coordinates at (x, y).
    """
    assert isinstance(x, int) and isinstance(y, int) and isinstance(color, str)
    canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = color)

red   = "#D81E05"
white = "#FFFFFF"


root = tkinter.Tk()
root.title ("Denmark")
root.geometry(str(width) + "x" + str(height))
canvas = tkinter.Canvas(root, highlightthickness = 0, background = red)

for y in range(height):
    for x in range(width):
        if x > int(height * 3/7) and x < int(height * 4/7) or y > int(height * 3/7) and y < int(height * 4/7):
            drawPixel(x, y, white)    

canvas.pack(expand = tkinter.YES, fill = "both")
root.mainloop()

sys.exit(0)
