import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    BIRD_HEIGHTS = [250, 290, 320]

    def __init__(self, image):
        self.type = 0
        super.__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.step = 0
    
    def draw(self, screen):
        if self.step >= 5:
            self.step = 0
        self.image = BIRD[0] if self.step < 5 else BIRD[1]
        self.step += 1
        screen.blit(self.image, self.rect)