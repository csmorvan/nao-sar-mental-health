
# NOTE:
# Audio files must be manually uploaded to the NAO robot.
# Expected location on robot:
#   /home/nao/music/
# Upload command (when robot is accessible):
#   scp audio/calm_music.mp3 nao@<ROBOT_IP>:/home/nao/music/


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

def break_module(tts, posture, audio, leds=None):
    """
    Plays calming music and guides the user through a short relaxation break.
    - Moves NAO into a relaxed posture
    - Fades LEDs to a calming color (optional)
    - Plays a music file stored on NAO
    """

    tts.say("Sure. Let's take a calm break together.")
    tts.say("Find a comfortable position and take a moment to relax.")

    # Move NAO into a relaxed position
    posture.goToPosture("SitRelax", 0.6)

    # Optional calming LED color (soft blue)
    try:
        if leds:
            leds.fadeRGB("FaceLeds", 0x3366FF, 1.5)
    except:
        pass  # LED hardware may not be available on all NAOs

    # Path to calming music file on the robot
    # Make sure you upload this file to your NAO at this location
    # music_path = "/home/nao/music/massobeats - rose water.mp3" -> NAO
    music_file = self.getPackagePath() + "/sounds/rose.mp3" # -> for Choregraphe

    # Try playing your calming audio file
    try:
        audio_id = audio.playFile(music_file)
        time.sleep(15)   # Let the music play (adjust duration if needed)
    except Exception as e:
        print("Audio playback failed:", e)
        tts.say("I couldn't play the audio file, but we can still take a quiet moment together.")
        time.sleep(20)

    tts.say("I hope you're feeling a bit more relaxed now.")
    tts.say("Let me know if you'd like to continue.")
