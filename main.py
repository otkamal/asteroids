import pygame
import constants
import player

def main():

    print("Starting asteroids!")
    pygame.init()

    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    p = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(constants.COLOR_BLACK)
        p.draw(screen)
        pygame.display.flip()
        dt = clock.tick(constants.MAX_FPS)
        # convert dt from milliseconds to seconds
        dt /= 1000


if __name__ == "__main__":
    main()