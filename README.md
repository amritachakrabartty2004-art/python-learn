# 🎓 Student CGPA Calculator Pro (Vercel Ready)

A premium, modern, and feature-rich CGPA calculator designed for students. This project is **fully optimized for Vercel deployment** with a high-end Web UI and a robust Python Command Line Interface.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Vercel](https://img.shields.io/badge/Deploy-Vercel-black?style=for-the-badge&logo=vercel)
![UI](https://img.shields.io/badge/Design-Glassmorphism-pink?style=for-the-badge)

---

## 🌟 Key Features

### 1. 🚀 Premium Web UI (Vercel Optimized)
- **Glassmorphic Design**: Modern, sleek interface with blur effects and vibrant gradients.
- **Real-time Calculation**: CGPA and Percentage update instantly as you type.
- **Responsive**: Works perfectly on mobile and desktop.
- **Export Feature**: Generate and save a structured `.txt` report directly from the browser.

### 2. 💻 Python CLI Version
- Pure Python implementation included for terminal use.
- Robust input validation and backlog detection module.

---

## 🚀 Deployment & Usage

### 🌎 Deploy to Vercel (Live Web App)
1. Push this project to your GitHub repository.
2. Go to **[Vercel.com](https://vercel.com)**.
3. Click "New Project" and import your repository.
4. Click **Deploy**. Vercel will automatically detect `index.html` and your site will be LIVE!

### 💻 Run Locally (CLI Version)
For the command-line experience:
```powershell
py .\student_cgpa_calculator.py
```

---

## 🛠️ Project Structure

```text
├── index.html                  # Main Web UI (Root for Vercel)
├── style.css                   # Premium Glassmorphism styling
├── script.js                   # Real-time calculation logic
├── student_cgpa_calculator.py  # Python CLI Version
└── README.md                   # Project documentation
```

---

## 📊 Grade Mapping Logic
Uses standard 10-point scale (O=10, A+=9, ..., F=0).
Formula: $CGPA = \frac{\sum(\text{Credit} \times \text{GradePoint})}{\sum(\text{Credits})}$
Percentage: $CGPA \times 9.5$

---

Developed for Student Excellence.

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