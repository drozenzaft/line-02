from display import *
from draw import *
import random

screen = new_screen()
color = [0,0,255]
#octave 1
'''for y in range(YRES/5):
    color = [random.randint(0,255),0,0]
    draw_line(0,y*5,XRES,random.randint(0,YRES),screen,color)
    #draw_line2(y*5,0,XRES,YRES,screen,color)
#octave 2
for y in range(YRES/5):
    color = [0,0,random.randint(0,255)]'''
draw_line2(XRES/2-100,YRES/2,XRES/2,YRES/2+200,screen,color)
'''draw_line2(y*5,0,XRES,random.randint(0,YRES),screen,color)
    #draw_line2(0,y*5,XRES,YRES,screen,color)'''
#octave 7
#for y in range(YRES/5):
draw_line7(XRES/2-100,YRES/2,XRES/2-100,YRES/2-200,screen,color)
draw_line7(XRES/2-100,YRES/2,XRES/2,YRES/2-200,screen,color)
#octave 8
#for y in range(YRES/5):
draw_line8(XRES/2-100,YRES/2,XRES/2,YRES/2-50,screen,color)
display(screen)
#save_extension(screen, 'img.png')
