# -*- coding: utf-8 -*-
# NAO Mental Health Assistive Robot Modules
# Works with Python 2.7 and NAOqi 2.1+

from naoqi import ALProxy
import time
import random

# ---------------------------
# Robot Connection Info
# ---------------------------
ROBOT_IP   = "127.0.0.1"   # change to NAO's IP
ROBOT_PORT = 9559

tts      = ALProxy("ALTextToSpeech", ROBOT_IP, ROBOT_PORT)
motion   = ALProxy("ALMotion", ROBOT_IP, ROBOT_PORT)
posture  = ALProxy("ALRobotPosture", ROBOT_IP, ROBOT_PORT)
audio    = ALProxy("ALAudioPlayer", ROBOT_IP, ROBOT_PORT)

# -----------------------------------------------------------
# MODULE 2: POSITIVE AFFIRMATIONS
# -----------------------------------------------------------

def affirmations_module():
    """
    Selects and speaks a random positive affirmation.
    """
    affirmations = [
        "It's okay to rest when you need to.",
        "You are doing the best you can today.",
        "I am proud of how far you have come.",
        "You deserve moments of calm and peace.",
        "Your effort matters, even when you can't see it.",
        "You are strong, capable, and learning every day.",
        "Take things one step at a time. You're doing great."
    ]

    message = random.choice(affirmations)
    tts.say("Here is a positive message for you.")
    tts.say(message)

# -----------------------------------------------------------
# OPTIONAL: BREAK MODULE (if needed later)
# -----------------------------------------------------------

def calm_break():
    """
    Plays a calm sound / music file.
    """
    tts.say("Sure. Let's take a calm break together.")
    # Example: play a sound file from NAO robot storage
    # audio.playFile("/home/nao/sounds/meditation.wav")
    tts.say("Imagine a peaceful place while you listen for a moment.")
    time.sleep(10)
    tts.say("Whenever you're ready, we can continue.")

# -----------------------------------------------------------
# Example test run (remove when used in Choregraphe box)
# -----------------------------------------------------------

if __name__ == "__main__":
    affirmations_module()
def break_module():
    """
    Calming break: soft breathing LED pattern + music.
    """

    tts.say("Let's take a calm break. You deserve a moment to relax.")

    posture.goToPosture("SitRelax", 0.6)

    # LED breathing pattern
    try:
        leds = ALProxy("ALLeds", ROBOT_IP, ROBOT_PORT)
    except:
        leds = None

    # Start calm music
    try:
        music_file = "/home/nao/music/calm_music.wav"
        audio_id = audio.playFile(music_file)
    except:
        audio_id = None

    # LED breathing cycles
    if leds:
        for i in range(3):
            leds.fadeRGB("ChestLeds", 0x0033FF, 2.0)  # fade in blue (2s)
            time.sleep(2)
            leds.fadeRGB("ChestLeds", 0x000000, 2.0)  # fade out
            time.sleep(2)

    # Stop audio if still playing
    if audio_id is not None:
        audio.stop(audio_id)

    tts.say("I hope you're feeling calmer now.")
