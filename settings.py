import math

# game settings
#RES = WIDTH, HEIGHT = 1600, 900
RES = WIDTH, HEIGHT = 1920, 1080
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0

PLAYER_POS = 1.5, 5  # mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60
PLAYER_MAX_HEALTH = 100

MOUSE_SENSITIVITY = 0.0001
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

# niveles y temporizador
LEVEL_DURATION = 180000  # 3 minutos en ms
LEVELS = [
    {'name': 'Nivel 1', 'player_pos': (1.5, 5.0), 'spawn_interval': (6000, 8000), 'max_enemies': 8, 'weights': [90, 10, 0], 'speed_mult': 0.85, 'damage_mult': 0.8, 'burst': 1},
    {'name': 'Nivel 2', 'player_pos': (1.5, 5.0), 'spawn_interval': (3000, 4500), 'max_enemies': 12, 'weights': [70, 25, 5], 'speed_mult': 1.0, 'damage_mult': 1.0, 'burst': 2},
    {'name': 'Nivel 3', 'player_pos': (1.5, 5.0), 'spawn_interval': (1500, 2500), 'max_enemies': 16, 'weights': [50, 35, 15], 'speed_mult': 1.15, 'damage_mult': 1.25, 'burst': 3},
]

# armas: placeholders reutilizando sprite de escopeta con escala/tinte propio
WEAPON_TYPES = [
    {'id': 'pistol', 'name': 'Pistola', 'damage': 25, 'cooldown': 250, 'scale': 0.3, 'tint': (180, 180, 255), 'animation_time': 90},
    {'id': 'shotgun', 'name': 'Escopeta', 'damage': 50, 'cooldown': 700, 'scale': 0.4, 'tint': None, 'animation_time': 90},
    {'id': 'machinegun', 'name': 'Ametralladora', 'damage': 15, 'cooldown': 120, 'scale': 0.35, 'tint': (255, 180, 120), 'animation_time': 90},
    {'id': 'rocket', 'name': 'Lanzacohetes', 'damage': 120, 'cooldown': 1200, 'scale': 0.5, 'tint': (255, 120, 120), 'animation_time': 90},
]

# sistema de armas únicas por nivel: aparecen una sola vez, en tiempos distintos
WEAPON_SPAWN_TIMES = (20000, 60000, 100000, 140000)  # ms desde inicio de nivel
WEAPON_PICKUP_LIFETIME = 60000  # expira a los 60 s si no se recoge
WEAPON_RESPAWN_DELAY = 5000  # tras expirar, reaparece en otra posición a los 5 s
WEAPON_STARTING = 'shotgun'  # arma inicial por nivel (no se genera en el mapa)