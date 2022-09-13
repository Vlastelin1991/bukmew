class Settings():
    """Класс для сохранения настроек игры"""

    def __init__(self):
        """Инииализиует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 4

        # Параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_widht = 3
        self.bullet_higth = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 10
        self.ship_limit = 3
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

