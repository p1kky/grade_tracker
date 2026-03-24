from core import calculations
from config import config
from data import data_manager

# --- quarter choice


def get_quarter():
    while True:
        quarter = input("Выберите четверть (0 - Выйти):\n - ").strip()

        if quarter not in map(str, range(0, 5)):
            print("Напишите цифру в диапазоне от 0 до 4\n")

            continue

        return quarter


# --- after quarter choice


def afterquarter_choice():
    while True:
        choice = input(
            "Выберите действие из перечисленных (цифра): \n"
            " 0. Назад\n"
            " 1. Выбрать предмет\n"
            " 2. Посчитать средний балл за четверть\n"
            " 3. Сбросить отметки за четверть\n"
            " - "
        ).strip()

        if choice not in map(str, range(0, 4)):
            print("Напишите цифру от 0 до 3\n")

            continue

        return int(choice)


# -- choice functions


# help func
def print_subjects(data, quarter):
    for i, subject in enumerate(config.SUBJECTS, start=1):
        print(
            f" {i}. {subject}  (отметки: {', '.join(map(str, data_manager.return_subject_marks(data, quarter, subject)))})"
        )


def get_subject(data, quarter):
    print_subjects(data, quarter)

    while True:
        user_subject = input(
            "Выберите предмет из выше перечисленных (цифра):\n - "
        ).strip()

        if not user_subject.isdigit():
            print(f"Напишите цифру от 1 до {len(config.SUBJECTS)}\n")

            continue

        if not (1 <= int(user_subject) <= len(config.SUBJECTS)):
            print(f"Напишите цифру от 1 до {len(config.SUBJECTS)}\n")

            continue

        return config.SUBJECTS[int(user_subject) - 1]


def get_gpa(data, quarter):
    result = calculations.calculate_gpa(data, quarter, data_manager)

    print(f"Ваш средний балл за четверть: {result}")


def delete_quarter_marks(data, quarter):
    while True:
        confirmation = (
            input(
                "Вы уверены, что хотите сбросить отметки по всем предметам за четверть? (да/нет):\n - "
            )
            .lower()
            .strip()
        )

        if confirmation not in ("да", "нет"):
            print("Напишите 'да' или 'нет'\n")

            continue

        if confirmation == "да":
            data_manager.reset_quarter_marks(data, quarter)
            print(f"Ваши отметки за {quarter} четверть были успешно сброшены")

        break


# --- choice after subject


def aftersubject_choice():
    while True:
        choice = input(
            "Выберите действие из перечисленных (цифра): \n"
            " 0. Назад\n"
            " 1. Просмотреть отметки\n"
            " 2. Добавить отметки\n"
            " 3. Удалить отметки\n"
            " 4. Сбросить отметки\n"
            " 5. Посчитать четвертную отметку по предмету\n"
            " - "
        ).strip()

        if choice not in map(str, range(0, 6)):
            print("Напишите цифру от 0 до 5\n")

            continue

        return int(choice)


# -- choice functions


def show_marks(data, quarter, subject):
    subject_marks = data_manager.return_subject_marks(data, quarter, subject)

    print(f"Ваши отметки по предмету '{subject}': {', '.join(map(str, subject_marks))}")


def add_mark(data, quarter, subject):
    while True:
        user_new_marks = (
            input(f"Введи новые отметки через пробел по '{subject}' (1-10):\n - ")
            .strip()
            .split()
        )

        if not user_new_marks:
            print("Введите хотя бы 1 число\n")

            continue

        try:
            user_new_marks = [int(x) for x in user_new_marks]
        except ValueError:
            print("Все значения должны быть числами\n")

            continue

        if any(x < 1 or x > 10 for x in user_new_marks):
            print("Напишите цифры в диапазоне от 1 до 10\n")

            continue

        data_manager.add_mark(data, quarter, subject, user_new_marks)

        print(
            f"По '{subject}' была добавлены отметки: {', '.join(map(str, user_new_marks))}"
        )

        break


def remove_mark(data, quarter, subject):
    subject_marks = data_manager.return_subject_marks(data, quarter, subject)

    while True:
        user_marks_to_remove = (
            input(f"Введи какую отметку убрать по '{subject}':\n - ").strip().split()
        )

        if not user_marks_to_remove:
            print("Введите хотя бы одну отметку\n")

            continue

        try:
            user_marks_to_remove = [int(x) for x in user_marks_to_remove]
        except ValueError:
            print("Все значения должны быть числами\n")

            continue

        if any(x not in subject_marks for x in user_marks_to_remove):
            print("Какой то из указанных отметок нет в списке\n")

            continue

        for mark in user_marks_to_remove:
            data_manager.remove_mark(data, quarter, subject, mark)

        print(
            f"По '{subject}' была удалены отметки: {', '.join(map(str, user_marks_to_remove))}"
        )

        break


def reset_subject_marks(data, quarter, subject):
    while True:
        confirmation = (
            input("Вы уверены, что хотите сбросить отметки по предмету? (да/нет):\n - ")
            .lower()
            .strip()
        )

        if confirmation not in ("да", "нет"):
            print("Напишите 'да' или 'нет'\n")

            continue

        if confirmation == "да":
            data_manager.reset_subject_marks(data, quarter, subject)
            print(f"Ваши отметки по '{subject}' были успешно сброшены")

            break


def print_quarter_mark(data, quarter, subject):
    subject_marks = data_manager.return_subject_marks(data, quarter, subject)
    result = calculations.calculate_quarter_mark(subject_marks)

    print(f"Ваша четвертная отметка по '{subject}' = {result}")
