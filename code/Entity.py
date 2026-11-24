from abc import ABC


class Entity(ABC):
    def __init__(self, name: str, posistion: tuple, image_path: str, size: tuple):
        self.name = name
        raw_surf = pygame.image.load(image_path).convert_alpha()
        