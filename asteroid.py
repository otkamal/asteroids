import pygame
import circleshape
import constants
import random
import math

class Asteroid(circleshape.CircleShape):

    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__explosion_sound = pygame.mixer.Sound(constants.FILEPATH_ASTEROID_EXPLOSION)
        self.__explosion_sound.set_volume(constants.DEFAULT_VOLUME_ASTEROID_EXPLOSION)
        self.points = self.__generate_irregular_polygon(15)

    def draw(self, screen):
        #points = self.__generate_irregular_polygon(10)
        pygame.draw.polygon(
            screen,
            constants.COLOR_WHITE,
            self.points,
            constants.ASTEROID_LINE_WIDTH
        )
        # pygame.draw.circle(
        #     screen,
        #     constants.COLOR_WHITE,
        #     self.position,
        #     self.radius,
        #     constants.ASTEROID_LINE_WIDTH
        # )
    
    def __generate_irregular_polygon(self, num_vertices, irregularity = 0.15):
        points = []
        angle_step = 2 * math.pi / num_vertices
        for i in range(num_vertices):
            angle = i * angle_step
            perturbed_radius = self.radius * (1 + random.uniform(-irregularity, irregularity))
            x = self.position.x + perturbed_radius * math.cos(angle)
            y = self.position.y + perturbed_radius * math.sin(angle)
            points.append((x, y))
        return points

    def update(self, dt):
        for i in range(len(self.points)):
            self.points[i] += (self.velocity * dt)
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