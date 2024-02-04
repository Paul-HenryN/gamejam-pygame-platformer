import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load(
            "Assets/pixel-platformer/Tiles/Characters/tile_0000.png"
        )
        self.img_moves = [False, False, False, False]
        pygame.display.set_caption("Dreambound")

    def run(self):
        while True:
            self.screen.blit(self.img, self.img_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.img_moves[0] = True
                    if event.key == pygame.K_DOWN:
                        self.img_moves[1] += 1

            pygame.display.update()
            self.clock.tick(60)


Game().run()
