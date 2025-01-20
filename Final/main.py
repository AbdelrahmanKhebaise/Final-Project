import os
import pygame
from tkinter import *
from tkinter import filedialog

# Initialize Pygame mixer
pygame.mixer.init()

# Function to play music
def play_music():
    song = song_listbox.get(ACTIVE)  # Get the selected song
    song_path = os.path.join(songs_directory, song)  # Get the full path of the song
    pygame.mixer.music.load(song_path)  # Load the song
    pygame.mixer.music.play(loops=0, start=0.0)  # Play the song

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Function to resume the music
def resume_music():
    pygame.mixer.music.unpause()

# Function to load songs from a directory
def load_songs():
    global songs_directory
    songs_directory = filedialog.askdirectory()  # Ask user to select a directory
    if songs_directory:
        # Clear the listbox
        song_listbox.delete(0, END)
        # Add all mp3 files in the directory to the listbox
        for song in os.listdir(songs_directory):
            if song.endswith(".mp3"):
                song_listbox.insert(END, song)

# Preload specific songs
def preload_songs():
    global songs_directory
    songs_directory = os.getcwd()  # Use the current directory
    preloaded_songs = [
        "Taylor Swift - 22.mp3",
        "Taylor Swift - Cruel Summer (Official Audio).mp3",
        "Taylor Swift - Look What You Made Me Do.mp3",
        "Taylor Swift - Love Story.mp3",
        "Taylor Swift - Shake It Off.mp3",
        "Taylor Swift - Style.mp3",
        "Taylor Swift - We Are Never Ever Getting Back Together.mp3",
        "Taylor Swift - Wildest Dreams.mp3",
        "Taylor Swift - You Belong With Me.mp3"
    ]
    for song in preloaded_songs:
        song_listbox.insert(END, song)

# Create the main window
root = Tk()
root.title("Music Player")

# Main area for music player
main_frame = Frame(root, bg="white")
main_frame.pack(fill=BOTH, expand=True)

label = Label(main_frame, text="Music Player", font=("Helvetica", 20))
label.pack(pady=10)

song_listbox = Listbox(main_frame, width=50, height=10, selectmode=SINGLE, font=("Helvetica", 12))
song_listbox.pack(pady=20)

play_button = Button(main_frame, text="Play", width=10, height=2, font=("Helvetica", 12), command=play_music)
play_button.pack(side=LEFT, padx=10, pady=20)

pause_button = Button(main_frame, text="Pause", width=10, height=2, font=("Helvetica", 12), command=pause_music)
pause_button.pack(side=LEFT, padx=10, pady=20)

stop_button = Button(main_frame, text="Stop", width=10, height=2, font=("Helvetica", 12), command=stop_music)
stop_button.pack(side=LEFT, padx=10, pady=20)

resume_button = Button(main_frame, text="Resume", width=10, height=2, font=("Helvetica", 12), command=resume_music)
resume_button.pack(side=LEFT, padx=10, pady=20)

load_button = Button(main_frame, text="Load Songs", width=20, height=2, font=("Helvetica", 12), command=load_songs)
load_button.pack(pady=20)

# Preload songs
preload_songs()

# Start the Tkinter event loop
root.mainloop()
