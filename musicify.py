from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title('mini musicify')
root.geometry("532x622")
root.configure(bg="white")
root.resizable(False, False)

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
currentsong = ""
paused = False

def load_music():
    global currentsong
    root.directory = filedialog.askdirectory()
    
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)
            
    for song in songs:
        songlist.insert("end", song)
        
    songlist.selection_set(0)
    currentsong = songs[songlist.curselection()[0]]
    
    
def play_music():
    global currentsong, paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, currentsong))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True
    
def next_music():
    global currentsong, paused
    
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(currentsong) + 1)
        currentsong = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global currentsong, paused
    
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(currentsong) - 1)
        currentsong = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='select your music folder or file', command=load_music)
menubar.add_cascade(label="Organise", menu=organise_menu)

songlist = Listbox(root, bg="black", fg="white", width=85, height=33)
songlist.pack()

playbtnim = PhotoImage(file="play.png")
pausebtnim = PhotoImage(file="pause (1).png")
nextbtnim = PhotoImage(file="next.png")
previbtnim = PhotoImage(file="previous.png")

control_frame = Frame(root)
control_frame.pack()

play_button = Button(control_frame, image=playbtnim, borderwidth=0, command=play_music)
pause_button = Button(control_frame, image=pausebtnim, borderwidth=0, command=pause_music)
next_button = Button(control_frame, image=nextbtnim, borderwidth=0, command=next_music)
previ_button = Button(control_frame, image=previbtnim, borderwidth=0, command=prev_music)

play_button.grid(row=0, column=2, padx=7, pady=10)
pause_button.grid(row=0, column=3, padx=7, pady=10)
next_button.grid(row=0, column=4, padx=7, pady=10)
previ_button.grid(row=0, column=1, padx=7, pady=10)

root.mainloop()
