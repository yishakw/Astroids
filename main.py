import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Astroids")
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        updatable.update(dt)
        for obj in asteroids:
            if player.check_collision(obj):
                print("Game Over")
                pygame.quit()
                return
            for bullet in shots:
                if bullet.check_collision(obj):
                    obj.split()
                    bullet.kill()
                    obj.kill()
        screen.fill(("black"))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick()/1000
if __name__ == "__main__":
    main()  