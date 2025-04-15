from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame # type: ignore
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) # type: ignore

    def update(self, dt):
        self.position += self.velocity * dt   

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        new_angle = random.uniform(20, 50)
        vec_a = self.velocity.rotate(new_angle)
        vec_b = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_a.velocity = vec_a * 1.2
        new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_b.velocity = vec_b * 1.2