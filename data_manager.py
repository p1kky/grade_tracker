import json


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def generate_empty_json(jsonfile, subjects):
    empty_json_structure = {
        "quarters": {str(q): {subject: [] for subject in subjects} for q in range(1, 5)}
    }

    try:
        with open(jsonfile, "x") as f:
            json.dump(empty_json_structure, f, indent=4, ensure_ascii=False)

    except FileExistsError:
        pass


def reset_quarter_marks(data, quarter):
    for i in data["quarters"][quarter]:
        data["quarters"][quarter][i].clear()


def return_marks(data, quarter, subject):
    return data["quarters"][quarter][subject]


def add_mark(data, quarter, subject, mark):
    data["quarters"][quarter][subject].append(mark)


def remove_mark(data, quarter, subject, mark):
    data["quarters"][quarter][subject].remove(mark)


def reset_subject_marks(data, quarter, subject):
    data["quarters"][quarter][subject].clear()


def save_json(filename, data):
    with open(filename, "w", encoding="utf-8"):
        json.dump(data, filename, indent=4, ensure_ascii=False)
