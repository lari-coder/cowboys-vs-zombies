import pygame 
from code.Const import C_GOLD, ENTITY_DAMAGE, ENTITY_HEALTH, ENTITY_SPEED
from code.Entity import Entity


class Bullet(Entity):
    def __init__(self, position: tuple):
        self.name = 'Bullet'
        self.surf = pygame.Surface((12, 5))
        self.surf.fill(C_GOLD)
        self.rect = self.surf.get_rect(center=position)

        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    def move(self):
        self.rect.x += ENTITY_SPEED[self.name]
        