def calculate_quarter_mark(subject_marks):
    while True:
        if len(subject_marks) < 2:
            print(
                "Посчитать средний балл не удается, менее чем 2 отметки по какому то из предметов"
            )

            return None

        result = round((sum(subject_marks) / len(subject_marks)), 0)

        return result


def calculate_gpa(data, quarter, data_manager):
    quarter_marks_list = data_manager.return_quarter_marks(data, quarter)

    final_marks = []

    for marks in quarter_marks_list:
        subject_avg = calculate_quarter_mark(marks)

        if subject_avg is not None:
            final_marks.append(subject_avg)

    if not final_marks:
        return None

    return round(sum(final_marks) / len(final_marks), 2)
