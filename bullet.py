import pygame

class Bullet:
    def __init__(self, screen, ship):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.color = (255, 255, 255)
        self.speed = 3
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

    def update(self):
        self.rect.y -= self.speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

