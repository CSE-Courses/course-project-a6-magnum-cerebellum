import pygame
from config import *
from collections import deque
import health


class Sprites:
    def __init__(self):
        self.sprite_parameters = {
            'barrel': { 
                'name': "barrel",
                'sprite': pygame.image.load('assets/sprites/barrel/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': 0.4,
                'animation': deque(
                    [pygame.image.load(f'assets/sprites/barrel/anim/{i}.png').convert_alpha() for i in range(12)]),
                'animation_dist': 800,
                'animation_speed': 10,
                'pickup': False,
                'used': False,
                 },
            'health': { 
                'name': "health",
                'sprite': pygame.image.load('assets/sprites/health/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': 0.5,
                'animation': deque(
                    [pygame.image.load(f'assets/sprites/health/anim/{i}.png').convert_alpha() for i in range(4)]),
                'animation_dist': 800,
                'animation_speed': 10,
                'pickup': True,
                'used': False,
                 },
            'mana': { 
                'name': "mana",
                'sprite': pygame.image.load('assets/sprites/mana/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': 0.5,
                'animation': deque(
                    [pygame.image.load(f'assets/sprites/mana/anim/{i}.png').convert_alpha() for i in range(4)]),
                'animation_dist': 800,
                'animation_speed': 10,
                'pickup': True,
                'used': False,
                 }
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_parameters['barrel'], (7.1, 2.1)),
            SpriteObject(self.sprite_parameters['barrel'], (5.9, 2.1)),
            SpriteObject(self.sprite_parameters['barrel'], (5.7, 9.7)),
            SpriteObject(self.sprite_parameters['barrel'], (4.2, 13.3)),
            SpriteObject(self.sprite_parameters['barrel'], (22.5, 14.7)),
            SpriteObject(self.sprite_parameters['barrel'], (21.2, 8.9)),
            SpriteObject(self.sprite_parameters['barrel'], (18.6, 5.5)),

            SpriteObject(self.sprite_parameters['health'], (8.4, 10)),
            SpriteObject(self.sprite_parameters['mana'], (8.3, 14.5)),
            SpriteObject(self.sprite_parameters['mana'], (8.0, 2.8)),
            SpriteObject(self.sprite_parameters['health'], (1.1, 1.25)),
            SpriteObject(self.sprite_parameters['health'], (16.4, 2.6)),
            SpriteObject(self.sprite_parameters['mana'], (18.3, 1.3)),
            SpriteObject(self.sprite_parameters['health'], (20.7, 11.7)),
            SpriteObject(self.sprite_parameters['mana'], (20.7, 11.7)),
            SpriteObject(self.sprite_parameters['health'], (20.7, 11.7)),
            SpriteObject(self.sprite_parameters['mana'], (22.6, 11.8)),
            SpriteObject(self.sprite_parameters['mana'], (9.5, 10.5)),
            SpriteObject(self.sprite_parameters['health'], (2.5, 13.4)),
            SpriteObject(self.sprite_parameters['mana'], (10.5, 9.4)),
            SpriteObject(self.sprite_parameters['health'], (16.5, 4.3)),
            SpriteObject(self.sprite_parameters['health'], (21.3, 2.4)),
            SpriteObject(self.sprite_parameters['health'], (13.6, 14.4))
        ]


class SpriteObject:
    def __init__(self, parameters, pos):
        self.name = parameters['name']
        self.pickup = parameters['pickup']
        self.object = parameters['sprite']
        self.viewing_angles = parameters['viewing_angles']
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = parameters['animation'].copy()
        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.used = parameters['used']
        self.animation_count = 0
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE
        if self.viewing_angles:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    def object_locate(self, player, bar):
        
        if self.used is True:
            return (False, )
        
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

      
        if self.pickup is True and distance_to_sprite <= 50:
            self.used = True
            if self.name == "health":
                bar.addHealth(25)
                text1.append("Picked up Health")
            if self.name == "mana":
                bar.addMana(25)
                text1.append("Picked up Mana")

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        distance_to_sprite *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        fake_ray = current_ray + FAKE_RAYS
        if 0 <= fake_ray <= FAKE_RAYS_RANGE and distance_to_sprite > 30:
            proj_height = min(int(PROJ_COEFF / distance_to_sprite * self.scale), render_display_height*2)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift
            # choosing sprite for angle
            if self.viewing_angles:
                if theta < 0:
                    theta += DOUBLE_PI
                theta = 360 - int(math.degrees(theta))

                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break

            # sprite animation
            sprite_object = self.object
            if self.animation and distance_to_sprite < self.animation_dist:
                sprite_object = self.animation[0]
                if self.animation_count < self.animation_speed:
                    self.animation_count += 1
                else:
                    self.animation.rotate()
                    self.animation_count = 0

            # sprite scale and pos
            sprite_pos = (current_ray * SCALE - half_proj_height, render_display_height//2 - half_proj_height + shift)
            sprite = pygame.transform.scale(sprite_object, (proj_height, proj_height))
            return (distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)