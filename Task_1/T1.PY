import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)
        
    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        
    except:
        speak("Sorry, I didn't understand")
        return ""
        
    return command


# Start Assistant
speak("Hello, I am your voice assistant")

while True:
    
    command = take_command()
    
    # Hello
    if "hello" in command:
        speak("Hello, how can I help you")
    
    
    # Time
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + time)
    
    
    # Date
    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)
    
    
    # Wikipedia Search
    elif "who is" in command or "what is" in command:
        speak("Searching Wikipedia")
        try:
            result = wikipedia.summary(command, sentences=2)
            speak(result)
        except:
            speak("Sorry, I could not find information")
    
    
    # Google Search
    elif "search" in command:
        speak("Searching Google")
        pywhatkit.search(command)
    
    
    # Exit
    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        break
    
    
    else:
        speak("Please say command again")