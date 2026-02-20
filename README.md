# 🎓 Student CGPA Calculator Pro

A premium, modern, and feature-rich CGPA calculator designed for students. This project offers two ways to interact: a high-end **Web-based UI** with real-time calculations and a robust **Command Line Interface (CLI)**.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Web](https://img.shields.io/badge/Interface-Web%20%26%20CLI-purple?style=for-the-badge)
![UI](https://img.shields.io/badge/Design-Glassmorphism-pink?style=for-the-badge)

---

## 🌟 Key Features

### 1. 🚀 Premium Web UI (Recommended)
- **Glassmorphic Design**: Modern, sleek interface with blur effects and vibrant gradients.
- **Real-time Calculation**: CGPA and Percentage update instantly as you type.
- **Dynamic Management**: Add/Remove multiple semesters and subjects fluidly.
- **Visual Status**: Instant pass/fail indicators and backlog tracking.

### 2. 💻 Terminal/CLI Version
- Pure Python implementation.
- Perfect for quick calculations and understanding the logic.
- Robust input validation.

### 3. 📝 Reporting & Detection
- **Backlog Detection**: Automatically identifies and lists subjects with 'F' grades.
- **Precise Conversion**: Uses the standard formula: `Percentage = CGPA × 9.5`.
- **Export Feature**: Generate and save a structured `.txt` report of your performance.

---

## 📊 Grade Mapping Logic

| Grade | Description | Point Value |
|-------|-------------|-------------|
| **O** | Outstanding | 10 |
| **A+**| Excellent   | 9  |
| **A** | Very Good   | 8  |
| **B+**| Good        | 7  |
| **B** | Above Avg   | 6  |
| **C** | Average     | 5  |
| **F** | Fail        | 0  |

---

## 🚀 How to Run

### Option A: Launch the Web UI (The Best Experience)
Navigate to the project folder and run:
```powershell
py .\cgpa_app\run_app.py
```
*Wait for your browser to open automatically, or go to `http://localhost:8000`.*

### Option B: Run the Terminal Version
For a classic command-line experience:
```powershell
py .\student_cgpa_calculator.py
```

---

## 🛠️ Project Structure

```text
├── student_cgpa_calculator.py  # Core CLI Python Program
├── cgpa_app/
│   ├── index.html              # Modern Web UI structure
│   ├── style.css               # Premium Glassmorphism styling
│   ├── script.js               # Real-time calculation logic
│   └── run_app.py              # Local server launcher
└── README.md                   # Project documentation
```

---

## 📖 B.Tech Project Context
This project implements the standard academic formula:
$$CGPA = \frac{\sum(\text{Credit} \times \text{GradePoint})}{\sum(\text{Credits})}$$

It demonstrates skills in:
- Python Logic & Loops
- Web Technologies (HTML5, CSS3, ES6 JavaScript)
- User Experience (UX) Design
- File Handling & Exporting

---

Developed with ❤️ for Student Excellence.