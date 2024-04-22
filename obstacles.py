import pygame
from random import randint

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, screen, type):
        super().__init__()

        self.screen = screen
        self.type = type

        if self.type == 'cactus':
            self.large_cactus_1 = pygame.image.load('assets/Cactus/LargeCactus1.png').convert_alpha()
            self.large_cactus_2 = pygame.image.load('assets/Cactus/LargeCactus2.png').convert_alpha()
            self.large_cactus_3 = pygame.image.load('assets/Cactus/LargeCactus3.png').convert_alpha()
            self.small_cactus_1 = pygame.image.load('assets/Cactus/SmallCactus1.png').convert_alpha()
            self.small_cactus_2 = pygame.image.load('assets/Cactus/SmallCactus2.png').convert_alpha()
            self.small_cactus_3 = pygame.image.load('assets/Cactus/SmallCactus3.png').convert_alpha()

            self.frames = [self.large_cactus_1, self.large_cactus_2, self.large_cactus_3, self.large_cactus_1, self.large_cactus_2, self.large_cactus_3]
            self.index = randint(0, 5)

            self.y_pos = 480
        else:
            self.bird_1 = pygame.image.load('assets/Bird/Bird1.png').convert_alpha()
            self.bird_2 = pygame.image.load('assets/Bird/Bird2.png').convert_alpha()

            self.frames = [self.bird_1, self.bird_2]
            self.index = 0

            self.y_pos = 410

        self.surf = self.frames[self.index]
        self.rect = self.surf.get_rect(bottomleft = (1300, self.y_pos))
        

    def animate(self):
        if self.type != 'cactus':
            self.index += 0.1
            if self.index >= len(self.frames):
                self.index = 0
            self.surf = self.frames[int(self.index)]

    def destroy(self):
        if(self.rect.x < -100):
            self.kill()

    def update(self):
        self.rect.x -= 6
        self.animate()
        self.destroy()
        self.screen.blit(self.surf, self.rect)



