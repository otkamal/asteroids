import pygame
import circleshape
import constants


class Shot(circleshape.CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            constants.COLOR_WHITE,
            self.position,
            self.radius,
            constants.SHOT_LINE_WIDTH
        )