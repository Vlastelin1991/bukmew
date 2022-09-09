import pygame


class Ship():
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его позизицию"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/rocket.svg')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # Каждый новый корабль отображается в нижнем крае экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты корабля
        self.x = float(self.rect.x)

        # Флаг перемещения корабля
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабл с учетом флага"""
        # Обновляет атрибут x обекта ship, не rect

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновлене атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

