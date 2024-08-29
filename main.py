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
