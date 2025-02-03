import pygame
import circleshape
import constants
import shot

class Player(circleshape.CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.booster_reserves = 1
        self.weapon_cooldown = 0
        self.booster_cooldown = 0
        self.num_lives = constants.PLAYER_BASE_LIVES
        self.is_dmg_immune = False
        self.dmg_immunity_cooldown = 0
        self.current_acceleration = 0
        self.__shoot_sound = pygame.mixer.Sound(constants.FILEPATH_PLAYER_SHOT)
        self.__shoot_sound.set_volume(constants.DEFAULT_VOLUME_PLAYER_SHOT)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * (self.radius)
        b = self.position - forward * (self.radius) - right
        c = self.position - forward * (self.radius) + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            constants.COLOR_WHITE if not self.is_dmg_immune else constants.COLOR_GRAY,
            self.triangle(),
            constants.PLAYER_LINE_WIDTH
        )

    def move(self, dt, with_boost = False):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.current_acceleration += constants.PLAYER_ACC
        movement_vector = forward * self.current_acceleration
        if movement_vector.length() > constants.PLAYER_SPEED:
            movement_vector.scale_to_length(constants.PLAYER_SPEED)
        if with_boost:
            movement_vector *= constants.PLAYER_BOOSTER_FACTOR
            self.booster_reserves -= 0.025
            self.booster_reserves = max(0, self.booster_reserves)
        # if with_boost:
        #     self.position += forward * self.current_acceleration * dt * constants.PLAYER_BOOSTER_FACTOR
        #     self.booster_reserves -= 0.025
        #     self.booster_reserves = max(0, self.booster_reserves)
        #     return
        print(movement_vector.length())
        self.position += movement_vector * dt

    def continue_to_drift(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        movement_vector = forward * self.current_acceleration
        self.current_acceleration -= constants.PLAYER_DECEL
        self.current_acceleration = max(25, self.current_acceleration)
        self.position += movement_vector * dt

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def shoot(self, dt):
        self.weapon_cooldown -= dt
        if self.weapon_cooldown > 0:
            print("Weapon on cooldown")
            return
        self.__shoot_sound.play()
        self.weapon_cooldown = constants.PLAYER_WEAPON_COOLDOWN
        new_shot = shot.Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_BASE_SHOOT_SPEED 

    def update(self, dt):

        self.booster_cooldown -= dt
        self.booster_cooldown = max(0, self.booster_cooldown)

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

        if self.is_dmg_immune:
            self.dmg_immunity_cooldown -= dt
            self.dmg_immunity_cooldown = max(0, self.dmg_immunity_cooldown)
            if self.dmg_immunity_cooldown == 0:
                self.is_dmg_immune = False

        # if the player uses all of their booster => start a cooldown before recharging
        if self.booster_reserves == 0:
            self.booster_cooldown = constants.PLAYER_BOOSTER_COOLDOWN
            self.booster_reserves = 0.001
            print("player used all boost => starting cooldown")
            
        if self.booster_cooldown <= 0:
            self.booster_reserves += 0.001
            self.booster_reserves = min(self.booster_reserves, 1)

        self.continue_to_drift(dt)


    
