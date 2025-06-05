import os
import openai
import speech_recognition as sr
import pyttsx3

# Set up speech recognition and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
# try to set german voice
for voice in engine.getProperty('voices'):
    if 'de' in voice.languages or 'german' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
engine.setProperty('rate', 150)  # slower rate for clarity

# OpenAI API key should be placed in OPENAI_API_KEY environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

BENDER_PROMPT = (
    "Du bist Bender aus der Serie Futurama. Antworte auf deutsch in "
    "Benders sarkastischem und manchmal respektlosem Tonfall. "
    "Sprich wie ein Roboter." 
)


def listen():
    """Record audio from microphone and return the recognized text."""
    with sr.Microphone() as source:
        print("Sprich jetzt...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='de-DE')
        print(f"Du hast gesagt: {text}")
        return text
    except sr.UnknownValueError:
        print("Spracherkennung fehlgeschlagen")
    except sr.RequestError as e:
        print(f"Fehler bei der Anfrage: {e}")
    return None


def ask_openai(text):
    """Send the text to OpenAI and return the assistant response."""
    if not openai.api_key:
        raise RuntimeError("OPENAI_API_KEY nicht gesetzt")
    messages = [
        {"role": "system", "content": BENDER_PROMPT},
        {"role": "user", "content": text},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response['choices'][0]['message']['content']


def speak(text):
    """Speak the given text via TTS."""
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
        user_input = listen()
        if not user_input:
            continue
        reply = ask_openai(user_input)
        print(f"Bender: {reply}")
        speak(reply)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Beende Assistent...")

