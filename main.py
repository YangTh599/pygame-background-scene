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

    amongus_text = boxes.Text_box(window,10,10,100,50,"Among Us", draw_rect=False, centered=False)
    scream = boxes.Text_box(window,10,50,100,50,"AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH", draw_rect=False, centered=False)
    amongus = []
    texts = [amongus_text]
    
    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        #Among us 


        # amongus = [draw_amongus(window,RED,50,200), draw_amongus(window, YELLOW, 300,500,True), draw_amongus(window, PURPLE_GUY, 400,150,True)]

        num = rnd(0,1)
        if num == 0:
            flipped = False
        else:
            flipped = True
        amongus.append(draw_amongus(window,rand_color(),rnd(10,600),rnd(10,600),rnd(1,6)/2, flipped))

        if len(amongus) >= 500:
            amongus.clear()

        if len(amongus) >= 100:
            
            if scream not in texts:
                texts.append(scream)

        else:
            if scream in texts:
                texts.remove(scream)

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

