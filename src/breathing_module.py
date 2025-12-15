
from naoqi import ALProxy
import time

# ROBOT_IP = "127.0.0.1" # simulation ip
ROBOT_IP = "192.168.4.22"
PORT = 9559

def main():
    # proxies needed
    tts     = ALProxy("ALTextToSpeech", ROBOT_IP, PORT)
    motion  = ALProxy("ALMotion", ROBOT_IP, PORT)
    posture = ALProxy("ALRobotPosture", ROBOT_IP, PORT)
    leds    = ALProxy("ALLeds", ROBOT_IP, PORT)

    # wake robot & move into standing pose
    motion.wakeUp()
    posture.goToPosture("StandInit", 0.5)

    tts.say("Let's take a few calming breaths together.")

    
    # loop for 3 full breathing cycles (4-7-8 breathing)
    for cycle in range(3):
        
        # INHALE (4 secs)
        tts.say("Take a slow breath in...")
        leds.fadeRGB("FaceLeds", 0xFFF5CC, 1.0)  # fades all face LEDs to warm glow during inhale for calming effect 

        # gentle upward shoulder movement & slight head lift to mimic breathing 
        motion.angleInterpolation(
            ["LShoulderPitch", "RShoulderPitch", "HeadPitch"],
            [[1.0], [1.0], [-0.10]],   
            [[4.0], [4.0], [4.0]],
            True
        )

        motion.openHand("LHand")
        motion.openHand("RHand")

        # HOLD (7 seconds)
        tts.say("Hold it there... nice and steady...")
        leds.fadeRGB("FaceLeds", 0xFFFFCC, 1.0) #  increase brightness during the breath-holds

        time.sleep(7)

        
        # EXHALE (8 seconds)
        tts.say("And now slowly exhale... let your shoulders relax...")
        leds.fadeRGB("FaceLeds", 0xFFEEDD, 1.5) # soft warm fade-out to release air/breathe out

        # shoulders lower & head returns slightly downward to mimic exhale
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

    leds.fadeRGB("FaceLeds", 0xFFF2CC, 1.0)   # soft neutral yellow calming tone to match

    # simple relaxed pose to finish the exercise

    # listing all movements from this module to follow
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

    
    #   FINISH!
    tts.say("Good job. I hope you feel a bit more at ease.")

    # reset to default 
    posture.goToPosture("StandInit", 0.5)
    motion.rest()


if __name__ == "__main__":
    main()
