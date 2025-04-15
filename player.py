import pygame # type: ignore
from circleshape import CircleShape
from constants import *
from bullet import Bullet


class Player(CircleShape):
    def __init__(self, x, y, reset_callback=False):
        super().__init__(x, y, PLAYER_RADIUS)
        self.reset_callback = reset_callback
        self.lives = PLAYER_STARTING_LIVES
        self.rotation = 0
        self.score = 0
        self.main_shot_cooldown = PLAYER_BASE_SHOOT_COOLDOWN
        self.split_shot_cooldown = PLAYER_BASE_SHOOT_COOLDOWN
        self.movement_speed = PLAYER_BASE_SPEED


        self.main_speed_level = 1
        self.main_radius_level = 1
        self.split_level = 1
        self.split_speed_level = 1
        self.split_radius_level = 1



    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # type: ignore
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius #/ 1.5 # type: ignore
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right / 1.5
        c = self.position - forward * self.radius + right / 1.5
        return [a, b, c]
    

    def draw(self, screen):
        edge_color = PLAYER_EDGE_COLORS.get(self.main_speed_level, "white")
        fill_color = PLAYER_FILL_COLORS.get(self.main_radius_level, "white")
        pygame.draw.polygon(screen, fill_color, self.triangle())
        pygame.draw.polygon(screen, edge_color, self.triangle(), 5)


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.movement_speed * dt
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT



    def shoot_main(self, x, y):
        self.main_shot_cooldown = PLAYER_BASE_SHOOT_COOLDOWN * COOLDOWN_MULTIPLIERS.get(self.main_speed_level, PLAYER_BASE_SHOOT_COOLDOWN)
        bullet = Bullet(x, y, self.main_radius_level, self.main_speed_level)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def shoot_split(self, x, y):
        self.split_shot_cooldown = PLAYER_BASE_SHOOT_COOLDOWN * COOLDOWN_MULTIPLIERS.get(self.split_speed_level, PLAYER_BASE_SHOOT_COOLDOWN)
        if self.split_level > 1:
            bullet_1 = Bullet(x, y, self.split_radius_level, self.split_speed_level)
            bullet_1.velocity = pygame.Vector2(0,1).rotate(self.rotation + 12.5) * PLAYER_SHOOT_SPEED
            bullet_2 = Bullet(x, y, self.split_radius_level, self.split_speed_level)
            bullet_2.velocity = pygame.Vector2(0,1).rotate(self.rotation - 12.5) * PLAYER_SHOOT_SPEED
        if self.split_level > 2:
            bullet_3 = Bullet(x, y, self.split_radius_level, self.split_speed_level)
            bullet_3.velocity = pygame.Vector2(0,1).rotate(self.rotation + 45) * PLAYER_SHOOT_SPEED
            bullet_4 = Bullet(x, y, self.split_radius_level, self.split_speed_level)
            bullet_4.velocity = pygame.Vector2(0,1).rotate(self.rotation - 45) * PLAYER_SHOOT_SPEED


    def update(self, dt):
        if self.main_shot_cooldown > 0:
            self.main_shot_cooldown -= dt
        if self.split_shot_cooldown > 0:
            self.split_shot_cooldown -= dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if(self.main_shot_cooldown <= 0):
                self.shoot_main(self.position.x, self.position.y)
            if(self.split_shot_cooldown <= 0):
                self.shoot_split(self.position.x, self.position.y)


    def reset(self, is_new_game):
            self.reset_callback(is_new_game)
            if(is_new_game == True):
                self.score = 0
                self.lives = PLAYER_STARTING_LIVES

            self.position.x = SCREEN_WIDTH / 2
            self.position.y = SCREEN_HEIGHT / 2

            self.main_speed_level = 1
            self.main_radius_level = 1
            self.split_level = 1
            self.split_speed_level = 1
            self.split_radius_level = 1

    def die(self):
        self.lives -= 1
        if self.lives <= 0:
            print("GAME OVER!")
            print(f"FINAL SCORE : 000")
        else:
            self.reset(False)
            

    


    