import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from menu import Menu
from scoreboard import Scoreboard
import pickle

def save_game(data, filename="savefile.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def load_game(filename="savefile.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)

def create_aliens(screen, rows, columns, section_height):
    aliens = []
    for row in range(rows):
        for column in range(columns):
            alien = Alien(screen, row, column, section_height)
            aliens.append(alien)
    return aliens

def run_game():
    pygame.init()
    pygame.mixer.init()
    laser_sound = pygame.mixer.Sound("resources/laser.wav")
    explosion_sound = pygame.mixer.Sound("resources/explosion.wav")
    lose_life_sound = pygame.mixer.Sound("resources/lose_life.wav")
    game_over_sound = pygame.mixer.Sound("resources/game_over.wav")
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    menu = Menu(screen)
    ship = Ship(screen)
    scoreboard = Scoreboard(screen)
    bullets = []
    aliens = []
    game_active = False
    show_menu = True
    lives = settings.ship_limit
    level_up_visible = False
    level_up_start_time = 0

    while True:
        if show_menu:
            menu.draw_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    action = menu.check_click(event.pos)
                    if action == "play":
                        settings.alien_speed = menu.selected_difficulty
                        settings.screen_width, settings.screen_height = menu.screen_size
                        settings.sound_on = menu.sound_on
                        screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

                        ship = Ship(screen)
                        scoreboard = Scoreboard(screen)  # Обнуляем счётчик
                        bullets.clear()
                        aliens = create_aliens(screen, 1, 5, 10)  # Создаем пришельцев в сетке
                        game_active = True
                        show_menu = False
                        scoreboard.score = 0  # Обнуляем счёт
                        scoreboard.prep_score()
        elif game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        show_menu = True
                        game_active = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        bullets.append(Bullet(screen, ship))
                        laser_sound.play()

            ship.update(pygame.mouse.get_pos())

            for bullet in bullets[:]:
                bullet.update()
                if bullet.rect.bottom < 0:
                    bullets.remove(bullet)

            for bullet in bullets[:]:
                for alien in aliens[:]:
                    if bullet.rect.colliderect(alien.rect):
                        aliens.remove(alien)
                        explosion_sound.play()
                        bullets.remove(bullet)
                        scoreboard.update_score(50)
                        break

            if not aliens:
                if scoreboard.score >= 450:
                    settings.alien_speed += 0.5  # Плавное увеличение скорости
                aliens = create_aliens(screen, 1, 5, 10)  # Создаем новых пришельцев
                scoreboard.update_score(100)
                level_up_visible = True
                level_up_start_time = pygame.time.get_ticks()

            for alien in aliens[:]:
                alien.update(aliens)  # Передаем список пришельцев
                if alien.rect.colliderect(ship.rect):
                    # Столкновение с пришельцем
                    lives -= 1
                    if lives == 0:
                        game_over_sound.play()
                        game_active = False
                        show_menu = True
                        scoreboard.score = 0  # Обнуляем счёт при потере всех жизней
                        scoreboard.prep_score()  # Обновляем отображение счёта
                    ship.center_ship()
                    aliens = create_aliens(screen, 1, 5, 10)  # Пересоздаем пришельцев
                    break

            screen.fill(settings.bg_color)
            ship.blitme()
            for bullet in bullets:
                bullet.draw_bullet()
            for alien in aliens:
                alien.blitme()
            scoreboard.show_score()

            ship_image = pygame.image.load('ship.png').convert_alpha()
            ship_image = pygame.transform.scale(ship_image, (50, 50))
            for i in range(lives):
                ship_rect = ship_image.get_rect()
                ship_rect.x = 10 + i * (ship_rect.width + 10)
                ship_rect.y = 10
                screen.blit(ship_image, ship_rect)

            if level_up_visible and pygame.time.get_ticks() - level_up_start_time > 2000:
                level_up_visible = False

            if level_up_visible:
                font = pygame.font.SysFont(None, 48)
                level_text = font.render("Level Up!", True, (255, 255, 0))
                screen.blit(level_text, (settings.screen_width // 2 - level_text.get_width() // 2, 100))


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # S для сохранения
                    game_data = {"level": level, "score": scoreboard.score, "lives": lives}
                    save_game(game_data)
                elif event.key == pygame.K_l:  # L для загрузки
                    game_data = load_game()
                    level = game_data["level"]
                    scoreboard.score = game_data["score"]
                    lives = game_data["lives"]

            pygame.display.flip()

if __name__ == '__main__':
    run_game()








