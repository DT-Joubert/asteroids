import pygame # type: ignore
from circleshape import CircleShape
from constants import *
from bullet import Bullet


class Player(CircleShape):
    def __init__(self, x, y, alive_callback=None, reset_callback=None):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.alive_callback = alive_callback
        self.reset_callback = reset_callback

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # type: ignore
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # type: ignore
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT


    def shoot(self, x, y, radius):
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
        bullet = Bullet(x, y, radius)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED



    def update(self, dt):
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt

        keys = pygame.key.get_pressed()

        if self.alive_callback():
            if keys[pygame.K_a]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_w]:
                self.move(dt)
            if keys[pygame.K_s]:
                self.move(-dt)
            if keys[pygame.K_SPACE]:
                if(self.shot_cooldown <= 0):
                    self.shoot(self.position.x, self.position.y, SHOT_RADIUS)
        else:
            if keys[pygame.K_RETURN]:
                self.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                self.reset_callback()

    