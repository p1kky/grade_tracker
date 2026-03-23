import calculations
import config
import data_manager

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
def print_subjects():
    for i, subject in enumerate(config.SUBJECTS, start=1):
        print(f" {i}. {subject}")


def get_subject():
    print_subjects()

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
            " 2. Добавить отметку\n"
            " 3. Удалить отметку\n"
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
        user_new_mark = input(
            f"Введи новую отметку по '{subject}' (1-10):\n - "
        ).strip()

        if not user_new_mark.isdigit():
            print("Напишите цифру\n")

            continue

        user_new_mark = int(user_new_mark)

        if user_new_mark > 10 or user_new_mark < 1:
            print("Напишите цифру в диапазоне от 1 до 10\n")

            continue

        data_manager.add_mark(data, quarter, subject, user_new_mark)

        print(f"По '{subject}' была добавлена отметка: {user_new_mark}")

        break


def remove_mark(data, quarter, subject):
    subject_marks = data_manager.return_subject_marks(data, quarter, subject)

    while True:
        user_mark = input(f"Введи какую отметку убрать по '{subject}':\n - ").strip()

        if not user_mark.isdigit():
            print("Напишите цифру\n")

            continue

        user_mark = int(user_mark)

        if user_mark not in subject_marks:
            print("Напишите отметку из имеющихся\n")

            continue

        data_manager.remove_mark(data, quarter, subject, user_mark)
        print(f"По '{subject}' была удалена отметка: {user_mark}")

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
