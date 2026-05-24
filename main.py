import tkinter as tk
from tkinter import scrolledtext
import voice_engine as ve
import webbrowser
import datetime
import os
import subprocess as sd
import sys  # Recommended for finding python executable
import threading


def process_input(user_text, source_type):
    if not user_text:
        return

    # Display User Input
    text_area.insert(tk.END, f"You ({source_type}): {user_text}\n")
    text_area.see(tk.END)

    query = user_text.lower()

    # 1. SPECIFIC WEBSITE COMMANDS
    if "open gmail" in query:
        webbrowser.open("https://mail.google.com")
        response = "Opening Gmail."
        print(response)

    elif "open facebook" in query:
        webbrowser.open("https://www.facebook.com")
        response = "Opening Facebook."
        print(response)

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube."
        print(response)

    # 2. CHECK TIME
    elif "time" in query:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        response = f"The current time is {current_time}."
        print(response)
    # 3. WEATHER (Placeholder)
    elif "weather" in query:
        response = "Please check a weather website for the forecast."
        print(response)
    # 4. DEFAULT: GOOGLE SEARCH EVERYTHING ELSE
    else:
        # If no command matched, send everything to Google Search
        search_term = user_text.strip()  # Use the full input text
        url = f"https://www.google.com/search?q={search_term}"

        webbrowser.open(url)
        response = f"Searching Google for: {user_text}"
        print(response)

    # OUTPUT
    text_area.insert(tk.END, f"System: {response}\n\n")
    ve.speak(response)

    if source_type == "Text":
        text_entry.delete(0, tk.END)


def handle_voice_search():
    status_label.config(text="Listening...", fg="red")
    root.update()

    threading.Thread(target=listen_thread).start()


def listen_thread():
    user_question = ve.listen()

    # Send result back to main thread safely
    root.after(0, lambda: process_voice_result(user_question))


def process_voice_result(user_question):
    status_label.config(text="Processing...", fg="orange")

    if user_question:
        process_input(user_question, "Voice")
    else:
        status_label.config(text="Ready", fg="green")
def handle_text_search():
    """Handles the typed input"""
    user_question = text_entry.get()

    if user_question:
        status_label.config(text="Processing...", fg="orange")
        # Send to the main processing function
        process_input(user_question, "Text")
        status_label.config(text="Ready", fg="green")
    else:
        ve.speak("Please type a question first.")


def log_out():
    """Destroys the main window and re-opens the sign-in page."""

    # CRITICAL FIX: Close the current window first
    root.destroy()

    try:
        # Using os.system as per your original code
       # os.system('python sign_in.py')

        # ALTERNATIVE (More Reliable):
         sd.Popen([sys.executable, "sign_in.py"])

    except Exception as e:
        print(f"Error opening sign-in page: {e}")


# --- GUI SETUP ---

root = tk.Tk()
root.title("RAPHSKI-Hybrid Search System")
root.geometry("600x500")

# 1. DISPLAY AREA (Top)
text_area = scrolledtext.ScrolledText(root, width=70, height=15, font=("Arial", 10))
text_area.pack(pady=10)

# 2. TEXT INPUT AREA (Middle)
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

text_entry = tk.Entry(input_frame, width=40, font=("Arial", 12))
text_entry.pack(side=tk.LEFT, padx=5)

btn_submit = tk.Button(input_frame, text="Search", command=handle_text_search, bg="#dddddd")
btn_submit.pack(side=tk.LEFT)

# 3. VOICE INPUT AREA (Bottom)
btn_voice = tk.Button(root, text="🎤 Use Voice Input", command=handle_voice_search, font=("Arial", 12), fg="#B6D0E2",
                      bg="#301934")
btn_voice.pack(pady=10)

status_label = tk.Label(root, text="Ready - Type or Speak", font=("Arial", 10))
status_label.pack()

btn_logout = tk.Button(root, text="Log Out", command=log_out, font=("Arial", 10), bg="red", fg="white")
btn_logout.pack(pady=5)

root.mainloop()