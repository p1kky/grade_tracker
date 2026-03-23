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
            continue

        if not (1 <= int(user_subject) <= len(subjects)):
            continue

        return subjects[int(user_subject) - 1]


def get_gpa():
    pass


def reset_quarter_marks():
    pass


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
            continue

        return int(choice)


def get_subject_marks():
    pass


def show_marks():
    pass


def add_mark():
    pass


def remove_mark():
    pass


def reset_subject_marks():
    pass


def get_quarter_mark():
    pass
