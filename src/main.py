
from naoqi import ALProxy
import time

# import local modules
import breathing_module  
# import affirmation_module   
# import break_module         
# import speech_recognition_controller as speech

ROBOT_IP = "127.0.0.1" # choregraphe simulation ip
PORT = 9559

def main():
    # proxies
    tts     = ALProxy("ALTextToSpeech", ROBOT_IP, PORT)
    motion  = ALProxy("ALMotion", ROBOT_IP, PORT)
    posture = ALProxy("ALRobotPosture", ROBOT_IP, PORT)

    # wake up & greetings
    motion.wakeUp()
    posture.goToPosture("StandInit", 0.5)

    tts.say("Hi there! How can I help you today? You may select from the following " \
    "options: breathing exercises, a calm break, or affirmations")
    time.sleep(1.0)

    # speech recognition
    user_choice = speech.listen_for_choice()
    print("Speech result:", user_choice)

    if user_choice == "none":
        tts.say("Hmm, I didn’t hear that clearly. Please try saying it again.")
        user_choice = get_user_choice_backup()

    # -----------------------------
    # MODULE ROUTING
    # -----------------------------
    if user_choice == "breathing":
        tts.say("Okay, let's take a moment to breathe together.")
        breathing_module.main()

    elif user_choice == "break":
        tts.say("Okay, let me play something calming for you.")
        break_module.main()  

    elif user_choice == "affirmations":
        tts.say("Okay, let me share some positive words of affirmations with you.")
        affirmation_module.main()

    else:
        tts.say("I'm glad you took a moment to relax today.")
        tts.say("Remember, I'm here for short breaks, but not for therapy purposes.")

    
    # finish
    posture.goToPosture("StandInit", 0.5)
    motion.rest()

if __name__ == "__main__":
    main()