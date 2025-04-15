import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet
from gamestate import ScoreTracker



def display_score(screen, score):
    pygame.font.init()
    my_font = pygame.font.SysFont('Arial', 30)
    text_surface = my_font.render(f"{score}", True, (200, 0, 0))
    screen.blit(text_surface, (10,10))





def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Bullet.containers = (updatable, drawable, bullets)
    
    


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score_tracker = ScoreTracker()
    asteroid_field = AsteroidField(score_tracker.add)

    is_alive = True


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        if(is_alive):
            updatable.update(dt)
            
            for obj in asteroids:
                if obj.is_colliding(player):
                    print("GAME OVER!")
                    print(f"FINAL SCORE : {score_tracker.score}")
                    return
                
                for bullet in bullets:
                    if bullet.is_colliding(obj):
                        bullet.kill()
                        obj.split()


            for obj in drawable:
                obj.draw(screen)
            
            display_score(screen, score_tracker.score)


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()




