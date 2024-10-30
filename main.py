# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        #exit program by mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fill the screen with black
        screen.fill("black")
        
        # render a player
        player.draw(screen)

        #update display
        pygame.display.flip()
        
        # set 60 fps limit
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()