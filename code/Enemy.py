from code.Entity import Entity
import random
import pygame
from code.Const import ENTITY_SPEED, STREET_TOP_Y, WIN_HEIGHT, WIN_WIDTH


class Enemy(Entity):
    def __init__(self, scale: float = 1.5):
        raw_img = pygame.image.load('asset/zombie.png').convert_alpha()
        zombie_size = (int(raw_img.get_width() * scale), int(raw_img.get_height() * scale))

        super().__init__('Zombie', (0, 0), 'asset/zombie.png', zombie_size)

        self.rect.left = WIN_WIDTH + 10
        self.rect.bottom = random.randint(STREET_TOP_Y, WIN_HEIGHT)

    def move (self):
        self.rect.x -= ENTITY_SPEED[self.name]
