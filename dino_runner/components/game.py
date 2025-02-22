import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_ups.power_upManage import PowerUpManage
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, DINO_START, HUMMER_TYPE, ICON, RESET, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS
from dino_runner.components.obstacles.obstaclesManage import ObstacleManager
from dino_runner.utils.text import draw_message

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.death_count = 0
        self.power_up_manager = PowerUpManage()

    def run(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def play(self):
        #game loop: events -update - draw
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.playing = True
        self.obstacle_manager.reset()
        self.score.reset()
        self.power_up_manager.reset()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed, self.score.score, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player.draw_power_up(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def on_death(self):
        print("BOOM")
        is_invincible = self.player.type == SHIELD_TYPE
        is_destroyer = self.player.type == HUMMER_TYPE

        if is_destroyer:
            self.score.reset()

        if not is_invincible and not is_destroyer:
            pygame.time.delay(500)
            self.playing = False
            self.death_count += 1

    def show_menu(self):
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        #Cambiar fondo pantalla
        self.screen.fill((200, 255, 80))
        #Agregar un texto de inicio en la pantalla
        if self.death_count == 0:
            draw_message("Press any key to start", self.screen)
            self.screen.blit(DINO_START, (center_x - 49, center_y - 121))
        else:
            draw_message("Press any key to restart", self.screen)
            draw_message(
                f"Your Score: {self.score.score}",
                self.screen,
                pos_y_center = center_y + 50
            )
            draw_message(
                f"Death count: {self.death_count}",
                self.screen,
                pos_y_center = center_y + 100
            )
            self.screen.blit(RESET, (center_x - 38, center_y -121))
        
        pygame.display.update()
        self.handle_menu_events()

        """if self.death_count == 0:
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render("Press any key to star.", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (center_x, center_y)
            self.screen.blit(text, text_rect)
            #Agregar una imagen en la pantalla
            self.screen.blit(DINO_START, (center_x - 49, center_y -121))
            #Refrescar pantalla
            pygame.display.update()
            #manejar eventos
            self.handle_menu_events()
        else:
            pass"""

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()


    
