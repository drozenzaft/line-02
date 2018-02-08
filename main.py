from display import *
from draw import *

screen = new_screen()
color = [0, 0, 255]
for y in range(YRES/5):
    '''x = (int)(y*(500/255.0))%255
    color = [0,0,x]'''
    draw_line(0,y*5,XRES,YRES,screen,color)
    draw_line(y*5,0,XRES,YRES,screen,color)
display(screen)
#save_extension(screen, 'img.png')
