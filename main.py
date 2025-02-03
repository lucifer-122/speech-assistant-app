import speech_recognition as sr
import webbrowser
import time
import playsound
import pydub
from pydub.playback import play
import os
import random
from gtts import gTTS
from time import ctime


r = sr.Recognizer()

def record_audio( ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            speak(voice_data)
        except sr.UnknownValueError:
            speak("Sorry, I did not get that")
        except sr.RequestError:
            speak("Sorry, my speech service is down")
        return voice_data
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
 
    
def response(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Alex')
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('searching for', search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of', location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)

speak('how can I help you?')
while 1:      
    voice_data = record_audio()
    response(voice_data)