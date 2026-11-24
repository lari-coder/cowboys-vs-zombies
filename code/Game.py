import pygame
from code.Const import FPS, WIN_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Cowboys vs Zombies")
        self.clock = pygame.time.Clock()

        raw_bg = pygame.image.load("./asset/background.png").convert()
        self.bg_surf = pygame.transform.scale(raw_bg, (WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            self.clock.tick(FPS)

            self.window.blit(self.bg_surf, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


        