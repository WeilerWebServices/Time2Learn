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
