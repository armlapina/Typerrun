class StatisticsTracker:
    def __init__(self):
        self.error_count = 0
        self.start_time = 0
        self.end_time = 0
        self.time = 0

    def track_errors(self, input_text, exercise_text):
        for i in range(min(len(input_text), len(exercise_text))):
            if input_text[i] != exercise_text[i]:
                self.error_count += 1

    def calculate_speed(self, typing_time, characters_typed):
        typing_speed = len(characters_typed) / typing_time if typing_time > 0 else 0
        return typing_speed
