import time
import speech_recognition as sr

from voice import listen, speak
from command_processor import process_command

recognizer = sr.Recognizer()

speak("Voice assistant is ready. Say 'hey rio' before your command.")

while True:
    try:
        command = listen()
        if command:
            command = command.lower().strip()
            print(f"🎙️ Heard: {command}")

            if any(word in command for word in ["exit", "quit", "stop"]):
                speak("Goodbye!")
                break

            # === Exact wake word ===
            if command == "hey rio":
                speak("Yeah, please tell me")
                time.sleep(1.2)  # 🔄 wait to let TTS fully complete

                next_command = listen()
                if next_command:
                    process_command(next_command.lower().strip())
                else:
                    speak("I didn't catch that. Please try again.")

            # === Wake word + command in one sentence ===
            elif command.startswith("hey rio"):
                speak("Yeah, please tell me")
                time.sleep(1.2)  # 🔄 give time for TTS
                actual_command = command.replace("hey rio", "", 1).strip()
                if actual_command:
                    process_command(actual_command)
                else:
                    speak("Please say the command after 'hey rio'.")

            else:
                print("💤 Wake word not detected. Ignoring...")

    except Exception as e:
        print(f"⚠️ Error: {e}")
        speak("Something went wrong. Restarting.")
