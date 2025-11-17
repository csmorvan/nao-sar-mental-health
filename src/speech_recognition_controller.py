
from naoqi import ALProxy
import time

ROBOT_IP = "127.0.0.1"
PORT = 9559

def listen_for_choice():
    asr = ALProxy("ALSpeechRecognition", ROBOT_IP, PORT)
    memory = ALProxy("ALMemory", ROBOT_IP, PORT)

    vocab = ["breathing", "break", "affirmations"] # list of exact words to recognize

    asr.pause(True)
    asr.setLanguage("English")
    asr.setVocabulary(vocab, False) # pull words from vocab list, exact matches only
    asr.pause(False) # recogtion following settings set

    asr.subscribe("SAR_ASR")
    print("Listening... please choose from: breathing, break, or affirmations.")
    time.sleep(5) # listen for 5s

    # get result from speech
    data = memory.getData("WordRecognized")
    asr.unsubscribe("SAR_ASR")

    # if nothing is heard or incomplete data
    if not data or len(data) < 2:
        return "none"
    
    word = data[0]
    confidence = data[1]

    if confidence < 0.40: # if NAO < 40% sure assume it didn't hear the person properly
        return "none"
    
    if word in vocab: # word is the exact one from vocab list
        return word
    
    return "none" # for when word wasn't on vocab list