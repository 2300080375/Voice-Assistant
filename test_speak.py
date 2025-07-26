import pyttsx3

engine = pyttsx3.init()

engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')

# Try voice[0] and voice[1] depending on your system
engine.setProperty('voice', voices[0].id)

print("🔊 Testing speech...")
engine.say("Yeah, tell me")
engine.runAndWait()
