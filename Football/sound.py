import winsound
from pygame import mixer

def Ball_Kick():
    winsound.PlaySound("ball_kick.wav", winsound.SND_ASYNC)


def Song_TeamA():
    winsound.PlaySound("Team_A.wav", winsound.SND_ASYNC)

def Song_TeamB():
     winsound.PlaySound("Team_B.wav", winsound.SND_ASYNC)


def Whistle():
    winsound.PlaySound("whistle_sound.wav", winsound.SND_ASYNC)

def Background_Sound():
    mixer.init()
    mixer.music.load('YNWA.wav')
    mixer.music.play()


def Background_Play(a):
    if a == 1:
        mixer.music.pause()
    else:
        mixer.music.unpause()

def Menu_Sound():
    mixer.init()
    mixer.music.load('Wavin_Flag.wav')
    mixer.music.play()


def Menu_Play(a):
    if a == 1:
        mixer.music.pause()
    else:
        mixer.music.unpause()


def End_Whistle():
    winsound.PlaySound("EndWhist.wav", winsound.SND_ASYNC)

def ON():
    winsound.PlaySound("switch.wav", winsound.SND_ASYNC)

def Click():
    winsound.PlaySound("Click.wav", winsound.SND_ASYNC)

