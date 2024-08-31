Suraj-Virtual-Assistant

![Screenshot 2024-08-31 220111](https://github.com/user-attachments/assets/9fe76e34-6bda-4bff-87c4-2ec4296ca548)


## Overview

Suraj Virtual Assistant is a voice-activated virtual assistant application built with Python, `Tkinter`, and various other libraries. It can perform tasks such as opening websites, playing music, fetching news, and more. The application has a professional user interface with interactive elements and a background image.

## Features

- **Voice Commands**: Recognizes and processes voice commands to perform actions such as opening websites or playing music.
- **News Fetching**: Retrieves and reads out the latest news headlines.
- **AI Interaction**: Uses OpenAI's GPT model to process commands and provide responses.
- **Background Image**: Displays a professional background image.
- **Interactive UI**: Includes interactive buttons with hover effects and a loading screen.
- **Music Library**: Allows playing songs from a predefined music library.
- **Error Handling**: Handles errors gracefully and provides feedback to the user.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/suraj-virtual-assistant.git
   cd suraj-virtual-assistant

2.Create and Activate Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.libreries installation
pip install speech_recognition pyttsx3 pygame requests gTTS customtkinter Pillow openai ctkimage

4.Add Configuration:
Obtain API keys  your own for OpenAI and NewsAPI.
Replace the placeholders in the code with your actual API keys. 
Disclaminer not use my api key its not work for all 

5.Running the Application
To start the virtual assistant application, run: python main.py

## Usage

1. **Start Recognition**: Click the "Start Recognition" button or use voice commands to activate the assistant.
2. **Voice Commands**:
   - Say "Suraj" to wake up the assistant.
   - Use commands like "open google", "play [song name]", or "news" to perform actions.
3. **Loading Screen**: A loading screen will appear during initialization to simulate progress.

## Functionalities

- **Voice Commands**: The assistant listens for the wake word "Suraj" and processes commands such as opening websites or playing music.
- **News Fetching**: Fetches the latest headlines from the news API and reads them aloud.
- **AI Processing**: Uses OpenAI's GPT model to respond to commands that don't fit predefined actions.
- **Error Handling**: Provides feedback if there are issues with speech recognition or other services.

## Troubleshooting

- **ModuleNotFoundError**: Ensure all dependencies are correctly installed. Check for typos in module names.
- **API Errors**: Verify that API keys are correctly configured and have the necessary permissions.
- **Performance Issues**: If the application hangs, check for issues in the threading or speech recognition parts of the code.

## Contact

For questions or support, contact me via WhatsApp: [9518772281](https://wa.me/9518772281).
