# 🎓 College Placement Intelligence & Prediction System

An AI-powered machine learning system designed to analyze student academic and skill-related data, predict placement outcomes, identify skill gaps, and provide personalized recommendations to improve placement readiness.

## 🚀 Project Overview

The **College Placement Intelligence & Prediction System** helps students and placement teams make data-driven decisions by combining student performance data with machine learning.

The system predicts whether a student is likely to be placed and provides a placement probability, skill-gap analysis, overall placement readiness score, and actionable recommendations.

## 🎯 Objectives

* Predict student placement outcomes using Machine Learning
* Estimate placement probability
* Analyze student skill gaps
* Calculate overall placement readiness
* Provide personalized improvement recommendations
* Support data-driven placement preparation
* Provide an easy-to-use web interface

## ✨ Key Features

### 🎯 Placement Prediction

Predicts whether a student is likely to be:

* ✅ Placed
* ❌ Not Placed

The system also provides a **placement probability score**.

### 📊 Skill Gap Analysis

Analyzes important placement-related skills such as:

* SQL
* Python
* Power BI
* Communication
* Aptitude

The system highlights areas where students need improvement.

### 💡 Personalized Recommendations

Based on the student's performance and skill levels, the system provides recommendations such as:

* Practice SQL interview questions
* Improve communication skills
* Strengthen Power BI/DAX knowledge
* Attend mock interviews
* Practice aptitude regularly

### 📈 Placement Readiness Score

The system calculates an overall readiness score and classifies the student's placement preparedness.

Example:

```text
Placement Readiness Score: 78/100
Readiness Level: GOOD
```

### 🖥️ Interactive Web Application

The project provides a simple web interface where student information can be entered and the prediction results can be viewed instantly.

## 🧠 Machine Learning Workflow

```text
Student Data
     ↓
Data Preprocessing
     ↓
Feature Selection
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Placement Prediction
     ↓
Skill Gap Analysis
     ↓
Recommendations
     ↓
Placement Readiness Score
```

## 🛠️ Technologies Used

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python       | Data processing and ML              |
| Pandas       | Data manipulation                   |
| NumPy        | Numerical operations                |
| Scikit-learn | Machine Learning                    |
| Streamlit    | Web application                     |
| SQL          | Student/placement data management   |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
College-Placement-Intelligence/
│
├── app.py
├── model/
├── data/
├── notebooks/
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact folder structure may vary depending on the final project files.

## 📋 Sample Output

```text
COLLEGE PLACEMENT INTELLIGENCE

Student ID       : STU1024
CGPA             : 8.29
Skills           : Python, SQL, Power BI
Internship       : Yes
Projects         : 2
Aptitude Score   : 78
Communication    : 72
Attendance       : 91%

PLACEMENT PREDICTION
Prediction       : PLACED
Probability      : 87.4%

SKILL GAP ANALYSIS

SQL              : 90%
Python            : 80%
Power BI          : 70%
Communication    : 60%
Aptitude          : 80%

PLACEMENT READINESS

Overall Score    : 78/100
Readiness        : GOOD
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vaishnavi-da36/College-Placement-Intelligence.git
```

### 2. Navigate to the Project

```bash
cd College-Placement-Intelligence
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser through the local Streamlit server.

## 📊 Example Use Case

A placement cell can use this system to:

1. Enter student academic and skill information
2. Predict placement probability
3. Identify students who need additional preparation
4. Analyze skill gaps
5. Provide targeted recommendations
6. Monitor overall placement readiness

## 🔮 Future Enhancements

* AI-powered career recommendations
* Company-specific placement prediction
* Job description and skill matching
* Resume analysis
* Interview preparation assistant
* Advanced NLP-based skill extraction
* Placement analytics dashboard
* Cloud deployment
* Real-time placement data integration

## 👩‍💻 Developer

**Vaishnavi R**
B.Tech Artificial Intelligence & Data Science

**Focus:** Data Analytics | Machine Learning | Python | SQL | Power BI

## 📌 Project Status

**Status: Completed ✅**

This project demonstrates the practical use of **Machine Learning, Data Analytics, and an interactive web application** for solving a real-world college placement intelligence problem.
