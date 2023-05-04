import pygame

from dino_runner.utils.text import draw_message

class Score:
    def __init__(self):
        self.score = 0

    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2
    
    def draw(self, screen):
        draw_message(
            f"Score: {self.score}",
            screen,
            font_size = 22,
            pos_x_center=1000,
            pos_y_center=50)

        font = pygame.font.Font('freesansbold.ttf', 22)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)

    def reset(self):
        self.score = 0