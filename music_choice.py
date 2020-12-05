from pygame import mixer
import os
import music
import config
import davis

### Will choose music to play based on several factors

def encounter_choice(enemy):
    type = enemy.type
    if type == "220 Student":
        davis.music_player.play_enemy1()
    if type == "AI Violation Email":
        davis.music_player.play_enemy2()
    if type == "Deadline":
        davis.music_player.play_enemy3()
    if type == "DJ Khaled":
        davis.music_player.play_enemy4()
    if type == "Wet Floor Sign":
        davis.music_player.play_enemy5()