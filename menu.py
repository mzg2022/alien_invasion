import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)

        # Цвета кнопок
        self.inactive_color = (200, 200, 200)
        self.active_color = (255, 255, 255)

        # Кнопки
        self.play_button = self.font.render("Play", True, self.inactive_color)
        self.easy_button = self.font.render("Easy", True, self.inactive_color)
        self.hard_button = self.font.render("Hard", True, self.inactive_color)
        self.size_button = self.font.render("Screen Size: 800x600", True, self.inactive_color)
        self.sound_button = self.font.render("Sound: On", True, self.inactive_color)

        # Позиции кнопок
        self.play_rect = self.play_button.get_rect(center=(self.screen_rect.centerx, self.screen_rect.centery - 100))
        self.easy_rect = self.easy_button.get_rect(center=(self.screen_rect.centerx, self.screen_rect.centery - 50))
        self.hard_rect = self.hard_button.get_rect(center=(self.screen_rect.centerx, self.screen_rect.centery))
        self.size_rect = self.size_button.get_rect(center=(self.screen_rect.centerx, self.screen_rect.centery + 50))
        self.sound_rect = self.sound_button.get_rect(center=(self.screen_rect.centerx, self.screen_rect.centery + 100))

        # Настройки по умолчанию
        self.selected_difficulty = 1
        self.screen_size = (800, 600)
        self.sound_on = True

    def draw_menu(self):
        self.screen.fill((0, 0, 0))

        # Подсветка кнопок при наведении
        mouse_pos = pygame.mouse.get_pos()
        self.play_button = self.font.render("Play", True, self.active_color if self.play_rect.collidepoint(mouse_pos) else self.inactive_color)
        self.easy_button = self.font.render("Easy", True, self.active_color if self.easy_rect.collidepoint(mouse_pos) else self.inactive_color)
        self.hard_button = self.font.render("Hard", True, self.active_color if self.hard_rect.collidepoint(mouse_pos) else self.inactive_color)
        self.size_button = self.font.render(f"Screen Size: {self.screen_size[0]}x{self.screen_size[1]}", True, self.active_color if self.size_rect.collidepoint(mouse_pos) else self.inactive_color)
        self.sound_button = self.font.render("Sound: On" if self.sound_on else "Sound: Off", True, self.active_color if self.sound_rect.collidepoint(mouse_pos) else self.inactive_color)

        # Отрисовка кнопок
        self.screen.blit(self.play_button, self.play_rect)
        self.screen.blit(self.easy_button, self.easy_rect)
        self.screen.blit(self.hard_button, self.hard_rect)
        self.screen.blit(self.size_button, self.size_rect)
        self.screen.blit(self.sound_button, self.sound_rect)
        pygame.display.flip()

    def check_click(self, mouse_pos):
        if self.play_rect.collidepoint(mouse_pos):
            return "play"
        elif self.easy_rect.collidepoint(mouse_pos):
            self.selected_difficulty = 1
        elif self.hard_rect.collidepoint(mouse_pos):
            self.selected_difficulty = 2
        elif self.size_rect.collidepoint(mouse_pos):
            self.screen_size = (1024, 768) if self.screen_size == (800, 600) else (800, 600)
        elif self.sound_rect.collidepoint(mouse_pos):
            self.sound_on = not self.sound_on
        return None

