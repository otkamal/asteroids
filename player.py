import pygame
import circleshape
import constants
import shot

class Player(circleshape.CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.weapon_cooldown = 0
        self.booster_reserves = 1
        self.booster_cooldown = 0
    
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

    def move(self, dt, with_boost = False):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        print(f"Boost Left = {self.booster_reserves}")
        if with_boost:
            self.position += forward * constants.PLAYER_SPEED * dt * constants.PLAYER_BOOSTER_FACTOR
            self.booster_reserves -= 0.025
            self.booster_reserves = max(0, self.booster_reserves)
            return
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

        self.booster_cooldown -= dt
        self.booster_cooldown = max(0, self.booster_cooldown)
        print(f"remaining cooldown: {self.booster_cooldown}")

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            if keys[pygame.K_LSHIFT] and self.booster_reserves > 0.01:
                self.move(dt, True)
            else:
                self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        # if the player uses all of their booster => start a cooldown before recharging
        if self.booster_reserves == 0:
            self.booster_cooldown = constants.PLAYER_BOOSTER_COOLDOWN
            self.booster_reserves = 0.001
            print("player used all boost => starting cooldown")
            
        if self.booster_cooldown <= 0:
            self.booster_reserves += 0.001
            self.booster_reserves = min(self.booster_reserves, 1)


    
