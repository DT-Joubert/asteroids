from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
import pygame # type: ignore
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius,  score_callback=None):
        super().__init__(x, y, radius)
        self.score_add = score_callback
       

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) # type: ignore

    def update(self, dt):
        self.position += self.velocity * dt   
        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = 0 - self.radius
        if self.position.x < 0 - self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = 0 - self.radius
        if self.position.y < 0 - self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            self.score_add(20)
            return
        
        new_angle = random.uniform(20, 50)
        vec_a = self.velocity.rotate(new_angle)
        vec_b = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius, self.score_add)
        new_asteroid_a.velocity = vec_a * 1.2
        new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius, self.score_add)
        new_asteroid_b.velocity = vec_b * 1.2
        self.score_add(5)