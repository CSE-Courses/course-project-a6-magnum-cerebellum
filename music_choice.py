from pygame import mixer
import os
import music
import config
#from davis import music_player

### Will choose music to play based on several factors

def encounter_choice(enemy):
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