import speech_recognition as sr
import pyttsx3
import openai
import sys

# 1. Initialize Engines
# Replace 'your-api-key-here' with your actual OpenAI API Key
openai.api_key = "Enter API KEY"
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def generate_response(text):
    """Dialogue Response Generation using OpenAI API """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"I encountered an error: {e}"

def speak(text):
    """Text-to-Speech Synthesis (."""
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()

def run_dialogue_system():
    print("--- Dialogue System Started (Say 'Exit the bot' to stop) ---")
    
    # Requirement 4: Loop allows system to listen again after responding
    while True:
        with sr.Microphone() as source:
            # Requirement 1: Listen to user's voice
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                # Requirement 2: Automatically stop when user stops speaking
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                # Speech to Text Conversion
                user_text = recognizer.recognize_google(audio)
                print(f"You: {user_text}")

                # Requirement 5: Specific keyword to terminate program
                if "exit the bot" in user_text.lower():
                    speak("Terminating the program. Goodbye!")
                    sys.exit()

                # Generate and deliver response
                bot_response = generate_response(user_text)
                speak(bot_response)

            except sr.WaitTimeoutError:
                continue # No speech detected, listen again
            except sr.UnknownValueError:
                print("Could not understand audio, please try again.")
                continue
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    run_dialogue_system()