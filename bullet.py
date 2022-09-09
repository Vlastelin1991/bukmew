import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядом выпущеным корабдлем"""

    def __init__(self, ai_game):
        """Создает обьект снаряда выпущенного кораблем"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Создание снаряда в позиции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_widht, self.settings.bullet_higth)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиция снаряда зранится в вещественном формате
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд с низу вверх по экрану"""
        # Обновление позиции снаряда в вещественном формате
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снарыда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
