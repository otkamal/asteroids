import pygame
import rectangleshape
import constants

class ResourceBar(rectangleshape.RectangleShape):

    def __init__(self, x, y):
        super().__init__(x, y, constants.RESOURCE_BAR_WIDTH, constants.RESOURCE_BAR_HEIGHT)
        self.available_resource = 1

    def draw(self, screen):
        pygame.draw.rect(
            surface = screen,
            color = constants.COLOR_WHITE,
            rect = pygame.Rect(
                self.position.x,
                self.position.y,
                self.width,
                self.height
            )
        )