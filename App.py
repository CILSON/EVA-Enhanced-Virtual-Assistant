# import pyaudio
import speech_recognition as sr
import time
import pyttsx3 
import pyautogui 
import keyboard 

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()    

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # 👈 Slower speaking rate

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        
def open_app(app_name):
    speak(f"Opening {app_name}")
    keyboard.press("windows")
    time.sleep(0.2)
    keyboard.release("windows")
    time.sleep(0.5) 
    pyautogui.write(app_name, interval=0.05)  # 👈 Slower typing speed
    time.sleep(0.5)
    keyboard.press("enter")
    keyboard.release("enter")

def main():
    speak("Which app should I open?")
    app = listen_command()
    if app:
        open_app(app)

if __name__ == "__main__":
    main()