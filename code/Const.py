# C
C_BLACK = (0, 0, 0)
C_GOLD = (255, 215, 0)
C_GREEN = (50, 200, 80)
C_RED = (220, 40, 40)
C_WHITE = (255, 255, 255)

# E
ENTITY_DAMAGE = {
    'Player': 20, # Dano se encostar no zumbi
    'Bullet': 20, # Dano do tiro no zumbi (1 hit = headshot)
    'Zombie': 25, # Dano causado pelo zumbi se encostar no cowboy (4 hits = game over)
}

ENTITY_HEALTH = {
    'Player': 100,
    'Bullet': 1,
    'Zombie': 20,
}

ENTITY_SPEED = {
    'Player': 5,
    'Bullet': 12,
    'Zombie': 3,
}

# F
FPS = 60 # Quadros por segundo

# G
GAME_DURATION = 60 # Tempo em segundos para vencer (60s)

# S
SPAWN_TIME = 1200 # Tempo entre cada zumbi em milissegundos (1.2s)
STREET_TOP_Y = 395 

# W
WIN_WIDTH = 900
WIN_HEIGHT = 500