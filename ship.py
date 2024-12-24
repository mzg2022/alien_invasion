import pygame

class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center_ship()

    def update(self, mouse_pos):
        self.rect.centerx = mouse_pos[0]
        # Keep ship within screen bounds
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        elif self.rect.left < 0:
            self.rect.left = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

