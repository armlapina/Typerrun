import random


class ExerciseGenerator:
    def __init__(self):
        self.exercises = []

    def generate_exercise(self, exercise_length):
        exercise = ''.join(
            random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ', k=exercise_length))
        self.exercises.append(exercise)
        return exercise

    def load_exercises_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.exercises = file.readlines()
            return True
        except FileNotFoundError:
            return False
