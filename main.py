from interface import cli_interface
from data import data_manager

intro_text = "\n" * 3 + "-*- " * 3 + "Grade Tracker" + " -*-" * 3


def main_menu(data):
    while True:
        print(intro_text)

        school_quarter = cli_interface.get_quarter()

        if school_quarter == "0":
            print(intro_text)

            print("Вы успешно вышли из программы")

            break

        after_quarter_menu(data, school_quarter)


def after_quarter_menu(data, school_quarter):
    while True:
        print(intro_text)

        choice = cli_interface.afterquarter_choice()

        if choice == 1:
            subject_menu(data, school_quarter)

        elif choice == 2:
            cli_interface.get_gpa(data, school_quarter)

        elif choice == 3:
            cli_interface.delete_quarter_marks(data, school_quarter)

        elif choice == 0:
            break


def subject_menu(data, school_quarter):
    print(intro_text)

    user_subject = cli_interface.get_subject()

    while True:
        print(intro_text)

        choice = cli_interface.aftersubject_choice()

        if choice == 1:
            cli_interface.show_marks(data, school_quarter, user_subject)

        elif choice == 2:
            cli_interface.add_mark(data, school_quarter, user_subject)

        elif choice == 3:
            cli_interface.remove_mark(data, school_quarter, user_subject)

        elif choice == 4:
            cli_interface.reset_subject_marks(data, school_quarter, user_subject)

        elif choice == 5:
            cli_interface.print_quarter_mark(data, school_quarter, user_subject)

        elif choice == 0:
            break


def main():
    data = data_manager.load_json()

    main_menu(data)


if __name__ == "__main__":
    main()
