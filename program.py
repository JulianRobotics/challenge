# Your code goes here

import pyray as pr

pr.init_window(500, 500, "Snake Game")

class Game:
    tail: list[TailSegment]
    player: Player
    apple: Apple

    def __init__(self) -> None:
        self.tail = # TODO: create a tail
        self.player = # TODO: create a player object
        self.apple = # TODO: create apple object

    def update(self) -> None:
        # all logic should go here
        if pr.is_key_down(pr.KeyboardKey.KEY_LEFT): # this is how you get user input,
                                                    # for a complete list, visit raylib.com
            pass
        pass

    def draw(self) -> None:
        # all drawing should go here
        pr.draw_rectangle_v(self.player.position(), (10,10), pr.BLACK)
        pr.draw_rectangle_v(self.apple.position(), (10,10), pr.RED)
        for tailPiece in self.tail:
            pr.draw_rectangle_v(tailPiece.position(), (10,10), pr.DARKGRAY) # please have a public method [position] in TailSegment



game = Game()

while not pr.window_should_close():
    game.update()

    pr.begin_drawing()
    pr.clear_background(pr.WHITE)
    game.draw()
    pr.end_drawing()
pr.close_window()
