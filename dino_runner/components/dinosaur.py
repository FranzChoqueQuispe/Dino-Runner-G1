import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING, DUCKING_HAMMER, DUCKING_SHIELD, HUMMER_TYPE, JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING, RUNNING_HAMMER, RUNNING_SHIELD, SHIELD_TYPE
from dino_runner.utils.text import draw_message
#DOS ESPACIOS ENTRE IMPORTS Y CLASES

JUMP_VELOCITY = 8.5
DINO_JUMPING = "jumping"
DINO_RUNNING = "running"
DINO_DUCKING = "ducking"

DUCKING_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HUMMER_TYPE: DUCKING_HAMMER}
JUMPING_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HUMMER_TYPE: JUMPING_HAMMER}
RUNNING_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HUMMER_TYPE: RUNNING_HAMMER}

class Dinosaur(Sprite): #PASCAL CASE, formato para las clases    
    POS_X = 80
    POS_Y = 310
    POS_Y_DUCK = 340

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.update_image(RUNNING_IMG[self.type][0])
        #self.image = RUNNING[0]
        #self.rect = self.image.get_rect()
        #self.rect.x = self.POS_X
        #self.rect.y = self.POS_Y

        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = JUMP_VELOCITY

    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()#user_input)
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()

        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING

        #if user_input(pygame.K_UP) and self.action != DINO_JUMPING: #error
        #    if user_input[pygame.K_UP]:
        #        self.action = DINO_JUMPING
        #    else:
        #        self.action = DINO_RUNNING
        
        if self.step >=10:
            self.step = 0


    def jump(self):
        pos_y = self.rect.y - self.jump_velocity * 4
        self.update_image(JUMPING_IMG[self.type], pos_y=pos_y)
        self.jump_velocity -= 0.8
        print(self.rect.y, self.jump_velocity, sep="::") 
        if self.jump_velocity < -JUMP_VELOCITY:
            self.rect.y = self.POS_Y
            self.action = DINO_RUNNING
            self.jump_velocity = JUMP_VELOCITY

    
    def run(self):

        self.update_image(RUNNING_IMG[self.type][self.step // 5])

        #self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.step += 1
        #self.update_image(RUNNING_IMG[self.type][self] if self.step < 5 else RUNNING[1]) #error
        #self.step += 1


        #if self.jump_velocity < -8.5:
        #    self.rect.y = 310
        #    self.action = "running"
        #    self.jump_velocity = 8.5


        #if user_input[pygame.K_UP] and not self.action == "jumping":
        #    self.action = "jumping"
        #elif self.action != "jumping":
        #    self.action = "running"

        #if self.step >=10:
        #    self.step = 0

    def duck(self):
        self.update_image(DUCKING_IMG[self.type][self.step // 5], pos_y=self.POS_Y_DUCK)
        self.step += 1

    def update_image(self, image: pygame.Surface, pos_x = None, pos_y = None):
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = pos_x or self.POS_X
        self.rect.y = pos_y or self.POS_Y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up(self, power_up):
        self.type = power_up.type
        self.power_up_time_up = power_up.start_time + (power_up.duration * 1000)

    def draw_power_up(self, screen):
        if self.type != DEFAULT_TYPE:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message(
                    f"{self.type.capitalize()} enabled for {time_to_show} seconds.",
                    screen,
                    font_size = 22,
                    pos_y_center = 50)
            else:
                self.type = DEFAULT_TYPE
                self.power_up_time_up = 0
                
        
