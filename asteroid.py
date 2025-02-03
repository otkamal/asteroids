import pygame
import circleshape
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__explosion_sound = pygame.mixer.Sound(constants.FILEPATH_ASTEROID_EXPLOSION)
        self.__explosion_sound.set_volume(constants.DEFAULT_VOLUME_ASTEROID_EXPLOSION)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            constants.COLOR_WHITE,
            self.position,
            self.radius,
            constants.ASTEROID_LINE_WIDTH
        )
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.__explosion_sound.play()
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        r_rotation = self.velocity.rotate(rand_angle)
        l_rotation = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_one.velocity = r_rotation * random.uniform(1.1, 1.5)
        new_asteroid_two.velocity = l_rotation * random.uniform(1.1, 1.5)