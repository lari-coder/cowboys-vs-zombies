from abc import ABC, abstractmethod
import pygame
from code.Const import ENTITY_DAMAGE, ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, posistion: tuple, image_path: str, size: tuple):
        self.name = name
        raw_surf = pygame.image.load(image_path).convert_alpha()
        self.surf = pygame.transform.scale(raw_surf, size)
        self.rect = self.surf.get_rect(left=posistion[0], top=posistion[1])

        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    @abstractmethod
    def move(self):
        pass