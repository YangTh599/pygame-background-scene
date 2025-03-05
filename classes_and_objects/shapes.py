import pygame

# SHAPE CLASSES

class Line():

    def __init__(self,window, color, start_coord, end_coord, width):
        self.window = window
        self.color = color
        self.start = start_coord
        self.end = end_coord
        self.width = width

    def draw(self):
        pygame.draw.line(self.window,self.color, self.start, self.end, self.width)

class Rectangle():

    def __init__(self, window, color, x, y ,width=1, length=1, line_width=0):
        self.rect = pygame.Rect(x,y,width,length)
        self.window = window
        self.color = color
        self.line_width = line_width

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect, self.line_width)

class Square(Rectangle):

    def __init__(self, window, color, x, y, side_length = 1, line_width = 0):
        super().__init__(window, color, x, y, side_length, side_length, line_width)

class Circ():
    
    def __init__(self, window, color, center_coords, radius, width=0):
        self.window = window
        self.color = color
        self.center = center_coords
        self.r = radius
        self.width = width

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.center, self.r, self.width)


class Polygon():

    def __init__(self,window, color, points, width=0):
        self.window = window
        self.color = color
        self.points = points
        self.width = width

    def draw(self):
        pygame.draw.polygon(self.window,self.color,self.points,self.width)