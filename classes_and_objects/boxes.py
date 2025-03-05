# These are Classes that help with on screen graphics

#font = pygame.font.Font("C:\\Windows/Users/YangTh599/Documents/GitHub/pygame-template/fonts/MoreSugar-Regular.ttf") # MORESUGAR Font

"""

import pygame
from os.path import join
pygame.init()

class Text_box():

    def __init__(self, window, x, y, width, height, text, font="Comic Sans MS",text_size = 24, draw_rect = True, centered = True):
        self.rect = pygame.Rect(x,y,width,height)
        self.window = window

        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.draw_rect = draw_rect
        self.centered = centered

        self.text = text
        self.text_size = text_size
        self.font = font
        self.text_font = pygame.font.SysFont(font, text_size)

    def change_font(self, new_font):
        if (new_font[-4:] == ".ttf" or new_font[-4:] == ".otf"):
            self.text_font = pygame.font.Font(new_font, self.text_size)
        else:
            self.text_font = pygame.font.SysFont(new_font, self.text_size)

    def italicize(self, italicize = True):
        if not (self.font[-4:] == ".ttf" or self.font[-4:] == ".otf"):
            self.text_font = pygame.font.SysFont(self.font, self.text_size, italic=italicize)
    
    def bolden(self, boldize = True):
        if not (self.font[-4:] == ".ttf" or self.font[-4:] == ".otf"):
            self.text_font = pygame.font.SysFont(self.font, self.text_size, bold=boldize)

    def draw_textbox(self):
        text = self.text_font.render(self.text, True, WHITE)
        if self.draw_rect:
            pygame.draw.rect(self.window, (50, 200, 50), self.rect)
        if self.centered:
            text_rect = text.get_rect(center=self.rect.center)
            self.window.blit(text, text_rect)
        else:
            self.window.blit(text, [self.x,self.y])

class Image_box():

    def __init__(self, x, y, width, height, image):
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.image.load(join('assets','images',image))

    def draw_image(self):
        window.blit(self.image, (self.x, self.y))

"""