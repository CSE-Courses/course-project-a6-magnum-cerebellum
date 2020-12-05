from pygame import mixer
import os
import music
import config
import encounter
#from davis import music_player

### Will choose music to play based on several factors

current_enemy = None
dead = False

def encounter_choice(enemy):
    global dead
    dead = False
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
        music_player = music.Music_Player()
        music_player.play_ambtrack8()
        dead = True
