from . import settings

def change_current_scene(scene):
    settings.currentScene = scene

def change_current_scene_run(run):
    if settings.currentScene:
        settings.currentScene._run = run