

Alex - Speech Assistant App

Alex is a Python-based speech assistant that can perform tasks like searching the web, finding locations, telling the time, and more. It uses **Speech Recognition** for voice input and **Text-to-Speech (gTTS)** for voice output.

---

## **Features**
- **Voice Commands**: Interact with Alex using natural language.
- **Web Search**: Search Google directly by voice.
- **Location Finder**: Find locations using Google Maps.
- **Time Check**: Ask for the current time.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## **Technologies Used**
- **Speech Recognition**: `speech_recognition` library for converting speech to text.
- **Text-to-Speech**: `gTTS` (Google Text-to-Speech) for converting text to speech.
- **Audio Playback**: `pydub` for playing audio files.
- **Web Interaction**: `webbrowser` for opening URLs.

---

## **Installation**

### **Prerequisites**
1. **Python 3.8 or higher**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **FFmpeg** (for `pydub`): Install FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).


Speak to Alex after hearing the prompt: **"How can I help you?"**

### **Available Commands**
- **"What is your name?"**: Alex introduces itself.
- **"What time is it?"**: Alex tells you the current time.
- **"Search for [query]"**: Alex searches Google for your query.
- **"Find location [place]"**: Alex opens Google Maps for the specified location.
- **"Exit"**: Alex says goodbye and closes the application.

