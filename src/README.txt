README.txt – NAO-Based Mental Health Support System
====================================================

--------------------------------------------------
1. Important Simulation Limitations (Choregraphe)
--------------------------------------------------

When using the Choregraphe simulation:
• ALSpeechRecognition cannot be tested
• Module routing based on speech cannot be tested
• LED transitions (ALLeds) may not render correctly
• Audio playback (ALAudioPlayer) runs silently

Because of these limitations:
• Only individual modules were tested in simulation
• Integrated interaction flow is intended for validation
  on a physical NAO robot

--------------------------------------------------
2. Code Files Overview
--------------------------------------------------

main.py
• Main controller script
• Greets the user and routes between modules using speech input
• Requires working speech recognition 

speech_recognition_controller.py
• Handles keyword-based speech recognition
• Uses restricted vocabularies and confidence thresholding
• Default confidence threshold: 0.40 (40%)

breathing_module.py
• Guided 4-7-8 breathing exercise
• Uses speech, motion, and LED cues
• Can be run independently in simulation

break_module.py
• Calm break module
• Moves robot to SitRelax posture
• Uses brief verbal prompts and optional calming audio
• Audio file must be uploaded manually to the robot

break_module_choregraphe_tester.py
• Simulator-friendly calm break demo
• Audio playback disabled
• Uses timed wait instead of music
• Used use: Choregraphe video recording

affirmation_module.py
• Randomized positive affirmation messages
• Minimal interaction required

--------------------------------------------------
3. How to Run the Code
--------------------------------------------------

A. Individual Modules (for Simulation)

  python breathing_module.py
  python break_module_choregraphe_tester.py
  python affirmation_module.py

B. Full System (for NAO)

The main controller requires working speech recognition:

  python main.py

--------------------------------------------------
4. Audio Setup (for NAO Only)
--------------------------------------------------

The calm break module attempts to play an audio file from:

  /home/nao/rose_water.wav

Steps:
1) Download the audio file
2) Upload it to the robot using SCP:
   scp "rose water.wav" nao@<ROBOT_IP>:/home/nao/
3) Confirm the file path matches the one in break_module.py

Audio source (copyright-free, per creator):
https://www.youtube.com/watch?v=xakBzg5atsM

