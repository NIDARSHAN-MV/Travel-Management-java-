import tkinter as tk
import webbrowser
import time
import threading
import socket

def open_browser():
    webbrowser.open_new_tab('http://127.0.0.1:5000')

def check_internet_connection():
    try:
        # Try to connect to Google's DNS server
        socket.create_connection(('8.8.8.8', 53), timeout=3)
        return True
    except OSError:
        return False

def start_loading():
    global timer_id
    loading_label.config(text="Connecting to server...")
    timer_id = root.after(8000, stop_loading)

def stop_loading():
    if check_internet_connection():
        open_browser_button.pack(pady=10)
        loading_label.pack_forget()
        try_again_button.pack_forget()  # Hide the "Try Again" button
    else:
        loading_label.config(text="Can't connect to the internet")
        try_again_button.pack(pady=10)  # Display the "Try Again" button
    root.update()

def retry_loading():
    try_again_button.pack_forget()  # Hide the "Try Again" button
    loading_thread = threading.Thread(target=start_loading)
    loading_thread.start()

root = tk.Tk()
root.geometry("500x600")
root.title("Welcome to my app!")

welcome_label = tk.Label(root, text="Welcome to my app!", font=("Arial Bold", 20))
welcome_label.pack(pady=50)

loading_label = tk.Label(root, text="Loading...", font=("Arial Bold", 16))
loading_label.pack(pady=10)

open_browser_button = tk.Button(root, text="Open Browser", command=open_browser)
try_again_button = tk.Button(root, text="Try Again", command=retry_loading)
try_again_button.pack_forget()  # Initially hidden

loading_thread = threading.Thread(target=start_loading)
loading_thread.start()

root.mainloop()
