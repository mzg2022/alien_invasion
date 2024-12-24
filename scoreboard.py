import pygame.font

class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.score = 0
        self.high_score = 0
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        score_str = f"Score: {self.score}   High Score: {self.high_score}"
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right - 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)

    def update_score(self, points):
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score
        self.prep_score()
