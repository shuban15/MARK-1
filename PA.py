import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine.say("good morning sir")
        engine.runAndWait()
    elif hour>=12 and hour<16:
        engine.say("good afternoon sir")
        engine.runAndWait()
    elif hour>=16 and hour<20:
        engine.say("good evening sir")
        engine.runAndWait()
    else:
        engine.say("good night sir")
        engine.runAndWait()

if __name__=="__main__":
    wishme()
    engine.say("i am jarvis how can i help you")
    engine.runAndWait()
