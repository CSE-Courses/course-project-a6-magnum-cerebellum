from pygame import mixer
import os
import music
import config
import encounter

### Will choose music to play based on several factors

current_enemy = None
dead = False

def encounter_choice(enemy):
    global dead
    dead = False
    if enemy.type == "Ethan":
        music_player = music.Music_Player()
        music_player.play_boss5()
    if current_enemy != enemy and encounter.music_steps > 50000:
        music_player = music.Music_Player()
        type = enemy.type
        if type == "220 Student":
            music_player.play_enemy1()
        if type == "AI Violation Email":
            music_player.play_enemy2()
        if type == "Deadline":
            music_player.play_enemy4()
        if type == "DJ Khaled":
            music_player.play_enemy3()
        if type == "Wet Floor Sign":
            music_player.play_enemy5()
        encounter.music_steps = 0

def death():
    global dead
    if not dead:
        encounter.boss_flag = False
        encounter.boss_defeated = False
        encounter.enemy_selected = False
        config.boss_initiate = False
        music_player = music.Music_Player()
        music_player.play_ambtrack8()
        dead = True

def win():
    music_player = music.Music_Player()
    music_player.play_ambtrack10()

