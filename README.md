# 🚀 StudentPredictor AI — Academic Success Forecaster

[![Stars](https://img.shields.io/github/stars/Washim-8/StudentPredictorAI-Student-Performer-Predictor?style=for-the-badge&color=6366f1)](https://github.com/Washim-8/StudentPredictorAI-Student-Performer-Predictor)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

## 📌 Overview

**StudentPredictor AI** is a high-performance machine learning application designed to bridge the gap between student metrics and academic outcomes. In today's fast-paced educational environment, identifying students who might need extra support or those who are excelling is often done too late. 

This project solves that problem by analyzing key variables—like attendance, study habits, and previous grades—to provide an instant, data-driven prediction of a student's performance level (High, Average, or Low). It’s not just a calculator; it’s an early-warning system built to help educators and students make proactive decisions before the final exams.

---

## ✨ Features

- **🎯 Precision ML Engine**: Leverages a ensemble of models (including Random Forest and SVM) to deliver predictions with documented high accuracy.
- **📊 Real-time Dashboard**: Interactive visualization using **Chart.js** to show distribution patterns and performance averages across the entire dataset.
- **💎 Premium Glassmorphic UI**: A modern, light-themed interface with smooth transitions, responsive layouts, and high-impact micro-animations.
- **⚡ Count-Up Confidence Gauge**: A custom circular visualization that counts up to the model's confidence level using spring-physics animations.
- **💡 Actionable Insights**: Beyond just a "Low" or "High" result, the system provides tailored advice to help students improve.
- **🌐 RESTful API Support**: Built-in API endpoints for external systems to send metrics and receive JSON-formatted predictions.

---

## 🛠 Tech Stack

| Category | Technologies |
| :--- | :--- |
| **Backend** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) |
| **Machine Learning**| ![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) ![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) |
| **Visualization** | ![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat&logo=chartdotjs&logoColor=white) |
| **Tools** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) ![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=flat&logo=visual-studio-code&logoColor=white) |

---

## 📂 Project Structure

```bash
├── static/              # CSS, JS, and Images
│   ├── css/style.css    # Premium light theme styles
│   └── js/main.js       # Form logic & animations
├── templates/           # HTML Templates (Jinja2)
│   ├── index.html       # Prediction form
│   ├── result.html      # Glassmorphic results page
│   └── dashboard.html   # Chart.js analytics
├── model/               # Trained artifacts (.pkl files)
├── dataset/             # Training data (students.csv)
├── app.py               # Main Flask application
└── requirements.txt     # Dependency list
```

---

## ⚙️ How It Works

1.  **Data Collection**: The user inputs 6 key metrics: Attendance, Internal Marks, Study Hours, Previous CGPA, Assignments, and Extracurricular participation.
2.  **Preprocessing**: The input is validated in real-time and passed to a pre-trained **StandardScaler** to normalize the values.
3.  **Classification**: The **Random Forest** (or selected ensemble) model processes the scaled vector.
4.  **Inference**: The model returns a classification and a probability score (Confidence).
5.  **Dynamic Rendering**: The UI animates the results page, popping in information chips and drawing the confidence gauge based on the fresh data.

---

## ▶️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Washim-8/StudentPredictorAI-Student-Performer-Predictor.git
    cd StudentPredictorAI-Student-Performer-Predictor
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    python app.py
    ```
    Visit `http://127.0.0.1:5000` in your browser.

---

## 📸 Screenshots & Demo

> [!TIP]
> **GIF Idea**: Showcase the transition from the form to the result page, highlighting the count-up gauge and the pop-in chips.

*(Add your high-res screenshots here targeting the Results and Dashboard views)*

---

## 🚀 Future Improvements

- [ ] **Multi-Model Comparison**: Allow users to switch between different ML algorithms (e.g., XGBoost vs SVM) in the UI.
- [ ] **Export to PDF**: Generate a professional academic report for students to download.
- [ ] **Bulk Upload**: Predict performance for an entire classroom via CSV upload.
- [ ] **Deep Learning Integration**: Implement a neural network using TensorFlow/PyTorch for more complex behavioral mapping.

---

## 👨‍💻 Author

### Washim Shaikh
**Aspiring Software Engineer**

I am a Computer Science Engineering student with a focus on building systems that solve real-world problems. Whether it's developing e-auction platforms for farmers (**AgriTrade**), engineering intelligent **AI Chatbots**, or building high-precision **Fraud Detection Systems**, I am passionate about the intersection of elegant code and practical AI.

My experience spans internships with **Coincent (AI)**, **Yhills (ML)**, and **iStudio (AWS)**, which has given me a deep understanding of software end-to-end—from data analysis and model training to full-stack web deployment. I believe technology should be efficient, accessible, and visually stunning.

**Key Skills:**
- **Languages**: Python, Java, C, C++, PHP
- **Frameworks**: Django, Flask, Full Stack Web
- **Intelligence**: Machine Learning, Data Analysis, Prompt Engineering
- **Database**: MySQL

---

## 📬 Contact

Feel free to connect for collaborations, opportunities, or just to talk tech!

- ✉️ **Email**: [washimshaikh33@gmail.com](mailto:washimshaikh33@gmail.com)
- 📱 **Phone**: +91 88849 58185
- 💻 **GitHub**: [github.com/Washim-8](https://github.com/Washim-8)
- 🔗 **LinkedIn**: [Washim Shaikh](https://www.linkedin.com/in/washim-shaikh-349868281/)

---
*© 2026 StudentPredictor AI — Designed & Built with ❤️ by Washim Shaikh*

---
