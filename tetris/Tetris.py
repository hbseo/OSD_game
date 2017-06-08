import pygame, sys
from pygame.locals import *
from Board import *

#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

class Tetris:
    DROP_EVENT = USEREVENT + 1

    def __init__(self):
        self.screen = pygame.display.set_mode((250, 450))
        self.clock = pygame.time.Clock()
        self.board = Board(self.screen)

    def handle_key(self, event_key):
        if event_key == K_DOWN:
            self.board.drop_piece()
        elif event_key == K_LEFT:
            self.board.move_piece(dx=-1, dy=0)
        elif event_key == K_RIGHT:
            self.board.move_piece(dx=1, dy=0)
        elif event_key == K_UP:
            self.board.rotate_piece()
        elif event_key == K_SPACE:
            self.board.full_drop_piece()
        elif event_key == K_ESCAPE:
            self.pause()

    def pause(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False


    def run(self):
        pygame.init()
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Tetris')
        pygame.time.set_timer(Tetris.DROP_EVENT, 500)

        while True:
            if self.board.game_over():
                print("Game over")
                pygame.quit()
                sys.exit()
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.handle_key(event.key)
                elif event.type == Tetris.DROP_EVENT:
                    self.board.drop_piece()

            self.board.draw()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    Tetris().run()
