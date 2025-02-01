import pygame
import constants
import player
import asteroid
import asteroidfield

def main():

    print("Starting asteroids!")
     
    pygame.init()

    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)

    p = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    a = asteroidfield.AsteroidField()
    
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Ending asteroids")
                return
        screen.fill(constants.COLOR_BLACK)
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(constants.MAX_FPS)
        # convert dt from milliseconds to seconds
        dt /= 1000


if __name__ == "__main__":
    main()