from pygame import mixer

class Music_Player():
    def __init__(self):
        self.musicMixer = mixer.music

    def play_intro():
        self.musicMixer.load("intro.ogg")
        self.musicMixer.play()

    def play_scary():
        pass
    def play_normal():
        pass
    def play_victory():
        pass
    def stop():
        pass

