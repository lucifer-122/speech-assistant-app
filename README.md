

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

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/speech-assistant-app.git
   cd speech-assistant-app
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## **Usage**
1. Start the application:
   ```bash
   python main.py
   ```

2. Speak to Alex after hearing the prompt: **"How can I help you?"**

### **Available Commands**
- **"What is your name?"**: Alex introduces itself.
- **"What time is it?"**: Alex tells you the current time.
- **"Search for [query]"**: Alex searches Google for your query.
- **"Find location [place]"**: Alex opens Google Maps for the specified location.
- **"Exit"**: Alex says goodbye and closes the application.

---

## **Code Structure**
- **`main.py`**: The main script containing the logic for the speech assistant.
- **`requirements.txt`**: Lists all dependencies for the project.
- **`README.md`**: This file, providing an overview of the project.

---

## **Contributing**
Contributions are welcome! If you'd like to improve Alex, follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- **Google Speech Recognition**: For speech-to-text functionality.
- **gTTS**: For text-to-speech conversion.
- **pydub**: For audio playback.

---

## **Contact**
For questions or feedback, feel free to reach out:
- **Your Name**: [Your Email](mailto:your-email@example.com)
- **GitHub**: [your-username](https://github.com/your-username)

---

Enjoy using Alex! 🚀

---

### **Screenshots (Optional)**
You can add screenshots of your app in action to make the README more engaging. For example:
```markdown
![Alex in Action](screenshots/alex-demo.png)
```

---

Let me know if you need further assistance! 😊
