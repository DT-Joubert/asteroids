import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet
from gamestate import ScoreTracker




def display_score(screen, score):
    my_font = pygame.font.SysFont('Arial', 30)
    text_surface = my_font.render(f"{score}", True, (200, 0, 0))
    screen.blit(text_surface, (10,10))


def display_game_over(screen, score):
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    game_over_font = pygame.font.SysFont('Arial', 30)
    high_score_font = pygame.font.SysFont('Arial', 35)
    press_enter_font = pygame.font.SysFont('Arial', 30)

    top_surface = game_over_font.render("GAME OVER", True, (255, 255, 255))
    top_width = top_surface.get_width()
    top_height = top_surface.get_height()
    top_x = (screen_width - top_width) // 2
    top_y = (screen_height - top_height) // 2 + 50

    middle_surface = high_score_font.render(f"HIGH SCORE: {score}", True, (255, 255, 255))
    middle_width = middle_surface.get_width()
    middle_height = middle_surface.get_height()
    middle_x = (screen_width - middle_width) // 2
    middle_y = (screen_height - middle_height) // 2


    bottom_surface = high_score_font.render("PRESS [ENTER] TO PLAY", True, (255, 255, 255))
    bottom_width = bottom_surface.get_width()
    bottom_height = bottom_surface.get_height()
    bottom_x = (screen_width - bottom_width) // 2
    bottom_y = (screen_height - bottom_height) // 2 - 50


    screen.blit(top_surface, (top_x, top_y))
    screen.blit(middle_surface, (middle_x, middle_y))
    screen.blit(bottom_surface, (bottom_x, bottom_y))





def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    pygame.font.init()
    print("Starting Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    is_alive = True

    user = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()


    Player.containers = (updatable, drawable, user)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Bullet.containers = (updatable, drawable, bullets)
    
    score_tracker = ScoreTracker()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField(score_tracker.add)

    def reset_game():
        nonlocal is_alive, player
        score_tracker.score = 0
        player.position.x = SCREEN_WIDTH / 2
        player.position.y = SCREEN_HEIGHT / 2
        is_alive = True



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return

        screen.fill("black")


        
        if(is_alive):
            updatable.update(dt)

            for obj in asteroids:
                if obj.is_colliding(player):
                    print("GAME OVER!")
                    print(f"FINAL SCORE : {score_tracker.score}")
                    for asteroid in asteroids:
                        asteroid.kill()
                    for bullet in bullets:
                        bullet.kill()
                    is_alive = False
                
                for bullet in bullets:
                    if bullet.is_colliding(obj):
                        bullet.kill()
                        obj.split()


            for obj in drawable:
                obj.draw(screen)
            
            display_score(screen, score_tracker.score)
        else :
            if keys[pygame.K_RETURN]:
                reset_game()
            display_game_over(screen, score_tracker.score)


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()




