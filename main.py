import pygame
import sys
from random import choice
from dino import Dino
from obstacles import Obstacles
from settings import Settings
from menu import Menu
from score import Score

def dino_collisons():
    if pygame.sprite.spritecollideany(dino.sprite, obstacles_group):
        dino.sprite.rect.bottomleft = (100, 480)
        score.score = 0
        obstacles_group.empty()
        return False
    else:
        return True

pygame.init()
settings = Settings()
screen = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption(settings.title)
pygame.display.set_icon(settings.icon)
clock = pygame.time.Clock()
menu = Menu(screen)
score = Score()


dino = pygame.sprite.GroupSingle()
dino.add(Dino(screen, settings))

obstacles_group = pygame.sprite.Group()

# Timer for obstacles spawning
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

floor_surf = pygame.image.load('assets/Other/Track.png')
floor_rect = floor_surf.get_rect()
floor_rect.center = (600, 450)

while True:
    settings.current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and not settings.game_active:
                settings.game_active = True
                menu.start = False
                score.game_begin_time = settings.current_time
        if settings.game_active:
            if event.type == obstacle_timer:
                obstacles = ['cactus', 'cactus', 'bird']
                obstacles_group.add(Obstacles(screen, choice(obstacles)))

            dino.sprite.dino_input(event)
            
    
    screen.fill((255,255,255))
    
    
    if settings.game_active:
        screen.blit(floor_surf, floor_rect)
        settings.game_active = dino_collisons()
        score.update_score(screen, settings)
        dino.update()
        obstacles_group.update()
        score.update_highscore(screen)
    elif not settings.game_active:
        if menu.start:
            menu.update()
        else:
            screen.blit(floor_surf, floor_rect)
            menu.update_replay()
        score.update_highscore(screen)

    pygame.display.update()
    clock.tick(60)