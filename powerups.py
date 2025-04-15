import pygame # type: ignore
from circleshape import CircleShape


class ExtraLife(CircleShape):
    def __init__(self, x, y, player):
        super().__init__(x, y, 15)
        self.rotation = 180
        self.player = player

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # type: ignore
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius #/ 1.5 # type: ignore
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right / 1.5
        c = self.position - forward * self.radius + right / 1.5
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "blue", self.triangle())

    def update(self, dt):
        if self.is_colliding(self.player):
            if self.player.lives < 99:
                self.player.lives += 1
            self.kill()






class MainGunSpeedBoost(CircleShape):
    def __init__(self, x, y, player):
        super().__init__(x, y, 20)
        self.rotation = 0
        self.player = player

    def diamond(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # type: ignore
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # type: ignore
        a = self.position + forward * self.radius
        b = self.position - right
        c = self.position - forward * self.radius
        d = self.position + right
        return [a, b, c, d]

    def draw(self, screen):
        pygame.draw.polygon(screen, "cyan", self.diamond(), 5)

    def update(self, dt):
        if self.is_colliding(self.player):
            if self.player.main_speed_level < 3:
                self.player.main_speed_level += 1
            self.kill()



class MainGunRadiusBoost(CircleShape):
    def __init__(self, x, y, player):
        super().__init__(x, y, 20)
        self.rotation = 0
        self.player = player

    def diamond(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # type: ignore
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # type: ignore
        a = self.position + forward * self.radius
        b = self.position - right
        c = self.position - forward * self.radius
        d = self.position + right
        return [a, b, c, d]

    def draw(self, screen):
        pygame.draw.polygon(screen, "cyan", self.diamond())

    def update(self, dt):
        if self.is_colliding(self.player):
            if self.player.main_radius_level < 3:
                self.player.main_radius_level += 1
            self.kill()



class SplitGunLevelBoost(CircleShape):
    def __init__(self, x, y, player):
        super().__init__(x, y, 20)
        self.rotation = 0
        self.player = player

    def diamond(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # type: ignore
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # type: ignore
        a = self.position + forward * self.radius
        b = self.position - right
        c = self.position - forward * self.radius
        d = self.position + right
        return [a, b, c, d]

    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.diamond())
        pygame.draw.polygon(screen, "white", self.diamond(), 5)


    def update(self, dt):
        if self.is_colliding(self.player):
            if self.player.split_level < 3:
                self.player.split_level += 1
            self.kill()


class SplitGunSpeedBoost(CircleShape):
    def __init__(self, x, y, player):
        super().__init__(x, y, 20)
        self.rotation = 0
        self.player = player

    def diamond(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # type: ignore
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # type: ignore
        a = self.position + forward * self.radius
        b = self.position - right
        c = self.position - forward * self.radius
        d = self.position + right
        return [a, b, c, d]

    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.diamond(), 5)

    def update(self, dt):
        if self.is_colliding(self.player):
            if self.player.split_speed_level < 3:
                self.player.split_speed_level += 1
            self.kill()



class SplitGunRadiusBoost(CircleShape):
    def __init__(self, x, y, player):
        super().__init__(x, y, 20)
        self.rotation = 0
        self.player = player

    def diamond(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # type: ignore
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # type: ignore
        a = self.position + forward * self.radius
        b = self.position - right
        c = self.position - forward * self.radius
        d = self.position + right
        return [a, b, c, d]

    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.diamond())


    def update(self, dt):
        if self.is_colliding(self.player):
            if self.player.split_radius_level < 3:
                self.player.split_radius_level += 1
            self.kill()

