import speech_recognition as sr


def speech():
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="eng-in")
            print(text)
        except:
            print("Could not understand audio")


if __name__ == "__main__":
    speech()
