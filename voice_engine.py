import speech_recognition as sr
import pyttsx3
import pyaudio
# 1. Set up the Speaker ( pyttsx3 )
engine = pyttsx3.init()


def speak(text):
    """Reads text aloud"""
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listens to microphone and returns text"""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Ask your question now.")

        try:
            # Capture the audio
            audio = recognizer.listen(source, timeout=5)

            # Convert Audio to Text (using Google API)
            # Note: You need internet for this
            text = recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text

        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""