import pygame

# Initialize the mixer
pygame.mixer.init()

# Load the music file
music_file = "C:/Users/Leonovo/Downloads/spotifydown.com - Warm Colours.mp3"
pygame.mixer.music.load(music_file)

# Play the music
pygame.mixer.music.play()

# Keep the program running while the music is playing
while pygame.mixer.music.get_busy():
    continue
