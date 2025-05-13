import pygame
from constants import *
from player import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Astroids")
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.containers = (updatable, drawable)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        updatable.update(dt)
        screen.fill(("black"))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick()/1000
if __name__ == "__main__":
    main()  