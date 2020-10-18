from pygame import mixer
import os


class Music_Player():
    def __init__(self):
        self.musicMixer = mixer.music
        filepath = os.path.abspath(__file__)
        self.filedir = os.path.dirname(filepath)

    ######### event specific play options #########

    ################################################
    # The following are ambient area/general map exploration tracks

    def play_ambtrack1(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/ambient/5spooky.it")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_ambtrack2(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/ambient/el_topo_-_horror_dub.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_ambtrack3(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/ambient/horror_naturalis.xm")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_ambtrack4(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/ambient/horror_trip.xm")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_ambtrack5(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/ambient/horrorvision_final.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_ambtrack6(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/ambient/jaktar-dungeons-1.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_ambtrack7(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/ambient/jaktar-dungeons-2.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_ambtrack8(self):
        musicpath = os.path.join(self.filedir, "/assets/music/music_files/in_use/ambient/jaktar-dungeons-3.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_ambtrack9(self):
        musicpath = os.path.join(self.filedir, "/assets/music/music_files/in_use/ambient/scary.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_ambtrack10(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/ambient/techno-time.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    #######################################
    # The following are tracks for bosses

    def play_boss1(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/boss/ace_de_techno_ii.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_boss2(self):
        musicpath = os.path.join (self.filedir, "assets/music/music_files/in_use/boss/akira.xm")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_boss3(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/boss/firage_-_the_grim_reaper_blows_the_horn.it")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_boss4(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/boss/horror_ist_pissed_2.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_boss5(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/boss/nitemare.it")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops=-1)

    def play_boss6(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/boss/techno_x.s3m")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    ###############################################
    # The following are tracks for random enemy encounters

    def play_enemy1(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/enemy_encounter/banana_addiction.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_enemy2(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/enemy_encounter/goto80-technowonderland-73.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_enemy3(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/enemy_encounter/horrorhouse.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops=-1)

    def play_enemy4(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/enemy_encounter/scary_dreams.xm")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_enemy5(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/enemy_encounter/vision_thing.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    ###########################################
    # The following are tracks for the main menu and options menu.

    def play_main(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/main_menu/horror_in_slimland.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    def play_options(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/options_menu/horror2_the_revenge.mod")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    ################################################
    # The following track is a victory tune to be played upon defeating an enemy.

    def play_victory(self):
        musicpath = os.path.join(self.filedir, "assets/music/music_files/in_use/victory/crab_rave.mid")
        self.musicMixer.load(musicpath)
        self.musicMixer.play(loops = -1)

    #def play_victory(self):
    #    pass

    ######## Music Utilities ######

    # volume : float [0.0,1.0]; sets music volume  
    def set_volume(self, volume):
        try:
            assert isinstance(volume, float)
            self.musicMixer.set_volume(volume)
            return True
        except:
            self.musicMixer.set_volume(0.0)
            return False

    # get current music volume
    def get_volume(self):
        try:
            return self.musicMixer.get_volume()
        except:
            return 0.0

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