import pygame

from code.Const import C_BLACK, C_GOLD, C_RED, C_WHITE, FPS, GAME_DURATION, SPAWN_TIME, STREET_TOP_Y, WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class Level:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()

        raw_bg = pygame.image.load("asset/background.png").convert()
        self.bg_surf = pygame.transform.scale(raw_bg, (WIN_WIDTH, WIN_HEIGHT))

        self.player = Player((80, STREET_TOP_Y - 80))
        self.bullets = []
        self.enemies = []

        self.font_hud = pygame.font.SysFont("arial", 22, bold=True)

        self.SPAWN_EVENT = pygame.USEREVENT + 1
        self.TIMER_EVENT = pygame.USEREVENT + 2
        pygame.time.set_timer(self.SPAWN_EVENT, SPAWN_TIME)
        pygame.time.set_timer(self.TIMER_EVENT, 1000)

        self.time_left = GAME_DURATION

    def draw_hud(self):
        health_color = C_WHITE if self.player.health > 25 else C_RED
        health_text = f"Saúde: {self.player.health}"

        shadow_h = self.font_hud.render(health_text, True, C_BLACK)
        self.window.blit(shadow_h, (22, 17))
        surf_h = self.font_hud.render(health_text, True, health_color)
        self.window.blit(surf_h, (20,15))

        timer_text = f"Tempo: {self.time_left}s"
        shadow_t = self.font_hud.render(timer_text, True, C_BLACK)
        self.window.blit(shadow_t, (WIN_WIDTH - 138, 17))
        surf_t = self.font_hud.render(timer_text, True, C_GOLD)
        self.window.blit(surf_t, (WIN_WIDTH - 140, 15))

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.window.blit(self.bg_surf, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == self.SPAWN_EVENT:
                    self.enemies.append(Enemy())
                if event.type == self.TIMER_EVENT:
                    self.time_left -= 1

            self.player.move()
            new_bullet = self.player.shoot()
            if new_bullet:
                self.bullets.append(new_bullet)
            self.window.blit(self.player.surf, self.player.rect)

            for bullet in self.bullets[:]:
                bullet.move()
                self.window.blit(bullet.surf, bullet.rect)
                if bullet.rect.left > WIN_WIDTH:
                    self.bullets.remove(bullet)

            for enemy in self.enemies[:]:
                enemy.move()
                self.window.blit(enemy.surf, enemy.rect)

                hit_by_bullet = False
                for bullet in self.bullets[:]:
                    if enemy.rect.colliderect(bullet.rect):
                        enemy.health -= bullet.damage
                        self.bullets.remove(bullet)
                        if enemy.health <= 0:
                            self.enemies.remove(enemy)
                            hit_by_bullet = True
                        break
                if hit_by_bullet:
                    continue

                if enemy.rect.colliderect(self.player.rect):
                    self.player.health -= enemy.damage
                    self.enemies.remove(enemy)
                    continue

                if enemy.rect.right < 0:
                    self.enemies.remove(enemy)

            self.draw_hud()
            pygame.display.flip()

            # 6. Verifica Condições de Derrota e Vitória
            if self.player.health <= 0:
                return "GAME_OVER"
            if self.time_left <= 0:
                return "VICTORY"