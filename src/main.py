
from naoqi import ALProxy
import time

# import local modules
import breathing_module  
# import affirmation_module   
# import break_module         
import speech_recognition_controller as speech

ROBOT_IP = "127.0.0.1" # choregraphe simulation ip
PORT = 9559

def main():
    # proxies
    tts     = ALProxy("ALTextToSpeech", ROBOT_IP, PORT)
    motion  = ALProxy("ALMotion", ROBOT_IP, PORT)
    posture = ALProxy("ALRobotPosture", ROBOT_IP, PORT)

    # wake up & greet user
    motion.wakeUp()
    posture.goToPosture("StandInit", 0.5)

    tts.say("Hi there! How can I help you today?You’re welcome to choose a breathing exercise, " \
    "a calm break, or some words of affirmations — whichever you prefer.")

    # speech recognition runs
    user_choice = speech.listen_for_choice()
    print("Speech result:", user_choice)

    if user_choice == "none":
        tts.say("Hmm, I didn’t hear that clearly. Please try saying it again.")
        return

    # -------------------
    # MODULE ROUTING
    # -------------------
    if user_choice == "breathing":
        tts.say("Okay, let's take a moment to breathe together.")
        breathing_module.main()

    # elif user_choice == "break":
        # tts.say("Okay, let me play something calming for you.")
        # break_module.main()  

    # elif user_choice == "affirmations":
        # tts.say("Okay, let me share some positive words of affirmations with you.")
        # affirmation_module.main()

    else:
        tts.say("I'm glad you took a moment to relax today.")
        tts.say("If you need another short break later, I’ll be right here — but remember, " \
        "I’m only for light stress-relief and not a substitute for therapy or professional help")

    
    # finish
    posture.goToPosture("StandInit", 0.5)
    motion.rest()

if __name__ == "__main__":
    main()