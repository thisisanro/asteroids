# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        #exit program by mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fill the screen with black
        screen.fill((0, 0, 0))
        
        #update display
        pygame.display.flip()

if __name__ == "__main__":
    main()