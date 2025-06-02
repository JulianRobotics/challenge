# Your code goes here

import pyray as pr
from random import randint

from tail_segment import TailSegment
from player import Player
from apple import Apple
from constants import *


pr.init_window(1200, 750, "Snake Game")
pr.set_target_fps(15)

class Game:
    tail: list[TailSegment]
    player: Player
    #apple: list[Apple]

    def __init__(self) -> None:
        self.tail = [TailSegment(15,6),TailSegment(16,6)]
        self.apple = [Apple(4,6),Apple(5,6)]
        self.make_apples()
        self.player = Player(14,6)
        self.score = 0
        self.dead = False
        self.hey = False

    def update(self) -> None:
        # all logic should go here
        self.draw()
        self.check_collisions()
        self.update_tail()
        self.player.move()

    def draw(self) -> None:
        # all drawing should go here
        for apple in self.apple:
            pr.draw_rectangle_v((apple.x*TILE_SIZE,apple.y*TILE_SIZE),(TILE_SIZE,TILE_SIZE),pr.RED)

        pr.draw_rectangle_v((self.player.position[0]*TILE_SIZE,self.player.position[1]*TILE_SIZE), (TILE_SIZE,TILE_SIZE), pr.BLACK)
        self.player_rect = pr.Rectangle(self.player.position[0]*TILE_SIZE,self.player.position[1]*TILE_SIZE,TILE_SIZE,TILE_SIZE)
        
        for tailPiece in self.tail:
            pr.draw_rectangle_v((tailPiece.x*TILE_SIZE,tailPiece.y*TILE_SIZE),(TILE_SIZE,TILE_SIZE),pr.DARKGRAY)
       
        pr.draw_text(f"SCORE: {str(self.score)}",20,20,20,pr.DARKBROWN)
    
    def update_tail(self):
        shift = TailSegment(self.tail[0].x + self.player.direction[0],self.tail[0].y + self.player.direction[1])
        self.tail.insert(0,shift)
        if self.hey:
            print("hji")
            self.hey = False
        else:
            self.tail.pop()

    def check_collisions(self):
        yes = False
        for apple in self.apple:
            apple_rect = pr.Rectangle(apple.x*TILE_SIZE,apple.y*TILE_SIZE,TILE_SIZE,TILE_SIZE)
            if pr.check_collision_recs(self.player_rect,apple_rect):
                self.score += 1
                yes = True
                self.hey = True
                self.apple.remove(apple)

        for tailSegment in self.tail[1:]:
            rect = pr.Rectangle(tailSegment.x*TILE_SIZE,tailSegment.y*TILE_SIZE,TILE_SIZE,TILE_SIZE)
            if pr.check_collision_recs(self.player_rect,rect):
                self.dead = True
        if self.player.position[0]*TILE_SIZE >= 1200 or self.player.position[0] < 0 or self.player.position[1]*TILE_SIZE >= 750 or self.player.position[1] < 0:
            self.dead = True

    def game_over(self):
        self.tail = [TailSegment(15,6),TailSegment(16,6)]
        self.player = Player(14,6)
        self.player.direction = LEFT
        pr.draw_text(f"Game Over\nYour score was: {self.score}\nPress M",200,200,30,pr.BLACK)
        if pr.is_key_down(pr.KeyboardKey.KEY_M):
            self.dead = False
            self.score = 0
            self.apple.clear()
            self.make_apples()
    
    def make_apples(self):
        for i in range(10):
            self.apple.insert(0,Apple(randint(0,40),randint(0,25)))

game = Game()

while not pr.window_should_close():
    if not game.dead:
        game.update()
    else:
        game.game_over()

    pr.begin_drawing()
    pr.clear_background(pr.WHITE)
    pr.end_drawing()
pr.close_window()
