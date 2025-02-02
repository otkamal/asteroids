import pygame

class RectangleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.width = width
        self.height = height

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must overide
        pass