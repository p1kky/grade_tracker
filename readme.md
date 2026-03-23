# 📚 CLI Grade Tracker 

A terminal-based electronic school journal (Grade Tracker) designed for students and educators. Despite being CLI-based, the interface is clean, intuitive, and user-friendly, making grade management straightforward and efficient.

--- 

## ✨ Features 
- Quarter Selection – Choose the school quarter to work with.
- Subject Management – View a list of subjects and select one to manage with.

### Quarter-Wide Operations:
- Calculate average grades for the quarter (with validation that every subject has grades)
- Reset all grades for the quarter (requires confirmation)

### Grade Operations per Subject:
- View grades
- Add a grade
- Delete a grade
- Reset grades for the subject (requires confirmation)
- Calculate quarter average (checks that at least 2 grades exist)

### Data Persistence – 
All grades are stored in a marks.json file for easy saving and loading, managed by one file: data_manager.
### Structured Code – 
The project is organized into folders: configuration, interface, calculations, data management, etc., making it maintainable and extendable.

---

## 🛠 Installation 

You can set up the project either via Git or by downloading the ZIP file.

### Option 1: Clone with Git

```bash
git clone https://github.com/yourusername/cli-grade-tracker.git
cd cli-grade-tracker
```

### Option 2: Download ZIP

1. Go to the repository page on GitHub.
2. Click the Code → Download ZIP button.
3. Extract the ZIP file to your preferred location.
4. Open a terminal and navigate into the extracted folder:
```bash
cd path/to/cli-grade-tracker
```

---

## 🚀 Usage 

1. Run the main script:
```bash
python3 main.py
```
2. Follow the intuitive prompts to:
- Select the quarter
- Choose a subject
- View, add, delete, or reset grades
- Calculate averages for a subject or the entire quarter
- Confirm actions when prompted (e.g., resetting grades).

> Tip: All your data is stored in marks.json automatically — no manual saving required.

---

## 📂 Project Structure 

```bash
grade-tracker/
├─ main.py              # Entry point
├─ config/
│  └─ config.py         # Project configuration
├─ interface/
│  └─ cli_interface.py  # Terminal interface logic
├─ core/
│  └─ calculations.py   # Grade calculation functions
├─ data/
│  ├─ data_manager.py   # JSON file operations
│  └─ marks.json        # Stored grades
```

---

## ✅ Requirements 

- Python 3.8+
- Standard Python libraries (json, os, etc.)

---

## 🤝 Contributing

Any suggestions or improvements are welcome!

---

## License

This project is licensed under the MIT License.
