
from naoqi import ALProxy
import time

ROBOT_IP = "127.0.0.1"
PORT = 9559


def _listen_with_vocab(vocab, listen_seconds=5, confidence_thresh=0.40,
                       robot_ip=ROBOT_IP, port=PORT):
    
    """
    main idea:
    1. listens for a word in `vocab` for `listen_seconds`.
    2. returns the recognized word if confident, else doesn't and asks for user to repeat in main.
    """

    asr = ALProxy("ALSpeechRecognition", robot_ip, port)
    memory = ALProxy("ALMemory", robot_ip, port)

    # configure ASR
    asr.pause(True)
    asr.setLanguage("English")
    asr.setVocabulary(vocab, False)  # exact matches only
    asr.pause(False)

    # listens for user
    asr.subscribe("SAR_ASR")
    time.sleep(listen_seconds)

    # reads result
    data = memory.getData("WordRecognized")

    # cleanup & end ASR
    try:
        asr.unsubscribe("SAR_ASR")
    except:
        pass

    # validation: confidence threshold - if < thresh % confident ask user to repeat
    # themselves
    if not data or len(data) < 2:
        return "none"

    word, confidence = data[0], data[1]

    if confidence < confidence_thresh:
        return "none"

    return word if word in vocab else "none" # ensures exact matches only

# 2 vocab lists to detect from - listens & waits for 5secs for user response
def listen_for_module_choice(robot_ip=ROBOT_IP, port=PORT):
    """
    returns: "breathing" | "break" | "affirmations" | "none"
    """
    vocab = ["breathing", "break", "affirmations"] # module options
    print("Listening for module choice:", vocab)
    return _listen_with_vocab(vocab, listen_seconds=5, robot_ip=robot_ip, port=port)


def listen_yes_no(robot_ip=ROBOT_IP, port=PORT):
    """
    returns: "yes" | "no" | "none"
    """
    vocab = ["yes", "no"] # feedback loop options
    print("Listening for yes/no:", vocab)
    return _listen_with_vocab(vocab, listen_seconds=5, robot_ip=robot_ip, port=port)
