class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)  # Черный фон
        self.ship_limit = 3  # Количество жизней
        self.bullet_speed = 3
        self.alien_speed = 1.0  # Исправлено: должно быть 1.0, а не кортеж (0, 1)
        self.fleet_drop_speed = 10

