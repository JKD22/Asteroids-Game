import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    #initialize pygame
    pygame.init()

    #CREATE the containers first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    #THEN set the containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #set up the clock
    clock = pygame.time.Clock()
    #set game time to 0
    dt = 0
    #set up the screen  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



    #set the game objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    #prints the game title
    print("Starting Asteroids!")
    #prints the screen width and height
    print(f"Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK) 
        #draws the player
        for entity in drawable:
            entity.draw(screen)
        #updates the player
        for entity in updatable:
            entity.update(dt)
        print(f"Number of asteroids: {len(asteroids)}")
        #checks for collisions
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()

        #updates display
        pygame.display.flip()
        #updates clock
        dt = clock.tick(60) / 1000
        fps = clock.get_fps()            #set the music time
        
        #PRINTS
        print(f"FPS: {fps}")
        print(f"DT: {dt}")
               
if __name__ == "__main__":
    main()
