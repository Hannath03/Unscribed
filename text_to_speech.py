import pyttsx3
def read_question(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate',50)
    engine.setProperty('volume',1)
