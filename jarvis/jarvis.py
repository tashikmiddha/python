import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import random
import smtplib
import qrcode as qr
import pyjokes

engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-50)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("good morning")
    elif(hour>=12 and hour<18):
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir,please tell me how may i help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.adjust_for_ambient_noise(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,Language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please....")
        return "None"
    return query

def sendemail(to ,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email','your password')
    server.sendmail('your email',to ,content)
    server.close()
    
if __name__=="__main__":
    
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'play music' in query:
            music_dir="C:\\user\\tashi\\music"
            songs=os.listdir(music_dir)
            print(songs)
            l=random.randrange(0,len(songs-1))
            os.startfile(os.path.join(music_dir,songs[l]))
        
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir ,the time is {strtime}")
         
        elif 'open code' in query:
            codepath="C:\\Users\\tashi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)
            
        elif 'open virtual box' in query:
            codepath="C:\\Users\\tashi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Oracle VM VirtualBox"
            os.startfile(codepath)
        elif 'email to tashik ' in query:
            try:
                speak("what should i say?")
                content=takecommand()
                to="tashik@gmail.com"
                sendemail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry,i am not able to send this email")     
        
        elif 'make qr of youtube' in query:
            img=qr.make("youtube.com")
            img.save("image.png")
            speak("qr is generated and saved in a _pycache_ folder")
        
        
        elif 'exit jarvis' in query :
            speak("exiting the jarvis")
            exit() 
        
         
                
                