import data_manager

subjects = (
    "Бел. яз",
    "Бел. лит",
    "Русск. яз",
    "Русск. лит",
    "Англ. яз",
    "История Беларуси",
    "Всемирная история",
    "Обществознание",
    "География",
    "Биология",
    "Математика",
    "Физика",
    "Химия",
    "Информатика",
    "Физ-ра",
    "Труды",
)


def get_quarter():
    while True:
        quarter = input("Выберите четверть:\n - ").strip()

        if quarter not in map(str, range(1, 5)):
            print("Напишите цифру в диапазоне от 1 до 4\n")

            continue

        return quarter


def afterquarter_choice():
    while True:
        choice = input(
            "Выберите действие из перечисленных (цифра): \n"
            " 1. Выбрать предмет\n"
            " 2. Посчитать средний балл за четверть\n"
            " 3. Сбросить отметки за четверть\n"
            " - "
        ).strip()

        if choice not in map(str, range(1, 4)):
            print("Напишите цифру от 1 до 3\n")

            continue

        return int(choice)


def print_subjects():
    for i, subject in enumerate(subjects, start=1):
        print(f" {i}. {subject}")


def get_subject():
    print_subjects()

    while True:
        user_subject = input(
            "Выберите предмет из выше перечисленных (цифра):\n - "
        ).strip()

        if not user_subject.isdigit():
            print(f"Напишите цифру от 1 до {len(subjects)}\n")

            continue

        if not (1 <= int(user_subject) <= len(subjects)):
            print(f"Напишите цифру от 1 до {len(subjects)}\n")

            continue

        return subjects[int(user_subject) - 1]


def get_gpa(data, quarter):
    quarter_marks_list = data_manager.return_quarter_marks(data, quarter)
    final_quarter_marks_list = []

    for i in quarter_marks_list:
        final_quarter_marks_list.append(calculate_quarter_mark(i))

    result = round((sum(final_quarter_marks_list) / len(final_quarter_marks_list)), 2)

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


def aftersubject_choice():
    while True:
        choice = input(
            "Выберите действие из перечисленных (цифра): \n"
            " 1. Просмотреть отметки\n"
            " 2. Добавить отметку\n"
            " 3. Удалить отметку\n"
            " 4. Сбросить отметки\n"
            " 5. Посчитать четвертную отметку по предмету\n"
            " - "
        ).strip()

        if choice not in map(str, range(1, 6)):
            print("Напишите цифру от 1 до 5\n")

            continue

        return int(choice)


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


def calculate_quarter_mark(subject_marks):
    while True:
        if len(subject_marks) < 2:
            print(
                "Посчитать средний балл не удается, менее чем 2 отметки по какому то из предметов"
            )

            exit()

        result = round((sum(subject_marks) / len(subject_marks)), 0)

        return result


def print_quarter_mark(data, quarter, subject):
    subject_marks = data_manager.return_subject_marks(data, quarter, subject)

    result = calculate_quarter_mark(subject_marks)

    print(f"Ваша четвертная отметка по '{subject}' = {result}")
