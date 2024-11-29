import os
import platform

def open_book(filepath):
    file_ext = os.path.splitext(filepath)[-1].lower()

    if file_ext in ['.pdf', '.mobi', '.epub']:
        open_ebook(filepath)
    elif file_ext in ['.mp3', '.mp4']:
        play_media(filepath)
    else:
        print("Unsupported file format")

def open_ebook(filepath):
    if platform.system() == "Windows":
        os.system(f'start "" "{filepath}"')
    elif platform.system() == "Linux":
        os.system(f'xdg-open "{filepath}"')
    elif platform.system() == "Darwin": # Mac OS
        os.system(f'open "{filepath}"')

def play_media(filepath):
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

    # Wait until the music finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

