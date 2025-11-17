
from naoqi import ALProxy
import time

ROBOT_IP = "127.0.0.1" # choregraphe simulation ip
PORT = 9559

def main():
    tts     = ALProxy("ALTextToSpeech", ROBOT_IP, PORT)
    motion  = ALProxy("ALMotion", ROBOT_IP, PORT)
    posture = ALProxy("ALRobotPosture", ROBOT_IP, PORT)
    leds    = ALProxy("ALLeds", ROBOT_IP, PORT)

    # wake robot & move into stable standing pose
    motion.wakeUp()
    posture.goToPosture("StandInit", 0.5)

    tts.say("Let's take a few calming breaths together.")

    
    #   3 FULL BREATHING CYCLES (4-7-8 breathing)
    for cycle in range(3):

        # ------------------------
        # INHALE (4 secs)
        # ------------------------
        tts.say("Take a slow breath in...")
        leds.fadeRGB("FaceLeds", 0xFFF5CC, 1.0)   # warm glow during inhale for calming effect

        # gentle upward shoulder movement + slight head lift to imitate breathing movement
        motion.angleInterpolation(
            ["LShoulderPitch", "RShoulderPitch", "HeadPitch"],
            [[1.0], [1.0], [-0.10]],   
            [[4.0], [4.0], [4.0]],
            True
        )

        motion.openHand("LHand")
        motion.openHand("RHand")

        # ------------------------
        # HOLD (7 seconds)
        # ------------------------
        tts.say("Hold it there... nice and steady...")
        leds.fadeRGB("FaceLeds", 0xFFFFCC, 1.0) # slightly brighter

        time.sleep(7)

        # ------------------------
        # EXHALE (8 seconds)
        # ------------------------
        tts.say("And now slowly exhale... let your shoulders relax...")
        leds.fadeRGB("FaceLeds", 0xFFEEDD, 1.5) # warm fade-out

        # shoulders lower + head returns slightly downward
        motion.angleInterpolation(
            ["LShoulderPitch", "RShoulderPitch", "HeadPitch"],
            [[1.40], [1.40], [0.15]],  # relaxed downward
            [[8.0], [8.0], [8.0]],
            True
        )

        motion.closeHand("LHand")
        motion.closeHand("RHand")

    
    #   IDLE POSE (STILL)
    tts.say("Let's stay here for a moment.")

    leds.fadeRGB("FaceLeds", 0xFFF2CC, 1.0)   # soft yellow calming tone to match

    # simple relaxed pose to finish the exercise
    motion.angleInterpolation(
        ["HeadPitch", "HeadYaw",
         "LShoulderPitch", "RShoulderPitch",
         "LShoulderRoll", "RShoulderRoll"],

        [[0.15], [0.0],
         [1.45], [1.45],
         [0.10], [-0.10]],

        [[1.5], [1.5],
         [2.0], [2.0],
         [2.0], [2.0]],

        True
    )

    motion.openHand("LHand")
    motion.openHand("RHand")

    time.sleep(2) # small hold before resetting

    # -----------------------------------------
    #   FINISH
    # -----------------------------------------
    tts.say("Good job. I hope you feel a bit more at ease.")

    # reset to default 
    posture.goToPosture("StandInit", 0.5)
    motion.rest()


if __name__ == "__main__":
    main()
