import pygame
from code.Player import Player
from code.Const import FPS, STREET_TOP_Y, WIN_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Cowboys vs Zombies")
        self.clock = pygame.time.Clock()

        raw_bg = pygame.image.load("./asset/background.png").convert()
        self.bg_surf = pygame.transform.scale(raw_bg, (WIN_WIDTH, WIN_HEIGHT))

        self.player = Player((80, STREET_TOP_Y - 20))
        self.bullets = []

    def run(self):
        while True:
            self.clock.tick(FPS)

            self.window.blit(self.bg_surf, (0, 0))

            self.player.move()
            new_bullet = self.player.shoot()
            if new_bullet:
                self.bullets.append(new_bullet)

            for bullet in self.bullets[:]:
                bullet.move()
                self.window.blit(bullet.surf, bullet.rect)
                if bullet.rect.left > WIN_WIDTH:
                    self.bullets.remove(bullet)

            self.window.blit(self.player.surf, self.player.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


        