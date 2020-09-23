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

    def test_song_stop(self):
        music_player = music.Music_Player()
        music_player.play_intro()
        self.assertEqual(music_player.musicMixer.get_busy(), True)
        music_player.stop()
        self.assertEqual(music_player.musicMixer.get_busy(), False)
    
    def test_song_pause(self):
        music_player = music.Music_Player()
        music_player.play_intro()
        music_player.set_volume(volume = 0.0)
        self.assertEqual(music_player.musicMixer.get_busy(), True)
        music_player.pause()
        pos_a = music_player.musicMixer.get_pos()
        time.sleep(3)
        pos_b = music_player.musicMixer.get_pos()
        self.assertEqual(pos_a, pos_b)
        music_player.unpause()
        pos_c = music_player.musicMixer.get_pos()
        time.sleep(3)
        pos_d = music_player.musicMixer.get_pos()
        self.assertNotEqual(pos_c, pos_d)

if __name__ == '__main__':
    pygame.init()
    unittest.main()