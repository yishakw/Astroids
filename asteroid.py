import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        # Only split if large enough
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # First asteroid: rotate +angle and speed up
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = self.velocity.rotate(random_angle) * 1.2
            a1.add(self.containers)

            # Second asteroid: rotate -angle and speed up
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = self.velocity.rotate(-random_angle) * 1.2
            a2.add(self.containers)
        