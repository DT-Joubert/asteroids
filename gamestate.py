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


    
    