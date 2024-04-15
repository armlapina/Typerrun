import tkinter as tk
from tkinter import filedialog, messagebox
import time
from typing_trainer import TypingTrainer
from statistics_tracker import StatisticsTracker
from exercise_generator import ExerciseGenerator


class TypingInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Trainer")
        self.root.geometry("800x800")
        self.statistics_tracker = StatisticsTracker()
        self.typing_trainer = TypingTrainer(ExerciseGenerator(), self.statistics_tracker)

        self.exercise_label = tk.Label(self.root, text="")
        self.exercise_label.pack()

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.start_button = tk.Button(self.root, text="Start Typing Session", command=self.choose_exercise_type)
        self.start_button.pack()

        self.statistics_button = tk.Button(self.root, text="Statistics", command=self.show_statistics)
        self.statistics_button.pack()

        self.random_button = tk.Button(self.root, text="Random Text", command=self.start_session_random)
        self.file_button = tk.Button(self.root, text="Text from File", command=self.start_session_file)
        self.back_button = tk.Button(self.root, text="Back to Main Menu", command=self.show_main_menu)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

    def show_message(self, message, color):
        message_label = tk.Label(self.root, text=message, fg=color)
        message_label.pack()
        message_label.after(3000, message_label.destroy)

    def choose_exercise_type(self):
        self.start_button.pack_forget()
        self.statistics_button.pack_forget()
        self.exit_button.pack_forget()

        self.random_button.pack()
        self.file_button.pack()
        self.back_button.pack()
        self.input_entry.delete(0, tk.END)

    def show_main_menu(self):
        self.statistics_tracker.end_time = time.time()
        if self.statistics_tracker.start_time != 0:
            self.statistics_tracker.time = self.statistics_tracker.end_time - self.statistics_tracker.start_time
        self.random_button.pack_forget()
        self.file_button.pack_forget()
        self.back_button.pack_forget()
        self.start_button.pack()
        self.statistics_button.pack()
        self.exit_button.pack()
        self.root.mainloop()

    def start_session_random(self):
        self.statistics_tracker.end_time = time.time()
        self.statistics_tracker.time = self.statistics_tracker.end_time - self.statistics_tracker.start_time
        self.statistics_tracker.start_time = time.time()
        self.typing_trainer.start_typing_session()
        self.show_typing_interface()

    def start_session_file(self):
        self.statistics_tracker.end_time = time.time()
        self.statistics_tracker.time = self.statistics_tracker.end_time - self.statistics_tracker.start_time
        self.statistics_tracker.start_time = time.time()
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                file_text = file.read()
            self.typing_trainer.current_exercise = file_text
            self.show_typing_interface()

    def show_typing_interface(self):
        self.exercise_label.config(text=self.typing_trainer.current_exercise)
        self.input_entry.bind("<Key>", lambda event: self.check_input(event) or "break")
        self.statistics_tracker.start_time = time.time()

    def check_input(self, event):
        if event.keycode == 22:  # Backspace key
            if len(self.typing_trainer.user_input) > 0:
                self.typing_trainer.user_input = self.typing_trainer.user_input[0:-1]
            return True
        if event.keycode in [50, 114, 111, 113, 116, 37]:  # Ignore Shift key
            return True
        if event.keycode == 65:
            input_char = " "
        else:
            input_char = event.char
        exercise_text = self.typing_trainer.current_exercise
        if input_char == exercise_text[len(self.typing_trainer.user_input)]:
            self.typing_trainer.user_input += input_char
            if self.typing_trainer.user_input == exercise_text:
                self.exercise_label.config(text="")
                messagebox.showinfo("Success", "Typing completed successfully!")
                self.choose_exercise_type()
                return False
            return True
        else:
            self.typing_trainer.error_count += 1
            return False

    def show_statistics(self):
        avg_mistakes = 0
        if len(self.typing_trainer.current_exercise) > 0:
            avg_mistakes = self.statistics_tracker.error_count / len(self.typing_trainer.current_exercise)
        best_wpm = self.statistics_tracker.calculate_speed(time.time() - self.statistics_tracker.start_time,
                                                           self.typing_trainer.current_exercise)
        messagebox.showinfo("Statistics", f"Average Mistakes: {avg_mistakes}\nBest WPM: {best_wpm}")


if __name__ == "__main__":
    typing_interface = TypingInterface()
    typing_interface.show_main_menu()
