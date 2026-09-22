import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

    import speech_recognition as sr

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        text = r.recognize_google(audio)
        text = text.lower()

        print("You said:", text)

        if "vennela" in text:
            print("Yes Sir, how can I help?")

        if "stop" in text:
            print("Goodbye Sir")
            break

    except Exception as e:
        print(f"Error: {e}")