import pygame

class Settings():
    def __init__(self):
        # General settings
        self.current_time = pygame.time.get_ticks()
        self.title = "Chrome Dinosaur"
        self.icon = pygame.image.load("assets/DinoWallpaper.png")

        # Screen settings
        self.width = 1200
        self.height = 600


        # Game settings
        self.game_active = False
        