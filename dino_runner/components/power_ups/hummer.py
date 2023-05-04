from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HUMMER_TYPE


class Hummer(PowerUp):
    def __init__(self):
        super().__init__(HAMMER, HUMMER_TYPE)
