from PIL import Image
import pygame
from . import settings
from . import _globals

class KinematicBody():
    
    def __init__(self, x, y, collision=None, sprite=None):
        self.x = x
        self.y = y
        self.collision = collision
        self.sprite = sprite

class StaticBody():

    def __init__(self, x, y, collision=None, sprite=None):
        self.x = x
        self.y = y
        self.collision = collision
        self.sprite = sprite

class Collision():
    pass

class CollisionShape():
    pass

class Sprite():
    
    def __init__(self, sprite):
        self.sprite = sprite

class AnimatedSprite():
    
    def __init__(self, sprites:list):
        self.sprites = sprites

class BackGround():
    def __init__(self, bgs:list, width, height):
        self.bgs = bgs
        self.width = width
        self.height = height
        self.bgs = [(pygame.image.load(bg), *Image.open(bg).size) for bg in bgs]
        self.screen = pygame.display.set_mode((width, height))

    def draw(self, *objects, y=0):
        x = 0
        for bg in self.bgs:
            self.screen.blit(bg[0], (x, y))
            x += bg[1]
        for element in objects:
            if element.sprite:
                self.screen.blit(element.sprite, (element.x, element.y))


class Camera():
    pass