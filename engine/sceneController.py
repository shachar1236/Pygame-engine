import pygame
from . import settings
from . import _globals
pygame.init()

class Scene():
    _run = False

    @classmethod
    def _start(cls):
        print("start")

    @classmethod
    def _loop(cls, delta):
        print("loop")

    @classmethod
    def _loop_(cls):
        clock = pygame.time.Clock()
        while cls._run:
            delta = clock.tick(60)
            delta = float(delta) / 10
            cls._loop(delta)

    @classmethod
    def _changeRun(cls, var):
        _run = var

def setScene(s):
    _globals.change_current_scene_run(False)
    s._run = True
    _globals.change_current_scene(s)
    s._start()
    s._loop_()


