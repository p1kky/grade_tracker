import json

from config import config


# --- json basic func-s


def load_json():
    try:
        with open(config.BASE_FILENAME, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data

    except FileNotFoundError:
        generate_empty_json(config.SUBJECTS)


def save_json(data):
    with open(config.BASE_FILENAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def generate_empty_json(subjects):
    empty_json_structure = {
        "quarters": {str(q): {subject: [] for subject in subjects} for q in range(1, 5)}
    }

    try:
        with open(config.BASE_FILENAME, "x") as f:
            json.dump(empty_json_structure, f, indent=4, ensure_ascii=False)

    except FileExistsError:
        pass


# --- quarter


def return_quarter_marks(data, quarter):
    whole_list = []

    for i in data["quarters"][quarter]:
        whole_list.append(data["quarters"][quarter][i])

        save_json(data)

    return whole_list


def reset_quarter_marks(data, quarter):
    for i in data["quarters"][quarter]:
        data["quarters"][quarter][i].clear()

        save_json(data)


# --- subject


def return_subject_marks(data, quarter, subject):
    return data["quarters"][quarter][subject]


def add_mark(data, quarter, subject, mark):
    data["quarters"][quarter][subject].append(mark)

    save_json(data)


def remove_mark(data, quarter, subject, mark):
    data["quarters"][quarter][subject].remove(mark)

    save_json(data)


def reset_subject_marks(data, quarter, subject):
    data["quarters"][quarter][subject].clear()

    save_json(data)
