from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BULLET_EDGE_COLORS, BULLET_FILL_COLORS, BULLET_RADIUS, SHOT_RADIUS
import pygame # type: ignore

class Bullet(CircleShape):
    def __init__(self, x, y, radius_level, speed_level):
        self.edge_color = BULLET_EDGE_COLORS.get(speed_level, "white")
        self.fill_color = BULLET_FILL_COLORS.get(radius_level, "white")
        self.radius = BULLET_RADIUS.get(radius_level, SHOT_RADIUS)
        super().__init__(x, y, self.radius)
        


    def draw(self, screen):
        pygame.draw.circle(screen, self.fill_color, self.position, self.radius) # type: ignore
        pygame.draw.circle(screen, self.edge_color, self.position, self.radius, 2) # type: ignore

    def out_of_bounds(self):
            return self.position.x < -10 or self.position.x > SCREEN_WIDTH + 10 or self.position.y < -10 or self.position.y > SCREEN_HEIGHT + 10

    def update(self, dt):
        self.position += self.velocity * dt 
        if self.out_of_bounds():
            self.kill()






    