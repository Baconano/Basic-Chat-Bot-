# Homework 12: Real-Time Dialogue System

## Project Overview
This project is a real-time conversational robot developed for the CSE 4392/5369 Natural Language Processing course at the University of Texas at Arlington. It implements a complete "Listen-Respond-Listen" loop, functioning similarly to a virtual assistant like Siri or Google Assistant.

## Technical Architecture
The system is built on three core NLP pillars:
1. **Speech-to-Text (ASR)**: Uses the `SpeechRecognition` library to capture live audio and convert it to text.
2. **Dialogue Generation**: Utilizes the OpenAI GPT-3.5 API to generate intelligent, context-aware responses.
3. **Text-to-Speech (TTS)**: Uses `pyttsx3` to synthesize and play the generated response back to the user in real-time.

## Requirements & Compliance
As per the assignment guidelines, the system performs the following:
* **Requirement 1 & 2**: Listens to the user's voice and automatically stops when the user finishes speaking.
* **Requirement 3**: Generates a real-time response in the form of audio.
* **Requirement 4**: Automatically returns to the listening state after the response is delivered.
* **Requirement 5**: Terminates the program immediately if the keyword **"Exit the bot"** is detected.

## Setup and Installation
Ensure you are in your Python environment and run:

```bash
pip install speechrecognition pyttsx3 openai==0.28 pyaudio
