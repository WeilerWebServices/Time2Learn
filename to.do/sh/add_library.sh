#!/bin/bash

# Step 1: Create directories for library and assets
mkdir -p Time2Learn/{library/ebooks,library/audiobooks,assets/icons}

# Step 2: Update the main.py to include the library in the dropdown menu
cat >> Time2Learn/main.py <<EOL

class LibraryMenu:
    def __init__(self, root):
        self.root = root

    def setup_menu(self, menu):
        # Create a cascading library menu with 5 levels of submenus
        self.library_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Library", menu=self.library_menu)

        self.level1 = Menu(self.library_menu, tearoff=0)
        self.library_menu.add_cascade(label="Ebooks", menu=self.level1)
        self.level2 = Menu(self.level1, tearoff=0)
        self.level1.add_cascade(label="Fiction", menu=self.level2)
        self.level3 = Menu(self.level2, tearoff=0)
        self.level2.add_cascade(label="Science Fiction", menu=self.level3)
        self.level4 = Menu(self.level3, tearoff=0)
        self.level3.add_cascade(label="Dystopian", menu=self.level4)
        self.level5 = Menu(self.level4, tearoff=0)
        self.level4.add_cascade(label="Classics", menu=self.level5)

        self.level5.add_command(label="Book1", command=lambda: self.open_flipbook("library/ebooks/book1.pdf"))
        self.level5.add_command(label="Book2", command=lambda: self.open_flipbook("library/ebooks/book2.mobi"))

        # Add audiobooks
        self.audiobooks_menu = Menu(self.library_menu, tearoff=0)
        self.library_menu.add_cascade(label="Audiobooks", menu=self.audiobooks_menu)
        self.audiobooks_menu.add_command(label="Audiobook1", command=lambda: self.open_flipbook("library/audiobooks/audiobook1.mp3"))

    def open_flipbook(self, filepath):
        import flipbook
        flipbook.open_book(filepath)

# Initialize the LibraryMenu in the main application
library_menu = LibraryMenu(root)
library_menu.setup_menu(app.menu)

EOL

# Step 3: Create the flipbook.py script
cat > Time2Learn/flipbook.py <<EOL
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

EOL

# Step 4: Create placeholder ebooks and audiobooks
echo "Creating placeholder ebooks and audiobooks..."
echo "Placeholder for book1.pdf" > library/ebooks/book1.pdf
echo "Placeholder for book2.mobi" > library/ebooks/book2.mobi
echo "Placeholder for audiobook1.mp3" > library/audiobooks/audiobook1.mp3

# Step 5: Inform the user that setup is complete
echo "Library setup complete! You can now add your ebooks and audiobooks to the 'library' directory and run the main application."
