import pygame
import circleshape
import constants

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
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