import pyautogui
import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
from tkinter import messagebox
from tkinter import * 
recognizer = sr.Recognizer()
with sr.Microphone() as source:       
    audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio)
        engine = pyttsx3.init()

        x="AIzaSyCDGF67u4Szetf_pUpAdAlNkXMWAi61uhg"
        genai.configure(api_key=x)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(text)
        
        engine.say(response.text)
        
        engine.runAndWait()
    
    except sr.UnknownValueError:
        messagebox.showinfo("info","Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
            
        messagebox.showinfo("info","Could not request results")