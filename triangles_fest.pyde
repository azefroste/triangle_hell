from random import choice
from time import time
import cell_obj

saved = False

# const
SAVE_FILE_PATH = "D:/Generative-art-save/triangles_fest/"

BG_PALETTE = [(97, 46, 52), (237, 76, 97), (242, 208, 213), (235, 113, 129), (133, 49, 60)]
FG_PALETTE = [(209, 50, 79), (207, 138, 151), (33, 26, 27), (214, 13, 50), (84, 66, 69)]

W_SIZE = 1000
GRID_CELL = int(W_SIZE/5)

def draw_background(window_size , grid_size, color_palette, dim = True):
    """
    --  works better with monochromic palette  --
    
    window_size : well... the window size in pixels
    grid_size : how many time you want to divide the widow ( works best with a full division )
    color_palette : color palette ( list of tuples of RGB colors )
    dim : True set the alpha of the colors to 100 ( False to 255 )
    """
    # generate a grid of N square ( random colors from a palette )
    pixel_size = (window_size / grid_size)
    if dim :
        _alpha = 120
    else :
        _alpha = 256
    for x in range(0, grid_size) :
        for y in range(0, grid_size) :
            # taking a random color of the choosen palette
            r, g, b = choice(color_palette)
            fill(r, g, b, _alpha)
            square(x * pixel_size, y * pixel_size, pixel_size)
        

def mousePressed():
    global saved
    saved = False
    redraw()
    
    
def keyPressed():
    # save the canvas as a .png in the given path
    global saved
    if key == "s" and not saved :
        saved = True
        file_name = str(int(time())) + ".png"
        save(SAVE_FILE_PATH + file_name)
    else :
        print("already saved")
        

def setup():
    size(W_SIZE, W_SIZE)
    noLoop()
    background(255)
    
    
  
def draw():
    cells = []
    fill(255)
    square(0, 0, W_SIZE)  # clear the canvas
    
    draw_background(W_SIZE, 5, BG_PALETTE, dim = True)
    
    for x in range(0, 5) :
        for y in range(0, 5) :
            noStroke()
            cells.append(cell_obj.cell(x * GRID_CELL, y * GRID_CELL, GRID_CELL, FG_PALETTE))
    
