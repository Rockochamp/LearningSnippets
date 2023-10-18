import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def print_available_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print("Voice ID:", voice.id)
        print("Name:", voice.name)
        print("Languages:", voice.languages)
        print("Gender:", voice.gender)
        print("Age:", voice.age)
        print("")

def main():
    print_available_voices()
    text = "Hello, this is a demonstration of text-to-speech using pyttsx3."
    text_to_speech(text)

if __name__ == "__main__":
    main()