import pygame
import constants

def main():

    print("Starting asteroids!")
    pygame.init()

    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(constants.COLOR_BLACK)
        pygame.display.flip()

if __name__ == "__main__":
    main()