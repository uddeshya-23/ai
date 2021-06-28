import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)



def date():
    year = int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

            
  
def wishme():
   #speak("welcome back uddeshya sir")
   #time()
   #date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("GOOD MORNING")
    elif hour >= 12 and hour < 18:
        speak("GOOD afternoon")
    elif hour >= 18 and hour < 24:
        speak("GOOD evening")
    else:
        speak("GOOD NIGHT")
  
  
    speak("hello mr. UDDDESHHYA WHAT CAN I DO FOR YOU")

def takeCommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("listening...")
       r.pause_threshold = 1
       audio = r.listen(source)

   try:
       print("Recognition")
       query = r.recognize_google(audio,language = "en-US")
       print(query)

   except Exception as e:
       print(e)
       speak("say that again..")

       return "None"
   return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com", "123test")
    server.sendmail("uddeshya350q@gmail.com",to, content)
    server.closes

def screenshot():
    img = pyautogui.screenshot()
    img.save("F:\ss\img{}.jpg")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent )

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "offline" in query:
            quit()

        elif "wikipedia" in query:
             speak("SEARCHING....")
             query = query.replace("wikipedia", "")
             result = wikipedia.summary(query, sentences = 2)
             speak(result)

        elif("send mail") in query:
           try:
                speak("what should i say?")
                content = takeCommand()
                to =("text@gmail.com")
                sendmail(to, content)
                speak("Email sent successfully")

           except Exception as e:
                speak(e)
                speak ("unable to send")
        elif"search in chrome"in query:
            speak("what should i search")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome_proxy.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "logout" in query:
            os.system("shutdown - 1")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            songs_dir ="F:\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[1]))

        elif "remember that" in query:
            speak("what should i need to know about you uddeshya sir")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "tell me about sir" in query:
            remember = open("data.txt","r")
            speak("hey" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()
