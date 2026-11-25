import pygame
from code.Bullet import Bullet
from code.Const import ENTITY_SPEED, STREET_TOP_Y, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity

class Player(Entity):
    def __init__(self, posistion: tuple, scale: float = 1.5):
        raw_idle = pygame.image.load('asset/cowgirl.png').convert_alpha()
        idle_size = (int(raw_idle.get_width() * scale), int(raw_idle.get_height() * scale))

        super().__init__('Player', posistion, 'asset/cowgirl.png', idle_size)
        self.surf_idle = self.surf

        raw_shoot = pygame.image.load('asset/cowgirl_shoot.png').convert_alpha()
        shoot_size = (int(raw_shoot.get_width() * scale), int(raw_shoot.get_height() * scale))
        self.surf_shoot = pygame.transform.scale(raw_shoot, shoot_size)

        self.shoot_anim_timer = 0
        self.shot_cooldown = 0

    def move(self):
        pressed_key = pygame.key.get_pressed()
        speed = ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_w] and self.rect.bottom > STREET_TOP_Y:
            self.rect.y -= speed
        if pressed_key[pygame.K_s] and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += speed

        if pressed_key[pygame.K_a] and self.rect.left > 10:
            self.rect.x -= speed
        if pressed_key[pygame.K_d] and self.rect.right < WIN_WIDTH - 80:
            self.rect.x += speed

        if self.shoot_anim_timer > 0:
            self.shoot_anim_timer -= 1
            if self.shoot_anim_timer == 0:
                self.surf = self.surf_idle

        if self.shot_cooldown > 0:
            self.shot_cooldown -= 1

    def shoot(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_SPACE] and self.shot_cooldown == 0:
            self.surf = self.surf_shoot
            self.shoot_anim_timer = 12
            self.shot_cooldown = 18

            bullet_pos = (self.rect.right + 22, self.rect.top + int(self.rect.height * 0.21))
            return Bullet(bullet_pos)
        return None
    