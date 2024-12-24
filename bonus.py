import pygame
import random

class Bonus:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('resources/bonus.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_width())
        self.rect.y = 0  # Начальная позиция сверху
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
