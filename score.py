import pygame

class Score():
    def __init__(self):
        self.score = int(0)
        self.highscore = int(0)

        self.highscore_surf = pygame.font.Font(None, 50).render(f'High Score: {self.highscore}', False, (53,53,53))
        self.highscore_rect = self.highscore_surf.get_rect(center = (150, 50))

        self.score_surf = pygame.font.Font(None, 50).render(f'Score: {self.score}', False, (53,53,53))
        self.score_rect = self.score_surf.get_rect(center = (1050, 50))

        self.game_begin_time = 500

    def update_highscore(self, screen):
        if self.score >= self.highscore:
            self.highscore = self.score
            self.highscore_surf = pygame.font.Font(None, 50).render(f'High Score: {self.highscore}', False, (53,53,53))

        screen.blit(self.highscore_surf, self.highscore_rect)

    def update_score(self, screen, settings):
        self.score = int((settings.current_time - self.game_begin_time) / 333)
        self.score_surf = pygame.font.Font(None, 50).render(f'Score: {self.score}', False, (53,53,53))
        screen.blit(self.score_surf, self.score_rect)

    

    

    
