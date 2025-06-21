import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGameDark:
    def __init__(self, master):  # ← Fixed here
        self.master = master
        master.title("🎮 Number Guessing Game")
        master.configure(bg="#1e1e1e")

        self.text_color = "#ffffff"
        self.accent_color = "#00bcd4"

        self.difficulty_frame = tk.Frame(master, bg="#1e1e1e")
        self.game_frame = tk.Frame(master, bg="#1e1e1e")

        self.create_difficulty_screen()

    def create_difficulty_screen(self):
        self.clear_frame(self.game_frame)
        self.difficulty_frame.pack()

        tk.Label(self.difficulty_frame, text="Select Difficulty Level", font=("Helvetica", 16, "bold"), fg=self.accent_color, bg="#1e1e1e").pack(pady=15)

        tk.Button(self.difficulty_frame, text="Easy (1-50)", command=lambda: self.start_game(1, 50),
                  bg=self.accent_color, fg=self.text_color, font=("Helvetica", 12), width=20).pack(pady=6)
        tk.Button(self.difficulty_frame, text="Medium (1-100)", command=lambda: self.start_game(1, 100),
                  bg=self.accent_color, fg=self.text_color, font=("Helvetica", 12), width=20).pack(pady=6)
        tk.Button(self.difficulty_frame, text="Hard (1-500)", command=lambda: self.start_game(1, 500),
                  bg=self.accent_color, fg=self.text_color, font=("Helvetica", 12), width=20).pack(pady=6)

    def start_game(self, low, high):
        self.low = low
        self.high = high
        self.number_to_guess = random.randint(low, high)
        self.attempts = 0
        self.max_attempts = 10
        self.hint_trigger = 3

        self.clear_frame(self.difficulty_frame)
        self.create_game_screen()

    def create_game_screen(self):
        self.game_frame.pack()

        tk.Label(self.game_frame, text=f"Guess a number between {self.low} and {self.high}",
                 font=("Helvetica", 13), fg=self.text_color, bg="#1e1e1e").pack(pady=12)

        self.guess_entry = tk.Entry(self.game_frame, font=("Helvetica", 12), bg="#333333", fg=self.text_color, insertbackground=self.text_color)
        self.guess_entry.pack(pady=5)

        tk.Button(self.game_frame, text="Submit Guess", command=self.check_guess,
                  bg=self.accent_color, fg=self.text_color, font=("Helvetica", 12), width=20).pack(pady=8)

        self.feedback_label = tk.Label(self.game_frame, text="", font=("Helvetica", 12),
                                       fg=self.accent_color, bg="#1e1e1e")
        self.feedback_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            return

        self.attempts += 1

        if guess < self.number_to_guess:
            self.feedback_label.config(text="Too low.")
        elif guess > self.number_to_guess:
            self.feedback_label.config(text="Too high.")
        else:
            messagebox.showinfo("🎉 Congratulations!", f"You guessed it in {self.attempts} attempts!")
            self.ask_replay()
            return

        if self.attempts == self.hint_trigger:
            hint = "even" if self.number_to_guess % 2 == 0 else "odd"
            messagebox.showinfo("💡 Hint", f"The number is {hint}.")

        if self.attempts >= self.max_attempts:
            messagebox.showinfo("❌ Game Over", f"Out of attempts. The number was {self.number_to_guess}.")
            self.ask_replay()

    def ask_replay(self):
        self.clear_frame(self.game_frame)
        if messagebox.askyesno("Play Again?", "Would you like to play again?"):
            self.create_difficulty_screen()
        else:
            self.master.quit()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        frame.pack_forget()

# Main
root = tk.Tk()
root.geometry("400x300")
game = NumberGuessingGameDark(root)
root.mainloop()
# This code creates a dark-themed number guessing game GUI using Tkinter.
# It allows users to select difficulty levels and provides feedback on their guesses.