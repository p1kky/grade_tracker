import cli_interface
import data_manager

data_manager.generate_empty_json(cli_interface.subjects)
data = data_manager.load_json()

intro_text = "\n" * 3 + "-*- " * 3 + "Grade Tracker" + " -*-" * 3


def main():
    print(intro_text)

    school_quarter = cli_interface.get_quarter()

    print(intro_text)

    choice_after_quarter = cli_interface.afterquarter_choice()

    print(intro_text)

    match choice_after_quarter:
        case 1:
            user_subject = cli_interface.get_subject()
            print(f"Вы выбрали предмет: {user_subject}")

            print(intro_text)

            choice_after_subject = cli_interface.aftersubject_choice()

            match choice_after_subject:
                case 1:
                    cli_interface.show_marks(data, school_quarter, user_subject)

                case 2:
                    cli_interface.add_mark(data, school_quarter, user_subject)

                case 3:
                    cli_interface.remove_mark(data, school_quarter, user_subject)

                case 4:
                    cli_interface.reset_subject_marks(
                        data, school_quarter, user_subject
                    )

                case 5:
                    cli_interface.print_quarter_mark(data, school_quarter, user_subject)

        case 2:
            cli_interface.get_gpa(data, school_quarter)

        case 3:
            cli_interface.delete_quarter_marks(data, school_quarter)


if __name__ == "__main__":
    main()
