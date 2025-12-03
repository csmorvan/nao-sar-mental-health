#class AffirmationModule:
    #def onInput_start(self):
        #self.onDone()


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

def main():
    """
    Speaks a randomly selected positive affirmation from a preset list.
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

    tts.say("Here is a positive message for you.")
    tts.say(random.choice(affirmations))

if __name__ == "__main__":
    main()