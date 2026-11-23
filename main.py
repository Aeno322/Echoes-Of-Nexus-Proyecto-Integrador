import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *

from sound import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.level = 1
        self.level_start_time = 0
        self.new_game()

    def new_game(self):
        self.level = 1
        self._setup_level(self.level)

    def _setup_level(self, level):
        self.level = level
        self.map = Map(self, level=level)
        self.player = Player(self)
        pos = LEVELS[level - 1]['player_pos']
        self.player.x, self.player.y = pos
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.sound = Sound(self)        
        self.level_start_time = pg.time.get_ticks()
        if not pg.mixer.music.get_busy():
            pg.mixer.music.play(-1)

    def next_level(self):
        if self.level >= len(LEVELS):
            self.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.new_game()
        else:
            hp = self.player.health if hasattr(self, 'player') else PLAYER_MAX_HEALTH
            self._setup_level(self.level + 1)
            self.player.health = min(PLAYER_MAX_HEALTH, hp + 50)

    def time_left(self):
        if not self.level_start_time:
            return LEVEL_DURATION
        return max(0, LEVEL_DURATION - (pg.time.get_ticks() - self.level_start_time))

    def check_level_complete(self):
        if self.time_left() <= 0:
            self.next_level()

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.check_level_complete()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
