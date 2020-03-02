import sys
sys.path.append("/home/shachar/Desktop/projects/Pygame-engine")
from engine.sceneController import *
from engine.objects import *
import engine.settings as settings

class MainScene(Scene):

    bg = BackGround(["data/bg.jpg", "data/bg2.png", "data/bg3.png"], 1280, 720)
    player = KinematicBody(100, 500)

    @classmethod
    def _start(cls):
        print("scene2 starting")

    @classmethod
    def _loop(cls, delta):
        cls.bg.draw()

setScene(MainScene)