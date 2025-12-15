from naoqi import ALProxy
import time

ROBOT_IP = "127.0.0.1"   # Choregraphe simulation IP
PORT = 9559


def main():
    #proxies
    tts     = ALProxy("ALTextToSpeech", ROBOT_IP, PORT)
    motion  = ALProxy("ALMotion", ROBOT_IP, PORT)
    posture = ALProxy("ALRobotPosture", ROBOT_IP, PORT)

    try:
        leds = ALProxy("ALLeds", ROBOT_IP, PORT)
    except:
        leds = None

    #wake up & greet user
    motion.wakeUp()
    posture.goToPosture("StandInit", 0.5)

    tts.say("Hi there! How can I help you today?")
    time.sleep(1.0)

    # DEMO PLACEHOLDER:
    # this interaction would now transition into speech recognition and module 
    # selection logic.
    tts.say(
        "In this demonstration, I will show how the interaction flows, "
        "without listening for speech input."
    )
    time.sleep(1.5)

    #module selection
    tts.say(
        "Would you like to do a breathing exercise, "
        "take a calm break, or hear some positive affirmations?"
    )
    time.sleep(2.0)

    # DEMO PLACEHOLDER:
    # user's spoken response would be processed here to determine which module 
    # is launched.
    tts.say(
        "Normally, I would listen for your response and guide you into one of these activities."
    )
    time.sleep(1.5)

    # breathing module
    tts.say("Okay, let's take a moment to breathe together.")
    time.sleep(2.5)

    # DEMO PLACEHOLDER:
    tts.say(
        "Here, a guided breathing exercise would begin, ")
    time.sleep(0.5)
    tts.say(
        "helping you slow your breathing and focus on the present moment."
    )
    time.sleep(2.0)

   # break module
    tts.say("Okay. Let's take a calm break together.")
    time.sleep(1.5)

    # DEMO PLACEHOLDER:
    tts.say(
        "During this calm break, soft and calming background music would begin to play."
    )
    time.sleep(1.5)

    tts.say(
        "I would encourage you to sit comfortably, relax your shoulders, "
        "and take this moment to rest."
    )
    time.sleep(8.0)

    # DEMO PLACEHOLDER

    # affirmation module
    tts.say("Okay, let me share some positive words of affirmations with you.")
    time.sleep(2.0)

    # DEMO PLACEHOLDER:
    # positive words of affirmations would be spoken here, randomized from a 
    # predefined list.
    tts.say(
        "Positive affirmations are used to promote reassurance, confidence, "
        "and emotional grounding."
    )
    time.sleep(2.0)

    # feedback
    tts.say("Good job. You're doing great taking care of yourself.")
    time.sleep(1.5)

    tts.say("Would you like to try another module? Please say yes or no.")
    time.sleep(2.0)

    # DEMO PLACEHOLDER:
    tts.say(
        "In the full system, your response would determine whether another " \
        "activity begins."
    )
    time.sleep(1.5)

    # closure
    tts.say(
        "I'm glad you decided to take this moment to relax. "
    ) 
    time.sleep(1.0)
    tts.say(
        "If you need another short break later, I'll be right here - but remember, "
        )
    time.sleep(0.5)
    tts.say(
        "I'm only for light stress relief and not a substitute for therapy or professional help."
    )
    
    time.sleep(2.0)

    # end interaction
    posture.goToPosture("StandInit", 0.5)
    motion.rest()


if __name__ == "__main__":
    main()
