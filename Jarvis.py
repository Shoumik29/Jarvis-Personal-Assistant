import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("Hello I am Jarvis. Please tell me how can i help you")


def Take_Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening.....")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Please, Say that again")
        return "None"
    return query


# def queryForReminder():
#     try:
#         f = open("JarvisReminder.txt", "r")
#         ls = f.readlines()
#         currentTime = datetime.datetime.now().strftime("%H%M")
#         print(currentTime)
#         for item in ls:
#             if currentTime in item:
#                 speak(f"Sir you had a reminder for {item}")
#     except Exception as e:
#         pass


if __name__ == '__main__':
    wish_me()
    while True:
        query = Take_Command().lower()
        #queryForReminder()

        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print("Jarvis:", results)
            speak(results)
        elif 'open movies' in query:
            path = "E:\\Movies"
            path = os.path.realpath(path)
            os.startfile(path)
            speak("Opening Movies Folder sir!")
        elif 'open youtube' in query:
            webbrowser.register('firefox', None,
                                webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
            webbrowser.get('firefox').open('youtube.com')
            speak("Opening Youtube sir!")
        elif 'open google' in query:
            webbrowser.register('firefox', None,
                                webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
            webbrowser.get('firefox').open('google.com')
            speak("Opening Google sir!")
        elif 'open stack overflow' in query:
            webbrowser.register('firefox', None,
                                webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
            webbrowser.get('firefox').open('stackoverflow.com')
            speak("Opening StackOverflow sir!")
        elif 'open facebook' in query:
            webbrowser.register('firefox', None,
                                webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
            webbrowser.get('firefox').open('facebook.com')
            speak("Opening Facebook sir!")
        elif 'open gmail' in query:
            webbrowser.register('firefox', None,
                                webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
            webbrowser.get('firefox').open('https://mail.google.com/mail/u/0/')
            speak("Opening Gmail sir!")
        elif 'search' in query:
            speak("What do you want to search?")
            searchQ = Take_Command().lower()
            webbrowser.register('firefox', None,
                                webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
            webbrowser.get('firefox').open(f'https://www.google.com.tr/search?q={searchQ}')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code blocks' in query:
            print("Opening Codeblocks....")
            codeBlocksPath = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(codeBlocksPath)
            speak("Opening CodeBlocks sir!")
        elif 'turn off' in query:
            speak("Good bye sir! I am quiting")
            break
        # elif 'set reminder' in query:
        #     speak("What do you want to be reminded for?")
        #     work = Take_Command()
        #     speak("When you want to be reminded?")
        #     workTime = Take_Command()
        #     f = open("JarvisReminder.txt", "a")
        #     f.write(f"{work} at {workTime}\n")
        #     speak(f"Your reminder for {work} has been set")
        #     f.close()

