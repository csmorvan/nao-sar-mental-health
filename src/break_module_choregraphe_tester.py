from naoqi import ALProxy
import time

# NOTE ON AUDIO TESTING IN CHOREGRAPHE TESTER:
# ------------------------------------------------------------
# Choregraphe Tester / Simulated Robot does NOT emulate robot
# speaker hardware. Audio playback via ALAudioPlayer runs
# silently in Tester and can only be audibly verified on a
# physical NAO/Pepper robot.
#
# For this test/demo, music playback is intentionally DISABLED
# (commented out) because audio will be added later during
# video editing. Instead, the robot waits for the song duration
# (2 minutes 20 seconds) before speaking the final line.
# ------------------------------------------------------------

# ---------------------------
# Robot Connection Info
# ---------------------------
ROBOT_IP   = "127.0.0.1"   
ROBOT_PORT = 9559

def main():
    tts      = ALProxy("ALTextToSpeech", ROBOT_IP, ROBOT_PORT)
    motion   = ALProxy("ALMotion", ROBOT_IP, ROBOT_PORT)
    posture  = ALProxy("ALRobotPosture", ROBOT_IP, ROBOT_PORT)
    leds = ALProxy("ALLeds", ROBOT_IP, ROBOT_PORT)
    # audio    = ALProxy("ALAudioPlayer", ROBOT_IP, ROBOT_PORT)


    tts.say("Sure. Let's take a calm break together.")
    tts.say("Find a comfortable position and take a moment to relax.")

    # Move NAO into a relaxed position
    posture.goToPosture("SitRelax", 0.6)

    # Optional calming LED color (soft blue)
    try:
        if leds:
            leds.fadeRGB("FaceLeds", 0x3366FF, 1.5)
    except:
        pass

    # ----------------------------
    # MUSIC DISABLED FOR TEST VIDEO
    # ----------------------------
    # music_file = "/home/nao/music/rose_water.wav"
    # try:
    #     audio_id = audio.playFile(music_file)
    # except Exception as e:
    #     print("Audio playback failed:", e)

    # Wait for the song duration (2 min 20 sec = 140 sec)
    time.sleep(140)

    tts.say("I hope you're feeling a bit more relaxed now.")
    tts.say("Let me know if you'd like to continue.")

    posture.goToPosture("StandInit", 0.5)
    motion.rest()

if __name__ == "__main__":
    main()