# 🚀 StudentPredictor AI — Academic Success Forecaster

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=24&color=6366F1&center=true&vCenter=true&width=800&lines=Predict+Student+Performance+with+AI;Data-Driven+Insights+for+Education;Built+with+Machine+Learning+%26+Flask;Early+Warning+System+for+Academic+Success" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/Washim-8/StudentPredictorAI-Student-Performer-Predictor?style=for-the-badge&color=6366f1" />
  <img src="https://img.shields.io/github/forks/Washim-8/StudentPredictorAI-Student-Performer-Predictor?style=for-the-badge&color=10b981" />
  <img src="https://img.shields.io/github/issues/Washim-8/StudentPredictorAI-Student-Performer-Predictor?style=for-the-badge&color=f59e0b" />
  <img src="https://img.shields.io/badge/Maintained%3F-yes-6366f1?style=for-the-badge" />
</p>

---

## 📌 Overview

**StudentPredictor AI** is a smart machine learning-powered web application that predicts student performance based on academic and behavioral data.  

In most educational systems, identifying struggling students happens too late—after results are already out. This project tackles that gap by offering **early insights** using data like attendance, study habits, and past performance.  

Instead of guesswork, it provides **instant, data-backed predictions**—helping educators take timely actions and students improve proactively. It transforms raw metrics into a roadmap for academic success.

---

## ✨ Features

- **🎯 Accurate Performance Prediction**  
  Classifies students as *High*, *Average*, or *Low performers* using trained ML models like Random Forest.

- **📊 Interactive Analytics Dashboard**  
  Visual insights powered by **Chart.js** to help understand trends, performance distributions, and feature correlations.

- **⚡ Real-Time Predictions**  
  Get instant results with a confidence score and a modern count-up gauge animation.

- **💡 Actionable Insights**  
  The system doesn't just give a label; it provides tailored suggestions to help students bridge the gap.

- **🌐 REST API Support**  
  Built-in support for programmatic access, making it easy to integrate with existing School Management Systems.

- **🎨 Premium UI/UX**  
  A modern, "Glassmorphic" interface that is clean, responsive, and visually engaging.

---

## 🛠 Tech Stack

### 💻 Core Technologies
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) ![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=flat-square&logo=jinja&logoColor=white)

### 🤖 Machine Learning
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat-square&logo=numpy&logoColor=white)

### 🌐 Frontend & Visualization
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) ![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat-square&logo=chartdotjs&logoColor=white)

---

## 📂 Project Structure

```bash
├── static/              # Assets and design system
│   ├── css/             # Glassmorphic light theme styles
│   └── js/              # UI logic and Chart.js integration
├── templates/           # Jinja2 HTML templates
│   ├── index.html       # Main prediction form
│   ├── result.html      # Prediction result showcase
│   └── dashboard.html   # Visual analytics hub
├── model/               # Trained artifacts (.pkl models & scalers)
├── dataset/             # Source training data (students.csv)
├── app.py               # Flask backend & API routes
└── requirements.txt     # Project dependencies
```

---

## ⚙️ How It Works

1.  **Input Data**: Enter student details like attendance, internal marks, study hours, previous CGPA, etc.
2.  **Processing**: The system validates inputs and scales them using a pre-trained **StandardScaler**.
3.  **Prediction**: A **Random Forest** model analyzes the features to categorize the student's performance level.
4.  **Visualization**: Results are displayed with a confidence score and advice, while the dashboard provides a birds-eye view of student data.

---

## ▶️ Installation & Setup

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Washim-8/StudentPredictorAI-Student-Performer-Predictor.git
cd StudentPredictorAI-Student-Performer-Predictor
```

2️⃣ **Set Up Virtual Environment**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Launch Application**
```bash
python app.py
```
Open `http://127.0.0.1:5000` in your browser.

---

## 📸 Screenshots / Demo

> [!NOTE]
> Add your high-resolution screenshots in the `/assets` or `/docs` folder to showcase the UI.

**💡 Demo GIF Ideas:**
- A screen recording of the form being filled and the result page "popping in."
- The confidence gauge counting up to the percentage.
- Navigating through the interactive charts in the Dashboard.

---

## 🚀 Future Improvements

- [ ] **Advanced Deep Learning**: Integrate Neural Networks for identifying complex behavioral patterns.
- [ ] **Classroom Bulk Upload**: Support CSV uploads to predict performance for entire batches at once.
- [ ] **PDF Reports**: Generate and download professional academic recommendation reports.
- [ ] **Cloud Deployment**: Deploy on AWS/Azure with a scalable database backend.
- [ ] **Mobile Integration**: Develop a lightweight React Native app for teachers on the go.

---

## 👨‍💻 Author

### **Washim Shaikh**
*Aspiring Software Engineer*

I am a Computer Science Engineering student who is deeply passionate about building systems that solve real-world problems. My work sits at the intersection of robust software development and intelligent systems—whether I'm building platforms for farmers, engineering AI-driven tools, or exploring machine learning applications.

I have a strong interest in AI/ML, Prompt Engineering, and building practical applications in domains like agriculture, finance, and automation. My portfolio includes real-world systems like **AgriTrade** (a farmer auction platform), **AI Chatbots**, and **Fraud Detection models**.

With hands-on experience through internships in AI, Machine Learning, Full Stack Development, and AWS, I enjoy turning complex ideas into intuitive, working products.

**🔧 Technical Arsenal:**
- **Languages**: Python, Java, C, C++, PHP
- **Web**: HTML, CSS, JavaScript, Django, Flask
- **Data**: MySQL, Data Analysis, Machine Learning
- **Tools**: Git, GitHub, VS Code, AWS

---

## 📬 Contact

I'm always open to discussing new projects, creative ideas, or opportunities to be part of your visions.

- 📧 **Email**: [washimshaikh33@gmail.com](mailto:washimshaikh33@gmail.com)
- 📱 **Phone**: +91 8884958185
- 💻 **GitHub**: [Washim-8](https://github.com/Washim-8)
- 🔗 **LinkedIn**: [Washim Shaikh](https://www.linkedin.com/in/washim-shaikh-349868281/)

👉 **Feel free to connect for collaborations or opportunities!**

---

## 📊 GitHub Stats
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Washim-8&show_icons=true&theme=tokyonight&border_radius=10" alt="Washim's GitHub Stats" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Washim-8&theme=tokyonight&border_radius=10" alt="GitHub Streak" />
</p>

---

### ⭐ Support

If you found this project useful, consider giving it a **Star** on GitHub! It helps more people find the project.

*© 2026 StudentPredictor AI — Built with passion by Washim Shaikh*
