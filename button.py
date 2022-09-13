import pygame.font

class Button():
    def __init__(self, ai_game, msg):
        """Инизиализирует атрибуты кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # РаЗмеры  и свойства кнопок
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение обьекта rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect_center = self.screen_rect.center

        # Сообщение о кнопке создается только один  раз
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает его по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Отображение пустой кнопки и вывод изображения
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)