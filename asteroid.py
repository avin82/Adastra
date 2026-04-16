import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            small_asteroid_1 = pygame.math.Vector2.rotate(self.velocity, angle)
            small_asteroid_2 = pygame.math.Vector2.rotate(self.velocity, angle * -1)
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_1.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
            new_asteroid_2.velocity = pygame.math.Vector2.rotate(self.velocity, angle * -1) * 1.2