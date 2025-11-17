# nao-sar-mental-health
# NAO Socially Assistive Robotics (SAR) – Mental Health Interaction  
BME 3720 • Introduction to Assistive Robotics • Final Project  

---

## Project Overview

This project explores the use of **Socially Assistive Robots (SARs)** as supportive tools for individuals experiencing stress or mental-health–related challenges.  
Our system enables the NAO robot to provide short, calming interactions designed to help users regulate stress levels through:

- Guided breathing exercises  
- Positive affirmation delivery  
- Calm break activities  
- Simple supportive dialogue  

The goal is to demonstrate how SARs can contribute to emotional support through **non-clinical, low-intensity interactions**.

---

## ⚠️ Ethical Considerations & Disclaimer

This system is **not** a medical device.  
It **does not** diagnose, treat, prevent, or replace therapy for mental-health conditions.

It is intended for:
- Classroom learning  
- Demonstrating SAR concepts  
- Low-intensity stress-relief interactions only  

Users who require help with mental-health concerns should seek professional support.

---

## 🗂 Repository Structure

The system is **event-driven** and currently includes:

- `main.py` – main controller that greets the user and routes to each module  
- `breathing_module.py` – guided breathing exercise with gentle arm/head movements and LED cues  
- `speech_recognition_controller.py` – speech recognition front-end to choose between modules  
- `affirmation_module.py` – placeholder for teammate (positive affirmations)  
- `break_module.py` – placeholder for teammate (calm break / music)
