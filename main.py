import pygame
import pygame.mixer

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from sounds import *

def main():
    #initialize pygame
    pygame.mixer.pre_init(22050, 16, 2, 2048*4)
    pygame.init()
    pygame.mixer.init()

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

    #play game music
    pygame.mixer.music.load("./sounds/cop-cuties.mp3")
    pygame.mixer.music.play()

    
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
        #updates display
        pygame.display.flip()
        #updates clock
        dt = clock.tick(60) / 1000
        fps = clock.get_fps()            #set the music time
        volume = pygame.mixer.music.get_volume()
        #music_time = pygame.mixer.music.get_pos()
        #if music_time > 4000:
            #pygame.mixer.music.stop()
            #pygame.mixer.music.play()


        
        #PRINTS
        print(f"FPS: {fps}")
        print(f"VOLUME: {volume}")
               
if __name__ == "__main__":
    main()
