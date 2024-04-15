import time


class TypingTrainer:
    def __init__(self, exercise_generator, statistics_tracker):
        self.end_time = 0
        self.error_count = 0
        self.start_time = 0
        self.exercise_generator = exercise_generator
        self.statistics_tracker = statistics_tracker
        self.current_exercise = ""
        self.user_input = ""

    def start_typing_session(self):
        self.current_exercise = self.exercise_generator.generate_exercise(50)
        self.start_time = time.time()

    def calculate_speed(self, typing_time, exercise_text):
        characters_typed = len(exercise_text) - self.error_count
        return characters_typed / typing_time if typing_time > 0 else 0

    def reset(self):
        self.error_count = 0
        self.start_time = 0
        self.end_time = 0
