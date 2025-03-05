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
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window, shapes, texts):
    window.fill(MIDNIGHT_BLUE) # 15

    for amongus in shapes:
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

    def draw_amongus(window, color, x, y, flip= False):

        if flip:
            amogus_body = shapes.Ellipse(window,color, x , y,300,400)
            amogus_legs1 = shapes.Rectangle(window, color, x+ 50, y+ 300,50,150)
            amogus_legs2 = shapes.Rectangle(window, color, x+ 200, y + 300,50,150)
            amogus_backpack = shapes.Rectangle(window, color, x + 275, y + 50,75,300)
            glass = shapes.Ellipse(window, CC_BLUE, x-50, y+50 ,300,50)
        else:
            amogus_body = shapes.Ellipse(window,color, x , y,300,400)
            amogus_legs1 = shapes.Rectangle(window, color, x+ 50, y+ 300,50,150)
            amogus_legs2 = shapes.Rectangle(window, color, x+ 200, y + 300,50,150)
            amogus_backpack = shapes.Rectangle(window, color, x - 50, y + 50,75,300)
            glass = shapes.Ellipse(window, CC_BLUE, x+50, y+50 ,300,50)

        amongus = [amogus_body,amogus_backpack,amogus_legs1,amogus_legs2,glass]

        return amongus


    
    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        #Among us 

        amongus_text = boxes.Text_box(window,10,10,100,50,"Among Us", draw_rect=False, centered=False)

        amongus = [draw_amongus(window,RED,50,200), draw_amongus(window, YELLOW, 300,500,True), draw_amongus(window, PURPLE_GUY, 400,150,True)]
        texts = [amongus_text]


        run = handle_events()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT: # QUIT
        #         run = False
        #         break
        

        
        draw(window, amongus, texts) # UPDATES SCREEN

    pygame.quit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

