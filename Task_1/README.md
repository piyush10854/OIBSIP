# Voice Assistant using Python (Beginner Project)

## Objective

The objective of this project is to build a basic voice assistant using Python that can understand simple voice commands and respond accordingly. This project helps beginners learn speech recognition, text-to-speech conversion, and basic task automation.

---

## Tools & Technologies Used

* **Python**
* **SpeechRecognition** (for voice input)
* **pyttsx3** (for text-to-speech output)
* **datetime** (for time and date)
* **Wikipedia** (for fetching information)
* **pywhatkit** (for web search)

---

## Steps Performed

1. **Setup Environment**

   * Installed required Python libraries using pip.

2. **Speech Recognition**

   * Used the microphone input to capture the user's voice.
   * Converted speech to text using the SpeechRecognition library.

3. **Text-to-Speech**

   * Implemented pyttsx3 to convert text responses into voice output.

4. **Command Processing**

   * Program checks user commands using conditions (if-else).
   * Executes specific tasks based on keywords.

5. **Features Implemented**

   * Responds to greetings (e.g., "Hello")
   * Tells the current time and date
   * Searches Wikipedia for information
   * Performs a Google search
   * Exit command to stop the assistant

---

## How to Run the Project

1. Install dependencies:

   ```bash
   pip install pyttsx3 SpeechRecognition wikipedia pywhatkit pyaudio
   ```

2. Run the Python file:

   ```bash
   python voice_assistant.py
   ```

3. Speak commands like:

   * "Hello"
   * "What is AI?"
   * "Tell me the time"
   * "Search Python"
   * "Exit"

---

## Outcome

* Successfully built a simple voice assistant.
* Learned how to integrate voice input and audio output.
* Understood basic Natural Language Processing concepts.
* Gained hands-on experience with Python libraries and APIs.

---

## Conclusion

This project demonstrates how Python can be used to create interactive applications. It serves as a foundation for building more advanced AI-based assistants with additional features like automation, GUI, and smart integrations.

---

## Future Improvements

* Add a GUI interface
* Improve accuracy using advanced NLP
* Integrate APIs (weather, email, reminders)
* Add wake word detection (e.g., "Hey Assistant")

---

## Author

Piyush Pandey

