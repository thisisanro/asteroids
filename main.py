# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        #exit program by mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fill the screen with black
        screen.fill("black")
        
        #update display
        pygame.display.flip()
        
        # set fps limit
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()