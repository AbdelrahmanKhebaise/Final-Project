import os
import pygame
from tkinter import *
from tkinter import filedialog

# Initialize Pygame mixer
pygame.mixer.init()

# Global variable for songs directory
songs_directory = ""

# Function to play music
def play_music():
    try:
        song = song_listbox.get(ACTIVE)  # Get the selected song
        song_path = os.path.join(songs_directory, song)  # Get the full path of the song
        pygame.mixer.music.load(song_path)  # Load the song
        pygame.mixer.music.play(loops=0, start=0.0)  # Play the song
    except pygame.error as e:
        print(f"Error playing song: {e}")  # Print error if song fails to play

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()  # Pause the music

# Function to resume the music
def resume_music():
    pygame.mixer.music.unpause()  # Resume the music

# Function to load songs from a directory
def load_songs():
    global songs_directory
    song_files = filedialog.askopenfilenames(
        title="Select Music Files", 
        filetypes=[("All Files", "*.*"), ("MP3 Files", "*.mp3")]
    )
    
    if song_files:
        # Set the directory path from the first file selected
        songs_directory = os.path.dirname(song_files[0])
        
        for song in song_files:
            song_name = os.path.basename(song)
            
            # Check if the song is already in the listbox, if not add it
            if song_name not in song_listbox.get(0, END):
                song_listbox.insert(END, song_name)


# Preload specific songs
def preload_songs():
    global songs_directory
    songs_directory = os.getcwd()  # Use the current directory
    preloaded_songs = [
        "Taylor Swift - 22.mp3",
        "Taylor Swift - Cruel Summer (Official Audio).mp3",
        "Taylor Swift - Look What You Made Me Do.mp3",
        "Taylor Swift - Love Story.mp3",
        "Taylor Swift - Blank Space.mp3",
        "Taylor Swift - Shake It Off.mp3",
        "Taylor Swift - Style.mp3",
        "Taylor Swift - We Are Never Ever Getting Back Together.mp3",
        "Taylor Swift - Wildest Dreams.mp3",
        "Taylor Swift - You Belong With Me.mp3"
    ]
    for song in preloaded_songs:
        song_path = os.path.join(songs_directory, song)
        if os.path.exists(song_path):  # Check if the file exists
            song_listbox.insert(END, song)

# Create the main window
root = Tk()
root.title("Music Player")

# Main area for music player
main_frame = Frame(root, bg="pink")
main_frame.pack(fill=BOTH, expand=True)

label = Label(main_frame, text="Music Player", font=("Helvetica", 20))
label.pack(pady=10)

song_listbox = Listbox(main_frame, width=50, height=10, selectmode=SINGLE, font=("Helvetica", 12))
song_listbox.pack(pady=20)

# Buttons for controls
play_button = Button(main_frame, text="Play", width=10, height=2, font=("Helvetica", 12), command=play_music)
play_button.pack(side=LEFT, padx=10, pady=20)

pause_button = Button(main_frame, text="Pause", width=10, height=2, font=("Helvetica", 12), command=pause_music)
pause_button.pack(side=LEFT, padx=10, pady=20)

resume_button = Button(main_frame, text="Resume", width=10, height=2, font=("Helvetica", 12), command=resume_music)
resume_button.pack(side=LEFT, padx=10, pady=20)

load_button = Button(main_frame, text="Add Songs", width=20, height=2, font=("Helvetica", 12), command=load_songs)
load_button.pack(pady=20)

# Preload songs
preload_songs()

# Start the Tkinter event loop
root.mainloop()
