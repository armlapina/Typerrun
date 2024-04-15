### Описание проекта
Цель проекта Typerrun - помочь пользователям улучшить навыки печати без необходимости смотреть на клавиатуру. Программа предлагает упражнения по печати на клавиатуре и проверяет правильность ввода.

### Реализуемый функционал
1. Генерация случайных упражнений для печати.
2. Оценка правильности печати и подсчет очков.
3. Учет скорости печати.
4. Визуализация статистики о проделанной работе.

### Архитектура
Проект будет разделен на следующие классы и функции:
- ExerciseGenerator: Класс для генерации заданий по печати. Методы: generate_exercise(), load_exercises_from_file().
- TypingTrainer: Класс для тренировки печати вслепую. Методы: start_typing_session(), calculate_speed().
- StatisticsTracker: Класс для отслеживания статистики. Методы: track_errors(), calculate_speed().
- UserInterface: Класс для отображения интерфейса тренажера. Находится в main.py. Методы: show_message(), choose_exercise_type(), show_statistics(), show_main_menu(), start_session_random(), start_session_file(), show_typing_interface(), check_input(), 
