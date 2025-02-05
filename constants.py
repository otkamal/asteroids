import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GRAY = (100, 100, 100)

DEFAULT_VOLUME_PLAYER_SHOT = 0.2
DEFAULT_VOLUME_ASTEROID_EXPLOSION = 0.15
DEFAULT_VOLUME_BACKGROUND_TRACK = 0.2

FILEPATH_PLAYER_SHOT = "sounds/blaster_sound.wav"
FILEPATH_ASTEROID_EXPLOSION = "sounds/asteroid_exploding.wav"
FILEPATH_BACKGROUND_TRACK = "sounds/background_music.mp3"

MAX_FPS = 60

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_LINE_WIDTH = 2

PLAYER_RADIUS = 20
PLAYER_LINE_WIDTH = 0
PLAYER_TURN_SPEED = 300
PLAYER_MAX_SPEED = 120
# 10% increase each iteration
PLAYER_ACCELERATION = 1.1
# 20% decrease each iteration
PLAYER_DECELERATION = 0.9995
# PLAYER_SPEED = 100
# PLAYER_ACC = 3
# PLAYER_DECEL = 1
PLAYER_BASE_SHOOT_SPEED = 700
PLAYER_WEAPON_COOLDOWN = 0.25
PLAYER_BOOSTER_FACTOR = 2
PLAYER_MAX_BOOSTED_SPEED = PLAYER_MAX_SPEED * PLAYER_BOOSTER_FACTOR
PLAYER_BOOSTER_COOLDOWN = 3
PLAYER_BASE_LIVES = 3
PLAYER_DMG_IMMUNITY_DURATION_POST_HIT = 5

SHOT_RADIUS = 5
SHOT_LINE_WIDTH = 0

RESOURCE_BAR_PADDING = 10
RESOURCE_BAR_WIDTH = SCREEN_WIDTH / 8
RESOURCE_BAR_HEIGHT = 30
RESOURCE_BAR_LINE_WIDTH = 2
MIN_RESOURCE_VALUE = 0.001