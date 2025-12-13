from naoqi import ALProxy
import time

ROBOT_IP = "127.0.0.1"
PORT = 9559


def _listen_with_vocab(vocab, listen_seconds=5, confidence_thresh=0.40,
                       robot_ip=ROBOT_IP, port=PORT):
    """
    Internal helper:
    Listens for a word in `vocab` for `listen_seconds`.
    Returns the recognized word if confident, else "none".
    """
    asr = ALProxy("ALSpeechRecognition", robot_ip, port)
    memory = ALProxy("ALMemory", robot_ip, port)

    # Configure ASR
    asr.pause(True)
    asr.setLanguage("English")
    asr.setVocabulary(vocab, False)  # exact matches only
    asr.pause(False)

    # Listen
    asr.subscribe("SAR_ASR")
    time.sleep(listen_seconds)

    # Read result
    data = memory.getData("WordRecognized")

    # Cleanup
    try:
        asr.unsubscribe("SAR_ASR")
    except:
        pass

    # Validate
    if not data or len(data) < 2:
        return "none"

    word, confidence = data[0], data[1]

    if confidence < confidence_thresh:
        return "none"

    return word if word in vocab else "none"


def listen_for_module_choice(robot_ip=ROBOT_IP, port=PORT):
    """
    Returns: "breathing" | "break" | "affirmations" | "none"
    """
    vocab = ["breathing", "break", "affirmations"]
    print("Listening for module choice:", vocab)
    return _listen_with_vocab(vocab, listen_seconds=5, robot_ip=robot_ip, port=port)


def listen_yes_no(robot_ip=ROBOT_IP, port=PORT):
    """
    Returns: "yes" | "no" | "none"
    """
    vocab = ["yes", "no"]
    print("Listening for yes/no:", vocab)
    return _listen_with_vocab(vocab, listen_seconds=4, robot_ip=robot_ip, port=port)
