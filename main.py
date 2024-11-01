# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    while True:
        #exit program by mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # move player left and right
        for obj in updatable:
            obj.update(dt)
        
        #fill the screen with black
        screen.fill("black")
        
        # render a player
        for obj in drawable:
            obj.draw(screen)

        #update display
        pygame.display.flip()
        
        # set 60 fps limit
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()