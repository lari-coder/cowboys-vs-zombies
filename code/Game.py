import pygame
from code.Enemy import Enemy
from code.Level import Level
from code.Menu import Menu
from code.Player import Player
from code.Const import C_BLACK, C_GOLD, C_GREEN, C_RED, C_WHITE, FPS, SPAWN_TIME, STREET_TOP_Y, WIN_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Cowboys vs Zombies")

        raw_bg = pygame.image.load("asset/background.png").convert()
        self.bg_surf = pygame.transform.scale(raw_bg, (WIN_WIDTH, WIN_HEIGHT))

        self.font_title = pygame.font.SysFont("georgia", 50, bold=True)
        self.font_text = pygame.font.SysFont("arial", 22, bold=True)

    def show_end_screen(self, title: str, subtitle: str, title_color: tuple):
        while True:
            self.window.blit(self.bg_surf, (0, 0))

            surf_title = self.font_title.render(title, True, title_color)
            rect_title = surf_title.get_rect(center=(WIN_WIDTH // 2, 195))
            self.window.blit(surf_title, rect_title)

            surf_sub = self.font_text.render(subtitle, True, C_WHITE)
            rect_sub = surf_sub.get_rect(center=(WIN_WIDTH // 2, 250))
            self.window.blit(surf_sub, rect_sub)

            surf_opt = self.font_text.render("ENTER: Voltar ao Menu   |   ESC: Sair", True, C_GOLD)
            rect_opt = surf_opt.get_rect(center=(WIN_WIDTH // 2, 310))
            self.window.blit(surf_opt, rect_opt)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()

            level = Level(self.window)
            result = level.run()

            if result == "VICTORY":
                self.show_end_screen(
                    "VITÓRIA!",
                    "Você sobreviveu à horda de zumbis por 60 segundos!",
                    C_GREEN
                )
            elif result == "GAME_OVER":
                self.show_end_screen(
                    "GAME OVER",
                    "Sua saúde zerou! Os zumbis venceram.",
                    C_RED
                )


        