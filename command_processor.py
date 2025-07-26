import subprocess
import webbrowser
import pyautogui
import os

def process_command(command):
    command = command.lower().strip()

    # === SYSTEM APP CONTROLS ===
    if "open chrome" in command:
        subprocess.Popen("start chrome", shell=True)

    elif "close chrome" in command or "close youtube" in command:
        subprocess.Popen("taskkill /f /im chrome.exe", shell=True)

    elif "open calculator" in command:
        subprocess.Popen("start calc", shell=True)

    elif "close calculator" in command:
        subprocess.Popen("taskkill /f /im calculator.exe", shell=True)

    elif "shutdown the system" in command:
        subprocess.Popen("shutdown /s /t 1", shell=True)

    elif "open notepad" in command:
        subprocess.Popen("start notepad", shell=True)

    elif "close notepad" in command:
        subprocess.Popen("taskkill /f /im notepad.exe", shell=True)

    elif "open file explorer" in command:
        subprocess.Popen("start explorer", shell=True)

    elif "open word" in command:
        subprocess.Popen("start winword", shell=True)

    elif "close word" in command:
        subprocess.Popen("taskkill /f /im winword.exe", shell=True)

    elif "open excel" in command:
        subprocess.Popen("start excel", shell=True)

    elif "close excel" in command:
        subprocess.Popen("taskkill /f /im excel.exe", shell=True)

    elif "open paint" in command:
        subprocess.Popen("start mspaint", shell=True)

    elif "close paint" in command:
        subprocess.Popen("taskkill /f /im mspaint.exe", shell=True)

    elif "open command prompt" in command or "open cmd" in command:
        subprocess.Popen("start cmd", shell=True)

    elif "open code" in command:
        subprocess.Popen("start code", shell=True)

    # === WhatsApp Desktop (via Shell AppsFolder) ===
    elif "open whatsapp" in command:
        try:
            subprocess.Popen("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", shell=True)
        except Exception as e:
            print("❌ Failed to open WhatsApp:", e)

    elif "close whatsapp" in command:
        subprocess.Popen("taskkill /f /im WhatsApp.exe", shell=True)

    # === Telegram Desktop ===
    elif "open telegram" in command:
        try:
            subprocess.Popen(r'"C:\Program Files\WindowsApps\TelegramMessengerLLP.TelegramDesktop_5.15.2.0_x64__t4vj0pshhgkwm\Telegram.exe"', shell=True)
        except Exception as e:
            print("❌ Failed to open Telegram:", e)

    elif "close telegram" in command:
        subprocess.Popen("taskkill /f /im Telegram.exe", shell=True)

    # === WEB SEARCH & SITES ===
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "search for" in command:
        query = command.replace("search for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # === MOUSE & KEYBOARD ACTIONS ===
    elif "scroll down" in command:
        pyautogui.scroll(-500)

    elif "scroll up" in command:
        pyautogui.scroll(500)

    elif "click" in command:
        pyautogui.click()

    elif "double click" in command:
        pyautogui.doubleClick()

    elif "press enter" in command:
        pyautogui.press("enter")

    elif command.startswith("type "):
        text = command.replace("type", "").strip()
        pyautogui.write(text)

    # === DEFAULT CASE ===
    else:
        print("🧠 Command not recognized.")
