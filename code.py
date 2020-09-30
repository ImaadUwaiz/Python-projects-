import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #to use voice frm system we use sapi5
voices = engine.getProperty('voices')
 #print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio): #takes a string and speak's
      engine.say(audio)
      engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir !" )

    elif hour>=12 and hour<17:
        speak("Good Afternoon sir! ")

    else:
        speak("Good evening sir! ")

    speak("I'm jarvis! please tell me how  may i help you!")

def takecommand():#it takes microphone input from the user and returns string output
    
     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("listning....")
        r.pause_threshold = 1
        audio = r.listen(source) #recoginse from speechrecognition

     try:
        print("recognising....")
        query = r.recognize_google(audio,language= 'en-in')
        print(f"user saide: {query}\n")

     except Exception as e:
        # print(e)
        print("say that again please....") 
        return "None" 
     return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail','yourpassword')
    server.sendmail('youremail', to , content)
    server.close()
if __name__ == "__main__":
    wishMe()
    #while True: #it wil keep on listning so use 
    if 1:
        query = takecommand().lower() #logic for  executing the task based on commad said
        
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia",'')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif  'open youtube' in query:
            webbrowser.open("youtube.com")
      
        elif  'open google' in query:
            webbrowser.open("google.com")
        
        elif  'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music ' in query:
            music_dir = 'paste the file link'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")

        elif 'open code' in query:
            codePath = "paste the file link"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("what should i say...")
                content = takecommand()
                to = "youremail"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry , im unable to send this email at the moment...please try again later")

          
