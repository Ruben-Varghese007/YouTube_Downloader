import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_youtube_video(url, save_path):
    ydl_opts = {'outtmpl': f'{save_path}/%(title)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def choose_save_location():
    # Open the file dialog to select a folder
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Force Tkinter to update before opening the file dialog
    root.update()
    
    # Open the dialog box
    folder_selected = filedialog.askdirectory(title="Select Save Location")
    
    # Return the selected folder path
    return folder_selected

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    
    save_path = choose_save_location()  # Get the folder selected by the user
    
    if not save_path:  # Check if user canceled the dialog
        print("No folder selected. Exiting.")
    else:
        print(f"Saving video to: {save_path}")
        download_youtube_video(video_url, save_path)
