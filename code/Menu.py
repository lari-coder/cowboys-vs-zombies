import pygame
from code.Const import C_BLACK, C_GOLD, C_GREEN, C_WHITE, WIN_HEIGHT, WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        raw_bg = pygame.image.load("asset/background.png").convert()
        self.bg_surf = pygame.transform.scale(raw_bg, (WIN_WIDTH, WIN_HEIGHT))

        self.font_title = pygame.font.SysFont("georgia", 52, bold=True)
        self.font_text = pygame.font.SysFont("arial", 22, bold=True)

    def draw_text(self, text: str, font, color: tuple, center_pos: tuple):

        for offset_x, offset_y in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
            outline_surf = font.render(text, True, C_BLACK)
            outline_rect = outline_surf.get_rect(center=(center_pos[0] + offset_x, center_pos[1] + offset_y))
            self.window.blit(outline_surf, outline_rect)

        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=center_pos)
        self.window.blit(text_surf, text_rect)

    def run(self):
        while True:
            self.window.blit(self.bg_surf, (0, 0))

            self.draw_text("COWBOYS VS ZOMBIES", self.font_title, C_GOLD, (WIN_WIDTH // 2, 175))
            self.draw_text("COMANDOS:", self.font_text, C_GOLD, (WIN_WIDTH // 2, 235))
            self.draw_text("W, A, S, D - Movimentar pela rua", self.font_text, C_WHITE, (WIN_WIDTH // 2, 270))
            self.draw_text("ESPAÇO - Atirar", self.font_text, C_WHITE, (WIN_WIDTH // 2, 305))
            self.draw_text("Objetivo: Sobreviva a horda por 60 segundos", self.font_text, C_GREEN, (WIN_WIDTH // 2, 355))
            self.draw_text("Pressione ENTER para jogar", self.font_text, C_GOLD, (WIN_WIDTH // 2, 435))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "PLAY"
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
