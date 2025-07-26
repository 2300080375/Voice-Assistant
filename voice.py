import speech_recognition as sr
import pyttsx3
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Optional: Set volume and voice
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Try voices[1].id if voice not heard

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
        except sr.WaitTimeoutError:
            print("⏱️ No speech detected.")
            return ""
    try:
        print("🧠 Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command
    except sr.UnknownValueError:
        print("❌ Couldn’t understand.")
        return ""
    except sr.RequestError:
        print("⚠️ Network issue.")
        return ""

def speak(text):
    print(f"🤖 Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)  # Let the system play it fully befor3r 1cxe continuing