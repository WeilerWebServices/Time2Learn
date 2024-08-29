#!/bin/bash

# Step 1: Create the project structure
mkdir -p Time2Learn/{assets,db,scripts,lessons,library}

# Step 2: Download and extract Python embedded version
cd Time2Learn
PYTHON_ZIP="python-embed.zip"
PYTHON_URL="https://www.python.org/ftp/python/3.9.6/python-3.9.6-embed-amd64.zip"

if [ ! -f $PYTHON_ZIP ]; then
    echo "Downloading Python embedded version..."
    curl -o $PYTHON_ZIP $PYTHON_URL
    unzip $PYTHON_ZIP -d python-embed
fi

# Step 3: Set up the virtual environment
echo "Setting up the virtual environment..."
python-embed/python.exe -m venv Time2Learn/venv

# Step 4: Activate the virtual environment and install dependencies
source Time2Learn/venv/Scripts/activate
pip install tk Pillow pygame

# Step 5: Create the main application file
cat > main.py <<EOL
import tkinter as tk
from tkinter import messagebox, Menu
from PIL import Image, ImageTk
import pygame

class Time2LearnApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time2Learn")
        self.root.geometry("1024x768")
        self.setup_ui()

    def setup_ui(self):
        # Setup menu
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.lesson_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Lessons", menu=self.lesson_menu)
        self.lesson_menu.add_command(label="1st Grade", command=self.load_lesson)

        self.menu.add_command(label="Library", command=self.open_library)
        self.menu.add_command(label="About", command=lambda: messagebox.showinfo("Info", "Time2Learn Application"))

        self.login_menu = self.menu.add_command(label="Log In", command=self.login_logout)

        # Load and set the background image
        image = Image.open("assets/logo.png")
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.update_login_status()

    def load_lesson(self):
        # Load lesson page (e.g., lesson_1.py)
        pass

    def open_library(self):
        # Open library to view books
        pass

    def update_login_status(self):
        # Update login/logout menu based on user status
        pass

    def login_logout(self):
        if self.is_logged_in:
            if messagebox.askokcancel("Log Out", "Are you sure you want to log out?"):
                self.is_logged_in = False
                self.update_login_status()
        else:
            self.is_logged_in = True
            self.update_login_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = Time2LearnApp(root)
    root.mainloop()
EOL

# Step 6: Create a sample lesson file
cat > lessons/lesson_1.py <<EOL
import tkinter as tk
from tkinter import messagebox

class Lesson1:
    def __init__(self, root):
        self.root = root
        self.root.title("1st Grade Sight Words - Lesson 1")
        self.setup_ui()

    def setup_ui(self):
        label = tk.Label(self.root, text="Welcome to Lesson 1", font=("Arial", 24))
        label.pack(pady=20)

        # Example content
        question_label = tk.Label(self.root, text="What word is this?", font=("Arial", 18))
        question_label.pack(pady=10)

        # Example answer options
        options = ["after", "again", "any", "ask"]
        for option in options:
            button = tk.Button(self.root, text=option, command=lambda opt=option: self.check_answer(opt))
            button.pack(pady=5)

    def check_answer(self, option):
        if option == "after":
            tk.messagebox.showinfo("Correct!", "Well done!")
        else:
            tk.messagebox.showwarning("Incorrect", "Try again.")

if __name__ == "__main__":
    root = tk.Tk()
    lesson = Lesson1(root)
    root.mainloop()
EOL

# Step 7: Create placeholder assets
echo "Creating placeholder assets..."
echo "Placeholder for the logo.png" > assets/logo.png
echo "Placeholder for the Time2Learn.mp3" > assets/Time2Learn.mp3

# Step 8: Inform the user that setup is complete
echo "Setup complete! Activate the virtual environment using 'source venv/Scripts/activate' and run 'main.py' in the 'Time2Learn' directory."