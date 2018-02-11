from display import *
from draw import *
import random

screen = new_screen()
color = [222,222,0]

#octave 1
draw_line(0,YRES/2,XRES,YRES/2,screen,color)
draw_line(0,125,XRES,YRES-125,screen,color)
draw_line(0,0,XRES,YRES,screen,color)

#octave 2
draw_line(125,0,375,YRES,screen,color)

#octave 7
draw_line(125,YRES,375,0,screen,color)
draw_line(XRES/2,YRES,XRES/2,0,screen,color)

#octave 8
draw_line(0,YRES-125,XRES,125,screen,color)
draw_line(0,YRES,XRES,0,screen,color)

display(screen)
#save_extension(screen, 'img.png')
