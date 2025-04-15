from circleshape import CircleShape
import pygame # type: ignore

class Bullet(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2) # type: ignore

    def update(self, dt):
        self.position += self.velocity * dt   