import pygame
import rectangleshape
import constants

class ResourceBar(rectangleshape.RectangleShape):

    def __init__(self, x, y):
        super().__init__(x, y, constants.RESOURCE_BAR_WIDTH, constants.RESOURCE_BAR_HEIGHT)
        self.available_resource = 0

    def update_available_resource(self, available_resource):
        self.available_resource = available_resource

    def draw(self, screen):
        if self.available_resource <= constants.MIN_RESOURCE_VALUE:
            outline_color = constants.COLOR_RED,
        else:
            outline_color = constants.COLOR_WHITE

        # fill rectangle
        pygame.draw.rect(
            surface = screen,
            color = constants.COLOR_WHITE,
            rect = pygame.Rect(
                self.position.x,
                self.position.y,
                self.available_resource * self.width,
                self.height
            )
        )

        # border
        pygame.draw.rect(
            surface = screen,
            color = outline_color,
            rect = pygame.Rect(
                self.position.x,
                self.position.y,
                self.width,
                self.height
            ),
            width = constants.RESOURCE_BAR_LINE_WIDTH
        )