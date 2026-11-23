from sprite_object import *
from collections import deque
import random
from random import randint, choices, randrange


class WeaponPickup:
    """Pickup de arma que flota en el mapa hasta que el jugador lo recoge."""

    def __init__(self, game, weapon_id, pos, sprite_path='resources/sprites/static_sprites/candlebra.png'):
        cfg = next(w for w in WEAPON_TYPES if w['id'] == weapon_id)
        self.weapon_id = weapon_id
        self.cfg = cfg
        self.sprite = SpriteObject(game=game, path=sprite_path, pos=pos, scale=0.35, shift=0.0)
        self.game = game
        self.x, self.y = pos
        self.life = pg.time.get_ticks()
        self.collected = False

    def update(self):
        self.sprite.update()
        if pg.time.get_ticks() - self.life > WEAPON_PICKUP_LIFETIME:
            self.collected = True
            self.game.object_handler.on_pickup_expired(self)

    def check_pickup(self):
        if not self.collected and abs(self.x - self.game.player.x) < 0.7 and abs(self.y - self.game.player.y) < 0.7:
            self.game.object_handler.on_pickup_collected(self)


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.pickups = []


        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_timer = 0

    def _populate_statics(self):
        add_sprite = self.add_sprite
        add_sprite(AnimatedSprite(self.game))
        add_sprite(AnimatedSprite(self.game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(self.game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(self.game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(self.game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(self.game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(self.game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(self.game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(self.game, pos=(14.5, 4.5)))
        add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 5.5)))
        add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))
        add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 12.5)))
        add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 20.5)))
        add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(10.5, 20.5)))
        add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5, 14.5)))
        add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5, 18.5)))
        add_sprite(AnimatedSprite(self.game, pos=(14.5, 24.5)))
        add_sprite(AnimatedSprite(self.game, pos=(14.5, 30.5)))
        add_sprite(AnimatedSprite(self.game, pos=(1.5, 30.5)))
        add_sprite(AnimatedSprite(self.game, pos=(1.5, 24.5)))

    def _free_cell(self, min_dist=5):
        player_pos = self.game.player.map_pos
        for _ in range(200):
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            if pos in self.game.map.world_map or pos in self.restricted_area or pos in self.game.object_handler.npc_positions:
                continue
            if abs(pos[0] - player_pos[0]) + abs(pos[1] - player_pos[1]) < min_dist:
                continue
            return (x + 0.5, y + 0.5)
        return None

        

    def reset(self):
        self.pickups = []
        self.sprite_list = []
        self.spawn_timer = 0
        self.pending_weapons = [w['id'] for w in WEAPON_TYPES if w['id'] != WEAPON_STARTING]
        random.shuffle(self.pending_weapons)
        self.spawned_weapon_ids = set()
        self.collected_weapon_ids = set()
        self.respawn_queue = []
        self._populate_statics()

    def check_win(self):
        pass

    def update(self):
        cfg = LEVELS[self.game.level - 1]
        now = pg.time.get_ticks()
        if self.game.level_start_time and now - self.spawn_timer >= self._next_spawn_delay:
            self.spawn_timer = now
            self._next_spawn_delay = randint(*cfg['spawn_interval'])
        [sprite.update() for sprite in self.sprite_list]

        self.pickups[:] = [p for p in self.pickups if not p.collected]



    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    @property
    def _next_spawn_delay(self):
        cfg = LEVELS[self.game.level - 1]
        if not hasattr(self, '_spawn_delay'):
            self._spawn_delay = randint(*cfg['spawn_interval'])
        return self._spawn_delay

    @_next_spawn_delay.setter
    def _next_spawn_delay(self, value):
        self._spawn_delay = value
