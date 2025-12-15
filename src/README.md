README.txt – NAO-Based Mental Health Support System

====================================================



This README explains:

1\) Required libraries and setup

2\) Important simulator limitations

3\) How to run the provided code files



--------------------------------------------------

1\. Requirements and Installation 

(Nothing new, only libraries used throughout 

the course)

--------------------------------------------------



Hardware/Software:

• NAO robot OR Choregraphe simulator

• NAOqi Python SDK

• Anaconda3 prompt

• Python environment compatible with NAOqi



Required Python Libraries:

• naoqi (provided by the NAOqi SDK)

• time (standard library)

• random (standard library)



--------------------------------------------------

2\. Important Simulation Limitations (Choregraphe)

--------------------------------------------------



When using Choregraphe simulation:

• ALSpeechRecognition cannot be tested

• Module routing based on speech cannot be tested

• LED transitions (ALLeds) may not render correctly

• Audio playback (ALAudioPlayer) runs silently



Because of these limitations:

• Only individual modules were tested in simulation

• Integrated interaction flow is intended for validation

&nbsp; on a physical NAO robot



--------------------------------------------------

3\. Code Files Overview

--------------------------------------------------



main.py

• Main controller script

• Greets the user and routes between modules using speech input

• Requires working speech recognition 



speech\_recognition\_controller.py

• Handles keyword-based speech recognition

• Uses restricted vocabularies and confidence thresholding

• Default confidence threshold: 0.40 (40%)



breathing\_module.py

• Guided 4-7-8 breathing exercise

• Uses speech, motion, and LED cues

• Can be run independently in simulation



break\_module.py

• Calm break module

• Moves robot to SitRelax posture

• Uses brief verbal prompts and optional calming audio

• Audio file must be uploaded manually to the robot



break\_module\_choregraphe\_tester.py

• Simulator-friendly calm break demo

• Audio playback disabled

• Uses timed wait instead of music

• Recommended for Choregraphe video recording



affirmation\_module.py

• Randomized positive affirmation messages

• Minimal interaction required



--------------------------------------------------

4\. How to Run the Code

--------------------------------------------------



A. Running Individual Modules (Recommended for Simulation)



These commands work best in Choregraphe/Tester:



&nbsp; python breathing\_module.py

&nbsp; python break\_module\_choregraphe\_tester.py

&nbsp; python affirmation\_module.py



B. Running the Full System (Physical Robot Required)



The main controller requires working speech recognition:



&nbsp; python main.py



--------------------------------------------------

5\. Audio Setup (Physical Robot Only)

--------------------------------------------------



The calm break module attempts to play an audio file from:



&nbsp; /home/nao/rose\_water.wav



Steps:

1\) Download the audio file

2\) Upload it to the robot using SCP:

&nbsp;  scp "rose\_water.wav" nao@<ROBOT\_IP>:/home/nao/

3\) Confirm the file path matches the one in break\_module.py



Audio source (copyright-free, per creator):

https://www.youtube.com/watch?v=xakBzg5atsM





