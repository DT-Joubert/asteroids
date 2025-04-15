from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from powerups import *
import pygame # type: ignore
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, player, bullets):
        super().__init__(x, y, radius)

        self.player = player
        self.bullets = bullets
       

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


        if self.is_colliding(self.player):
                self.player.die()
        else:
            for bullet in self.bullets:
                if self.is_colliding(bullet):
                    bullet.kill()
                    self.split()





    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            self.player.score += 20
            self.roll_loot_spawn()
            return
        
        new_angle = random.uniform(20, 50)
        vec_a = self.velocity.rotate(new_angle)
        vec_b = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius, self.player, self.bullets)
        new_asteroid_a.velocity = vec_a * 1.2
        new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius, self.player, self.bullets)
        new_asteroid_b.velocity = vec_b * 1.2
        self.player.score += 5
        self.roll_loot_spawn()






    def roll_loot_spawn(self):

        chance = (self.player.main_speed_level + self.player.main_radius_level + self.player.split_level + self.player.split_speed_level + self.player.split_radius_level) * self.player.lives

        main_roll = random.randint(1, chance)
        if main_roll == 1:

            if(self.player.split_level == 1):
                drop_roll = random.randint(1, 4)
            else:
                drop_roll = random.randint(1, 6)
    
            if drop_roll == 1:
                print("EXTRA LIFE")
                ExtraLife(self.position.x, self.position.y, self.player)
            elif drop_roll == 2:
                print("MAIN GUN SPEED BOOST")
                MainGunSpeedBoost(self.position.x, self.position.y, self.player)
            elif drop_roll == 3:
                print("MAIN GUN RADIUS BOOST")
                MainGunRadiusBoost(self.position.x, self.position.y, self.player)
            elif drop_roll == 4:
                print("SPLIT GUN LEVEL BOOST")
                SplitGunLevelBoost(self.position.x, self.position.y, self.player)
            elif drop_roll == 5:
                print("SPLIT GUN SPEED BOOST")
                SplitGunSpeedBoost(self.position.x, self.position.y, self.player)
            elif drop_roll == 6:
                print("SPLIT GUN RADIUS BOOST")
                SplitGunRadiusBoost(self.position.x, self.position.y, self.player)




