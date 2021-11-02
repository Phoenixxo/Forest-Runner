import pygame
from pygame.math import Vector2
from base import Entity

bat_f = pygame.image.load("D:\\Projects\\SideScroller\\batF.png")
bat_f = pygame.transform.scale(bat_f, (50, 50))

screen = pygame.display.set_mode((1280, 720))


class Player(Entity):
    """Player Class"""

    def __init__(self):
        Entity.__init__(self)
        self.image = bat_f
        self.rect = self.image.get_rect()
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = 0.35, -0.12
        self.position, self.velocity = Vector2(0, 0), Vector2(0, 0)
        self.acceleration = Vector2(0, self.gravity)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, dt):
        self.draw()
        self.horizontal_movement(dt)
        self.vertical_movement(dt)

    def horizontal_movement(self, dt):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= 0.5
        elif self.RIGHT_KEY:
            self.acceleration.x += 0.5

        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity()
        self.position.x += (self.velocity.x * dt) + (
            0.5 * self.acceleration.x * (dt * dt)
        )
        self.rect.x = self.position.x

    def vertical_movement(self, dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7:
            self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * 0.5) * (
            dt * dt
        )
        if self.position.y > 600:
            self.on_ground = True
            self.velocity.y = 0
            self.position.y = 600
        self.rect.bottom = self.position.y

    def limit_velocity(self, max_vel=4):
        "Handles velocity maxing out and not becoming unplayable. The Max_Vel is set to 4 by default but can be changed if a number is passed into the function."
        self.velocity.x = max(-max_vel, min(self.velocity.x, max_vel))
        if abs(self.velocity.x) < 0.01:
            self.velocity.x = 0

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 8
            self.on_ground = False
