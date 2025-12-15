from naoqi import ALProxy
import time

# import local modules
import breathing_module  
import affirmation_module   
import break_module         
import speech_recognition_controller as speech

ROBOT_IP = "127.0.0.1"  # choregraphe simulation ip
PORT = 9559


def main():
    # proxies
    tts     = ALProxy("ALTextToSpeech", ROBOT_IP, PORT)
    motion  = ALProxy("ALMotion", ROBOT_IP, PORT)
    posture = ALProxy("ALRobotPosture", ROBOT_IP, PORT)

    try:
        leds = ALProxy("ALLeds", ROBOT_IP, PORT)
    except:
        leds = None

    # wake up & greet user
    motion.wakeUp()
    posture.goToPosture("StandInit", 0.5)

    tts.say("Hi there! How can I help you today?")

    # ---------------------
    # FEEDBACK LOOP START
    # ---------------------
    while True:

        tts.say(
            "Would you like to do a breathing exercise, "
            "take a calm break, or hear some positive affirmations?"
        )

        # speech recognition runs (MODULE CHOICE)
        user_choice = speech.listen_for_module_choice(ROBOT_IP, PORT)
        print("User choice:", user_choice)

        # if nothing or unclear input
        if user_choice == "none":
            tts.say("Hmm, I didn’t hear that clearly. Please try saying it again.")
            continue

        # -------------------
        # MODULE ROUTING
        # -------------------
        if user_choice == "breathing":
            tts.say("Okay, let's take a moment to breathe together.")
            breathing_module.main()

        elif user_choice == "break":
            tts.say("Okay. Let's take a calm break together.")
            break_module.break_module(
                break_module.tts,
                break_module.posture,
                break_module.audio,
                leds=leds
            )

        elif user_choice == "affirmations":
            tts.say("Okay, let me share some positive words of affirmations with you.")
            affirmation_module.main()

        else:
            tts.say("That's okay. Let's take a moment to pause.")

        # -----------------------
        # FEEDBACK AFTER MODULE
        # -----------------------
        tts.say("Good job. You're doing great taking care of yourself.")
        tts.say("Would you like to try another module? Please say yes or no.")

        # speech recognition runs (YES / NO)
        continue_choice = speech.listen_yes_no(ROBOT_IP, PORT)
        print("Continue choice:", continue_choice)

        # if user does NOT say yes, exit loop
        if continue_choice != "yes":
            tts.say(
                "I'm glad you decided to take this moment to relax. "
                "If you need another short break later, I'll be right here - but remember, "
                "I'm only for light stress-relief and not a substitute for therapy or professional help."
            )
            break

    # finish
    posture.goToPosture("StandInit", 0.5)
    motion.rest()


if __name__ == "__main__":
    main()
