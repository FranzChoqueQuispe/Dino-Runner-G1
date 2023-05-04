import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.score import Score 
from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS
from dino_runner.components.obstacles.obstaclesManage import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def play(self):
        #game loop: events -update - draw
        self.playing = True
        self.obstacle_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        #self.score.draw()
        #self.power_up
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
        #is_invincible = self.player.type == SHIELD_TYPE
        #if not is_invincible
        pygame.time.delay(500)
        self.playing = False
        self.death_count += 1

    def show_menu(self):
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        #Cambiar fondo pantalla
        self.screen.fill((255, 255, 255))
        #Agregar un texto de inicio en la pantalla
        if self.death_count == 0:
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render("Press any key to star.", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (center_x, center_y)
            self.screen.blit(text, text_rect)
            #Agregar una imagen en la pantalla
            #self.screen.blit(DINO_START, (center_x - 49, center_y -121))
        else:
            pass
        
        #Refrescar pantalla
        pygame.display.update()
        #manejar eventos
        self.handle_menu_events()

    def handle_menu_events(self):
        pass

    
