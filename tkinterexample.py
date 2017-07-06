"""
tkinterexample.py
assignment #3
draw the flag of Denmark using tkinter
"""

import math
import sys
import tkinter


height = 280
width = 370

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


y = 0
while y < height:
    x = 0
    while x < width:
        if (x > 120 and x < 160) or (y > 120 and y < 160):
            drawPixel(x, y, white)
        x += 1
    y += 1


canvas.pack(expand = tkinter.YES, fill = "both")
root.mainloop()

sys.exit(0)
