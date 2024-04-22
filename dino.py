import pygame

class Dino(pygame.sprite.Sprite):
    def __init__(self, screen, settings):
        super().__init__()

        self.screen = screen
        self.settings = settings

        self.dino_walk_1 = pygame.image.load('assets/Dino/DinoRun1.png').convert_alpha()
        self.dino_walk_2 = pygame.image.load('assets/Dino/DinoRun2.png').convert_alpha()

        self.dino_jump = pygame.image.load('assets/Dino/DinoJump.png').convert_alpha()

        self.dino_duck_1 = pygame.image.load('assets/Dino/DinoDuck1.png').convert_alpha()
        self.dino_duck_2 = pygame.image.load('assets/Dino/DinoDuck2.png').convert_alpha()

        self.dino_duck_frames = [self.dino_duck_1, self.dino_duck_2]
        self.dino_duck_frames_index = 0

        self.dino_frames = [self.dino_walk_1, self.dino_walk_2]
        self.dino_frames_index = 0

        self.dino_surf = self.dino_frames[self.dino_frames_index]
        self.rect = self.dino_surf.get_rect()
        self.rect.bottomleft = (100, 480)

        self.is_jumping = False
        self.jump_time_start = 0
        self.gravity = 0

        self.is_ducking = False

    def animation(self):
            if(self.is_jumping):
                # Animation for the dino jumping
                self.dino_surf = self.dino_jump
            elif(self.is_ducking):
                # Animation for dino ducking
                self.rect.bottomleft = (100, 520)
                self.dino_duck_frames_index += 0.1
                if self.dino_duck_frames_index >= len(self.dino_duck_frames):
                    self.dino_duck_frames_index = 0
                self.dino_surf = self.dino_duck_frames[int(self.dino_duck_frames_index)]
            else:
                # Animation for the dino runnings
                self.dino_frames_index += 0.1
                if self.dino_frames_index >= len(self.dino_frames):
                    self.dino_frames_index = 0
                self.dino_surf = self.dino_frames[int(self.dino_frames_index)]

    def dino_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not self.is_jumping:
                self.gravity -= 12
                self.is_jumping = True
                self.jump_time_start = self.settings.current_time
            if event.key == pygame.K_DOWN and self.is_jumping:
                self.gravity = 20
            if event.key == pygame.K_DOWN and not self.is_jumping:
                self.is_ducking = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and self.is_jumping:
                self.jump_time_start = 0
            if event.key == pygame.K_DOWN and self.is_ducking:
                self.rect.bottomleft = (100, 480)
                self.is_ducking = False

    def apply_gravity(self):
        if self.is_jumping:
            time_difference = self.settings.current_time - self.jump_time_start
            if (time_difference) >= 1000 or self.jump_time_start == 0 or self.rect.centery <= 300:
                self.jump_time_start = 0
                self.gravity += 0.7
            else:
                self.gravity += (time_difference / 1000)
            
            self.rect.centery += self.gravity
            if self.rect.centery >= 433:
                self.is_jumping = False
                self.rect.centery = 433
        else:
            self.gravity = 0

    def update(self):
        self.animation()
        self.apply_gravity()
        self.screen.blit(self.dino_surf, self.rect)
