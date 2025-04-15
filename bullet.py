from circleshape import CircleShape
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
import pygame # type: ignore

class Bullet(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2) # type: ignore

    def out_of_bounds(self):
            return self.position.x < -10 or self.position.x > SCREEN_WIDTH + 10 or self.position.y < -10 or self.position.y > SCREEN_HEIGHT + 10

    def update(self, dt):
        self.position += self.velocity * dt 
        if self.out_of_bounds():
            self.kill()


    