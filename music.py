from pygame import mixer
import os
class Music_Player():
    def __init__(self):
        self.musicMixer = mixer.music
        filepath = os.path.abspath(__file__)
        self.filedir = os.path.dirname(filepath)

    ######### event specific play options #########
    def play_intro(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/intro.ogg")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_scary(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/scary.ogg")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)
    
    def play_normal(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/fast.ogg")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_victory(self):
        pass

    ######## Music Utilities ######

    # volume : float [0.0,1.0]; sets music volume  
    def set_volume(self, volume):
        try:
            self.musicMixer.set_volume(volume)
        except:
            print("unable to set volume")

    # get current music volume
    def get_volume(self):
        try:
            return self.musicMixer.get_volume()
        except:
            print("unable to get volume")

    # increment : float [0.0, 1.0]; increases current volume by 'increment' amount
    def increase_volume(self, increment):
        current_vol = self.musicMixer.get_volume()
        try:
            assert isinstance(increment, float)
            self.set_volume(current_vol + increment)
        except:
            print("could not increase volume")

    # increment : float [0.0, 1.0]; decreases current volume by 'increment' amount
    def decrease_volume(self, increment):
        current_vol = self.musicMixer.get_volume()
        try:
            assert isinstance(increment, float)
            self.set_volume(current_vol - increment)
        except:
            print("could not decrease volume")

    def pause(self):
        self.musicMixer.pause()

    def unpause(self):
        self.musicMixer.unpause()

    def stop(self):
        self.musicMixer.stop()