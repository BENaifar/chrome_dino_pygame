import pygame

class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.start = True

        # Menu Start
        self.dino_start_surf = pygame.image.load('assets/Dino/DinoStart.png').convert_alpha()
        self.dino_start_rect = self.dino_start_surf.get_rect(center = (600, 300))

        self.text_surf = pygame.font.Font(None, 50).render(f'Press enter or spacebar to start', False, (53, 53, 53))
        self.text_rect = self.text_surf.get_rect(center = (600, 500))

        # Menu Replay
        self.dino_surf = pygame.image.load('assets/Dino/DinoRun1.png')
        self.dino_rect = self.dino_surf.get_rect(bottomleft = (100, 480))
        
        self.reset_surf = pygame.image.load('assets/Other/Reset.png')
        self.reset_rect = self.reset_surf.get_rect(center = (600, 300))
    
    def update(self):
        self.screen.blit(self.dino_start_surf, self.dino_start_rect)
        self.screen.blit(self.text_surf, self.text_rect)

    def update_replay(self):
        self.screen.blit(self.dino_surf, self.dino_rect)
        self.screen.blit(self.reset_surf, self.reset_rect)
