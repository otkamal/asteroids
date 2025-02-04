import pygame
import constants
import player
import asteroid
import asteroidfield
import shot
import resourcebar

def main():

    print("Starting asteroids!")
     
    pygame.init()
    pygame.font.init()
    background_track = pygame.mixer.Sound(constants.FILEPATH_BACKGROUND_TRACK)
    background_track.set_volume(constants.DEFAULT_VOLUME_BACKGROUND_TRACK)
    background_track.play(-1)

    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, updatable, drawable)
    resourcebar.ResourceBar.containers = (drawable)

    p = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    booster_resource = resourcebar.ResourceBar(
        0 + constants.RESOURCE_BAR_PADDING,
        constants.SCREEN_HEIGHT - constants.RESOURCE_BAR_HEIGHT - constants.RESOURCE_BAR_PADDING
    )
    health_resource = resourcebar.ResourceBar(
        0 + constants.RESOURCE_BAR_PADDING,
        constants.SCREEN_HEIGHT - constants.RESOURCE_BAR_HEIGHT * 2 - constants.RESOURCE_BAR_PADDING * 2
    )
    asteroidfield.AsteroidField()

    dt = 0
    score = 0
    while True:
        font = pygame.font.Font(None, 36)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Ending asteroids")
                exit(0)
        screen.fill(constants.COLOR_BLACK)
        updatable.update(dt)
        booster_resource.update_available_resource(p.booster_reserves)
        health_resource.update_available_resource(p.num_lives / constants.PLAYER_BASE_LIVES)
        for a in asteroids:
            if a.is_colliding(p) and not p.is_dmg_immune and p.num_lives > 0:
                p.num_lives -= 1
                print(f"extra life used, {p.num_lives} lives remaining")
                p.is_dmg_immune = True
                p.dmg_immunity_cooldown = constants.PLAYER_DMG_IMMUNITY_DURATION_POST_HIT
            elif a.is_colliding(p) and not p.is_dmg_immune and p.num_lives <= 0:
                print(f"You have died.")
                print(f"Final Score: {score}")
                exit(0)
        for a in asteroids:
            for s in shots:
                if a.is_colliding(s):
                    print("collision detected")
                    a.split()
                    s.kill()
                    score += 100
        for d in drawable:
            d.draw(screen)
        score_text = font.render(f"Score: {score}", True, constants.COLOR_WHITE)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        dt = clock.tick(constants.MAX_FPS)
        # convert dt from milliseconds to seconds
        dt /= 1000


if __name__ == "__main__":
    main()