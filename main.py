import cli_interface

json_data_file = "marks.json"

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
                    cli_interface.show_marks()

                case 2:
                    cli_interface.add_mark()

                case 3:
                    cli_interface.remove_mark()

                case 4:
                    cli_interface.reset_subject_marks()

                case 5:
                    cli_interface.get_quarter_mark()

        case 2:
            cli_interface.get_gpa()

        case 3:
            cli_interface.reset_quarter_marks()

    print(intro_text)


if __name__ == "__main__":
    main()
