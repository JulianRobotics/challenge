import pyray as pr
from constants import *

class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.position = (self.x,self.y)
        self.direction = LEFT

    def move(self) -> None:
        if pr.is_key_down(pr.KeyboardKey.KEY_RIGHT):
            if(self.direction != LEFT):
                self.direction = RIGHT
        elif pr.is_key_down(pr.KeyboardKey.KEY_DOWN):
            if(self.direction != UP):
                self.direction = DOWN
        elif pr.is_key_down(pr.KeyboardKey.KEY_LEFT):
            if(self.direction != RIGHT):
                self.direction = LEFT
        elif pr.is_key_down(pr.KeyboardKey.KEY_UP):
            if(self.direction != DOWN):
                self.direction = UP
        self.position = ((self.position[0]+self.direction[0])%20,(self.position[1]+self.direction[1])%20)