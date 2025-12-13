from naoqi import ALProxy
import time
import math

# NOTE ON AUDIO TESTING IN CHOREGRAPHE TESTER:
# ------------------------------------------------------------
# Audio playback is intentionally disabled. The robot waits for
# the song duration (2 min 20 sec) while performing calm motions.
# Audio will be added later during video editing.
# ------------------------------------------------------------

ROBOT_IP   = "127.0.0.1"   # OK for Tester
ROBOT_PORT = 9559

tts     = ALProxy("ALTextToSpeech", ROBOT_IP, ROBOT_PORT)
motion  = ALProxy("ALMotion", ROBOT_IP, ROBOT_PORT)
posture = ALProxy("ALRobotPosture", ROBOT_IP, ROBOT_PORT)

try:
    leds = ALProxy("ALLeds", ROBOT_IP, ROBOT_PORT)
except:
    leds = None


def calm_motion_cycle(motion, leds=None):
    """
    One short calming motion cycle (~5 seconds)
    """
    # Breathing-like arm motion
    names  = ["LShoulderPitch", "RShoulderPitch"]
    angles = [1.2, 1.2]   # relaxed
    times  = [2.5, 2.5]
    motion.angleInterpolation(names, angles, times, True)

    angles = [1.4, 1.4]
    motion.angleInterpolation(names, angles, times, True)

    # Small head nod
    motion.angleInterpolation("HeadPitch", 0.15, 1.5, True)
    motion.angleInterpolation("HeadPitch", 0.0, 1.5, True)

    # Soft LED pulse (optional)
    if leds:
        try:
            leds.fadeRGB("FaceLeds", 0x3366FF, 1.5)  # soft blue
            leds.fadeRGB("FaceLeds", 0x000000, 1.5)
        except:
            pass


def break_module(tts, posture, audio=None, leds=None):
    tts.say("Sure. Let's take a calm break together.")
    tts.say("Find a comfortable position and take a moment to relax.")

    posture.goToPosture("SitRelax", 0.6)

    # ----------------------------
    # MUSIC DISABLED FOR TEST VIDEO
    # ----------------------------
    # audio.playFile("/home/nao/music/rose_water.wav")

    SONG_DURATION = 140  # seconds (2 min 20 sec)
    CYCLE_TIME    = 7    # approx duration of one calm cycle

    cycles = int(SONG_DURATION / CYCLE_TIME)

    for _ in range(cycles):
        calm_motion_cycle(motion, leds)

    tts.say("I hope you're feeling a bit more relaxed now.")
    tts.say("Let me know if you'd like to continue.")
