# Webscraper Crossword v0.0 alpha
# Author: Paul Graham Jr.

# This main program file should allow for the building of a crossword puzzle based on a list of words

# imports ======================================================================================================/
# import pygame
from tkinter import *
# ==============================================================================================================/

# Main loop ====================================================================================================/
# Initialize
root = Tk()
root.title("Crossword")

cols = 15
rows = 15

# Make a 2d array with the abobe dimentions and fill it with 0s
grid = [0 for i in range(cols)]
for i in range(cols):
    grid[i] = [0 for i in range(rows)]

# read list of words and map them inside the grid (grid[x][y] = char)


# draw grid
for x in range(cols):
    for y in range(rows):
        # If grid[x][y] exists add an entry
        Entry(root, width=1).grid(row=x, column=y, padx=2)

# label = Label(root, text="Hi There").grid(row=0, column=0)

root.mainloop()
# ==============================================================================================================/