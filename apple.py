import pyray as pr
from random import randint
from constants import *
class Apple():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.position = (x,y)
        self.rect = pr.Rectangle(self.x*TILE_SIZE,self.y*TILE_SIZE,TILE_SIZE,TILE_SIZE)
    

    def generate_random_position(self):
        self.x = randint(0,19)
        self.y = randint(0,19)
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE