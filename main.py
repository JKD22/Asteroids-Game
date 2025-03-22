import pygame
from constants import *
from player import Player

def main():
    #initialize pygame
    pygame.init()
    #set up the clock
    clock = pygame.time.Clock()
    #set game time to 0
    dt = 0
    #set up the screen  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #set the player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
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
        player.draw(screen)
        #updates display
        pygame.display.flip()
        #updates clock
        dt = clock.tick(60) / 1000
        fps = clock.get_fps()
        print(f"FPS: {fps}")
if __name__ == "__main__":
    main()
