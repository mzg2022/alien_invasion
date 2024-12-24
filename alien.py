import pygame
import random


class Alien:
    def __init__(self, screen, row, column, section_height):
        self.screen = screen
        self.image = pygame.image.load('alien.png').convert_alpha()

        # Уменьшаем размер изображения примерно в 1.5 раза
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() // 2,
                                             self.image.get_height() // 2))

        self.rect = self.image.get_rect()
        self.screen_width = screen.get_width()
        self.direction = 1  # 1 - движение вправо, -1 - движение влево
        self.speed = random.uniform(0.5, 1.5)  # Случайная начальная скорость

        # Устанавливаем высоту секции, на которую будут опускаться пришельцы
        self.section_height = section_height

        # Инициализация позиции пришельца
        self.rect.x = column * (self.rect.width + 10)  # Ширина + отступ
        self.rect.y = row * self.section_height  # Высота секции

    def update(self, aliens):
        # Двигаемся по горизонтали с учетом базовой скорости
        self.rect.x += self.speed * self.direction

        # Проверка столкновения с краем экрана
        if self.rect.right >= self.screen_width or self.rect.left <= 0:
            # Меняем направление
            self.direction *= -1
            # Сдвигаем вниз на одну секцию
            for alien in aliens:
                alien.rect.y += self.section_height

            # Ограничиваем вертикальное перемещение
            if self.rect.y > self.screen.get_height() - self.rect.height:
                self.rect.y = self.screen.get_height() - self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)









