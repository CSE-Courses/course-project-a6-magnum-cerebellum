import json
import os
from actions import Action
import pygame
import random
import enemies
import random
import player
import game
import character

# Global variable to be used to count movements
step_counter = 0
encounter_trigger = 4096

# Implements a step counter in order to control random enemy encounters on the map

# Should be called at beginning of level and after every enemy encounter
def restart_encounters():
    global step_counter
    step_counter = 0
    print("Step counter is " + str(step_counter) + "\n")

def increment_step_counter():
    global step_counter
    step_counter += random.randrange(1, 128)
    print("Step counter after adding is " + str(step_counter) + "\n")
    if step_counter >= encounter_trigger:
        # Then trigger a battle with a random enemy
        #game.GameMain(0, __str__())
        print("Step counter at encounter is " + str(step_counter) + "\n")
        # Restart the counter
        restart_encounters()