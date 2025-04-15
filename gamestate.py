from constants import *

class ScoreTracker:
    def __init__(self):
        self.score = 0

    def add(self, amount):
        self.score += amount

class LivesTracker:
    def __init__(self):
        self.lives = PLAYER_STARTING_LIVES

    def add(self):
        self.lives += 1

    def subtract(self):
        self.lives -= 1

class WeaponTracker:
    def __init__(self):
        self.main_speed_level = 1
        self.main_speed_level_max = 3
        self.main_radius_level = 1
        self.main_radius_level_max = 3
        self.split_level = 1
        self.split_level_max = 3
        self.split_speed = 1
        self.split_speed_max = 3
        self.split_radius_level = 1
        self.split_radius_level_max = 3

    
    