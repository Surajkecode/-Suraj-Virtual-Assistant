import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import pygame
import os
import customtkinter as ctk
from PIL import Image, ImageTk
from gtts import gTTS
import time
import openai
import threading

# Initialize modules
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi_key = "9149f3a6cdd6409e9aead4d05abedcaa"
openai.api_key = "sk-proj-CtSDVXUisHOc428D15SaT3BlbkFJypYIILc64kJYtHy41Gds"
music_library = {}  # Define your music library here


# Function to speak text
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


# Function to process commands
def process_command(command):
    commands = {
        "google": "https://google.com",
        "facebook": "https://facebook.com",
        "college": "https://www.tgpcet.com",
        "youtube": "https://youtube.com",
        "linkedin": "https://linkedin.com"
    }

    command_lower = command.lower()

    if any(keyword in command_lower for keyword in commands):
        for keyword, url in commands.items():
            if keyword in command_lower:
                webbrowser.open(url)
                return
    elif command_lower.startswith("play"):
        song = command_lower.split(" ")[1]
        link = music_library.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in the library.")
    elif "news" in command_lower:
        fetch_news()
    else:
        response = ai_process(command)
        speak(response)


# Function to fetch news
def fetch_news():
    try:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi_key}")
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
        else:
            speak("Failed to retrieve news.")
    except Exception as e:
        speak(f"Error fetching news: {e}")


# Function to process AI requests
def ai_process(command):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a virtual assistant named Suraj skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )
    return response.choices[0].message['content']


# Function to start speech recognition
def start_recognition():
    threading.Thread(target=run_recognition).start()


def run_recognition():
    speak("Initializing Suraj....")
    try:
        with sr.Microphone() as source:
            speak("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        word = recognizer.recognize_google(audio)
        if word.lower() == "suraj":
            speak("Yes")
            with sr.Microphone() as source:
                speak("Suraj Active...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                process_command(command)
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that.")
    except sr.RequestError as e:
        speak(f"Error with the speech recognition service: {e}")
    except Exception as e:
        speak(f"Error: {e}")


# Function to create the UI
def create_ui():
    app = ctk.CTk()
    app.title("Suraj Virtual Assistant")

    # Resize window to desired size
    app_width = 1280
    app_height = 720
    app.geometry(f"{app_width}x{app_height}")
    app.resizable(True, True)

    # Load and set background image using ImageTk.PhotoImage
    background_image = Image.open("robot.jpg")
    bg_image = ImageTk.PhotoImage(background_image.resize((app_width, app_height), Image.Resampling.LANCZOS))
    bg_label = ctk.CTkLabel(app, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Advanced Start Button with hover effect
    start_button = ctk.CTkButton(app, text="Start Recognition", command=start_recognition, fg_color="white",
                                 text_color="black")
    start_button.place(relx=0.5, rely=0.7, anchor="center")

    # Adding interactive UI elements
    start_button.bind("<Enter>", lambda e: start_button.configure(fg_color="lightgrey"))
    start_button.bind("<Leave>", lambda e: start_button.configure(fg_color="white"))

    # Show a loading screen before main UI
    show_loading_screen(app)

    app.mainloop()


# Function to show the loading screen
def show_loading_screen(app):
    loading_screen = ctk.CTkToplevel(app)
    loading_screen.title("Initializing...")
    loading_screen.geometry("300x150")
    loading_screen.grab_set()

    # Progress bar
    progress_var = ctk.DoubleVar()
    progress_bar = ctk.CTkProgressBar(loading_screen, variable=progress_var, width=200)
    progress_bar.place(relx=0.5, rely=0.5, anchor="center")

    progress_label = ctk.CTkLabel(loading_screen, text="Initializing Suraj...")
    progress_label.place(relx=0.5, rely=0.4, anchor="center")

    # Simulate loading
    for i in range(100):
        progress_var.set(i + 1)
        loading_screen.update_idletasks()
        time.sleep(0.03)

    loading_screen.destroy()


if __name__ == "__main__":
    create_ui()
