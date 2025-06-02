import pyray as pr

class TailSegment():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.position = (self.x,self.y)
    
    def position(self):
        return self.position