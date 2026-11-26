import pygame
from code.Enemy import Enemy
from code.Player import Player
from code.Const import FPS, SPAWN_TIME, STREET_TOP_Y, WIN_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Cowboys vs Zombies")
        self.clock = pygame.time.Clock()

        # Carrega o background
        raw_bg = pygame.image.load("./asset/background.png").convert()
        self.bg_surf = pygame.transform.scale(raw_bg, (WIN_WIDTH, WIN_HEIGHT))

        # Instancia o Player e as listas de entidades
        self.player = Player((80, STREET_TOP_Y - 20))
        self.bullets = []
        self.enemies = []

        # Evento para spawnar zumbis periodicamente
        self.SPAWN_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWN_EVENT, SPAWN_TIME)

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.window.blit(self.bg_surf, (0, 0))

            # Eventos (Fechar a janela e timer de spawn dos zumbis)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == self.SPAWN_EVENT:
                    self.enemies.append(Enemy())

            # Atualiza e desenha o Player
            self.player.move()
            new_bullet = self.player.shoot()
            if new_bullet:
                self.bullets.append(new_bullet)
                
            self.window.blit(self.player.surf, self.player.rect)

            # Atualiza e desenha as balas
            for bullet in self.bullets[:]:
                bullet.move()
                self.window.blit(bullet.surf, bullet.rect)
                if bullet.rect.left > WIN_WIDTH:
                    self.bullets.remove(bullet)

            # Atualiza, desenha e checa colisão dos zumbis com as balas
            for enemy in self.enemies[:]:
                enemy.move()
                self.window.blit(enemy.surf, enemy.rect)

                # Verifica se alguma bala acertou o zumbi
                for bullet in self.bullets[:]:
                    if enemy.rect.colliderect(bullet.rect):
                        enemy.health -= bullet.damage
                        self.bullets.remove(bullet)
                        if enemy.health <= 0:
                            self.enemies.remove(enemy)
                        break

                # Remove o zumbi se ele sair totalmente pela esquerda
                if enemy in self.enemies and enemy.rect.right < 0:
                    self.enemies.remove(enemy)
            
            pygame.display.flip()


        