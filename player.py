import pygame
import circleshape
import constants
import shot

class Player(circleshape.CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.weapon_cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            constants.COLOR_WHITE,
            self.triangle(),
            constants.PLAYER_LINE_WIDTH
        )

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def shoot(self, dt):
        self.weapon_cooldown -= dt
        if self.weapon_cooldown > 0:
            print("Weapon on cooldown")
            return
        self.weapon_cooldown = constants.PLAYER_WEAPON_COOLDOWN
        new_shot = shot.Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_BASE_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)