import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

from colors import *
from pygame_config import *
import classes_and_objects.shapes as shapes
import classes_and_objects.boxes as boxes

def init_game():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window, shapes, amonguses, texts):
    window.fill(MIDNIGHT_BLUE) # 15

    for shape in shapes:
        shape.draw()

    for amongus in amonguses:
        for part in amongus:
            part.draw()

    for text in texts:
        text.draw_textbox()


    pygame.display.update()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False
    
    return True

def main(): # MAIN FUNCTION
    window = init_game()
    clock = pygame.time.Clock()
    # ADD ALL OBJECTS/CLASSES BELOW HERE

    def draw_amongus(window, color, x, y, scale=1, flip= False):

        if flip:
            amogus_body = shapes.Ellipse(window,color, x * scale, y * scale,300 *scale,400 * scale)
            amogus_legs1 = shapes.Rectangle(window, color, (x+ 50)* scale, (y+ 300)* scale,50* scale,150* scale)
            amogus_legs2 = shapes.Rectangle(window, color, (x+ 200)* scale, (y + 300)* scale,50* scale,150* scale)
            amogus_backpack = shapes.Rectangle(window, color, (x + 275)* scale, (y + 50)* scale,75* scale,300* scale)
            glass = shapes.Ellipse(window, CC_BLUE, (x-50)* scale, (y+50)* scale ,300* scale,50* scale)
        else:
            amogus_body = shapes.Ellipse(window,color, x* scale , y* scale,300* scale,400* scale)
            amogus_legs1 = shapes.Rectangle(window, color, (x+ 50)* scale, (y+ 300)* scale,50* scale,150* scale)
            amogus_legs2 = shapes.Rectangle(window, color, (x+ 200)* scale, (y + 300)* scale,50* scale,150* scale)
            amogus_backpack = shapes.Rectangle(window, color, (x - 50)* scale, (y + 50)* scale,75* scale,300* scale)
            glass = shapes.Ellipse(window, CC_BLUE, (x+50)* scale, (y+50)* scale ,300* scale,50* scale)

        amongus = [amogus_body,amogus_backpack,amogus_legs1,amogus_legs2,glass]

        return amongus
    
    def draw_star(window, x, y, color = WHITE):
        star = shapes.Polygon(window, color, [[x,y],[x+15,y+30],[x+45,y+45],[x+15,y+60],[x,y+90],[x-15,y+60],[x-45,y+45],[x-15,y+30]])

        return star

    amongus_text = boxes.Text_box(window,10,10,100,50,"Among Us", draw_rect=False, centered=False)
    thayer_amogus = draw_amongus(window,THAYER_GREEN,75,200,.75)
    classic_amogus = draw_amongus(window,RED, 400, 300, flip=True)

    star1 = draw_star(window, 350,250)
    star2 = draw_star(window, 700, 40)
    star3 = draw_star(window, 350, 550)

    stars = [star1, star2, star3]
    amongus = [thayer_amogus, classic_amogus]
    texts = [amongus_text]
    
    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        #Among us 


        

        run = handle_events()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT: # QUIT
        #         run = False
        #         break
        

        
        draw(window,stars, amongus, texts) # UPDATES SCREEN

    pygame.quit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

