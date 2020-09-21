import pygame
import unittest
import time
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import music

class TestMusic(unittest.TestCase):

    def test_volume(self):
        music_player = music.Music_Player()
        vol_pass = music_player.set_volume(volume = 0.2)
        vol_fail = music_player.set_volume(volume = 33)
        self.assertEqual(vol_pass, True)
        self.assertEqual(vol_fail, False)


if __name__ == '__main__':
    pygame.init()
    unittest.main()