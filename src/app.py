import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

st.set_page_config(
    page_title="College Placement Intelligence",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #f5f7ff, #eef2ff);
}
.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #243b80;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}
.section-title {
    color: #243b80;
    font-size: 25px;
    font-weight: bold;
    margin-top: 20px;
}
.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}
.metric-title {
    color: #555;
    font-size: 16px;
}
.metric-value {
    color: #243b80;
    font-size: 28px;
    font-weight: bold;
}
.prediction-card {
    padding: 25px;
    border-radius: 18px;
    background: white;
    text-align: center;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
}
div.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 48px;
    font-size: 17px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🎓 College Placement Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Student Performance & Placement Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">📝 Student Academic Details</div>',
    unsafe_allow_html=True
)

st.info("Please enter all student details to generate the performance dashboard.")

with st.form("student_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        cgpa = st.number_input(
            "🎓 CGPA",
            min_value=0.0,
            max_value=10.0,
            value=None,
            placeholder="Enter CGPA",
            step=0.01
        )

        tenth = st.number_input(
            "📚 10th Percentage",
            min_value=0.0,
            max_value=100.0,
            value=None,
            placeholder="Enter 10th percentage",
            step=0.1
        )

        twelfth = st.number_input(
            "📖 12th Percentage",
            min_value=0.0,
            max_value=100.0,
            value=None,
            placeholder="Enter 12th percentage",
            step=0.1
        )

        attendance = st.number_input(
            "🕒 Attendance Percentage",
            min_value=0.0,
            max_value=100.0,
            value=None,
            placeholder="Enter attendance percentage",
            step=0.1
        )

    with col2:
        aptitude = st.number_input(
            "🧠 Aptitude Score",
            min_value=0,
            max_value=100,
            value=None,
            placeholder="Enter aptitude score",
            step=1
        )

        coding = st.number_input(
            "💻 Coding Score",
            min_value=0,
            max_value=100,
            value=None,
            placeholder="Enter coding score",
            step=1
        )

        communication = st.number_input(
            "🗣️ Communication Score",
            min_value=0,
            max_value=100,
            value=None,
            placeholder="Enter communication score",
            step=1
        )

        backlogs = st.number_input(
            "📕 Number of Backlogs",
            min_value=0,
            max_value=20,
            value=None,
            placeholder="Enter number of backlogs",
            step=1
        )

    with col3:
        internship = st.selectbox(
            "💼 Internship Experience",
            options=["Select", "Yes", "No"]
        )

        certifications = st.number_input(
            "📜 Number of Certifications",
            min_value=0,
            max_value=20,
            value=None,
            placeholder="Enter number of certifications",
            step=1
        )

        projects = st.number_input(
            "🚀 Number of Projects",
            min_value=0,
            max_value=20,
            value=None,
            placeholder="Enter number of projects",
            step=1
        )

    st.write("")

    col_predict, col_clear = st.columns(2)

    with col_predict:
        submitted = st.form_submit_button(
            "🤖 Predict Placement",
            type="primary"
        )

    with col_clear:
        clear_all = st.form_submit_button(
            "🧹 Clear All"
        )

if clear_all:
    st.rerun()

if submitted:

    if (
        cgpa is None
        or tenth is None
        or twelfth is None
        or attendance is None
        or aptitude is None
        or coding is None
        or communication is None
        or backlogs is None
        or certifications is None
        or projects is None
        or internship == "Select"
    ):
        st.error("⚠️ Please fill all the student details before prediction.")

    else:

        internship_value = 1 if internship == "Yes" else 0

        academic_score = (tenth + twelfth + (cgpa * 10)) / 3

        technical_score = (
            aptitude + coding + communication
        ) / 3

        internship_score = 10 if internship_value == 1 else 0

        overall_performance = (
            academic_score * 0.40
            + technical_score * 0.35
            + attendance * 0.10
            + internship_score * 0.05
            + certifications * 0.05
            + projects * 0.05
        )

        overall_performance = min(100, max(0, overall_performance))

        np.random.seed(42)

        X_train = np.random.rand(300, 10)

        y_train = (
            X_train[:, 0] * 0.25
            + X_train[:, 1] * 0.15
            + X_train[:, 2] * 0.15
            + X_train[:, 3] * 0.10
            + X_train[:, 4] * 0.10
            + X_train[:, 5] * 0.10
            + X_train[:, 6] * 0.05
            + X_train[:, 7] * 0.05
            + X_train[:, 8] * 0.025
            + X_train[:, 9] * 0.025
            > 0.50
        ).astype(int)

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)

        model = LogisticRegression()
        model.fit(X_train_scaled, y_train)

        student_data = np.array([[
            cgpa / 10,
            tenth / 100,
            twelfth / 100,
            attendance / 100,
            aptitude / 100,
            coding / 100,
            communication / 100,
            min(backlogs / 10, 1),
            certifications / 10,
            projects / 10
        ]])

        student_scaled = scaler.transform(student_data)

        probability = model.predict_proba(student_scaled)[0][1] * 100

        probability = (
            probability * 0.30
            + overall_performance * 0.70
        )

        if backlogs > 0:
            probability -= backlogs * 3

        if internship_value == 1:
            probability += 5

        probability = min(99, max(1, probability))

        if probability >= 50:
            result = "Likely to be Placed"
            result_icon = "🎉"
        else:
            result = "Needs Improvement"
            result_icon = "📈"

        st.markdown(
            '<div class="section-title">📊 Student Performance Dashboard</div>',
            unsafe_allow_html=True
        )

        st.success("✅ Student details processed successfully!")

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">🎓 CGPA</div>
                <div class="metric-value">{cgpa:.2f}/10</div>
            </div>
            """, unsafe_allow_html=True)

        with m2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">📚 Academic Score</div>
                <div class="metric-value">{academic_score:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)

        with m3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">💻 Technical Score</div>
                <div class="metric-value">{technical_score:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)

        with m4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">⭐ Overall Performance</div>
                <div class="metric-value">{overall_performance:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### 📈 Performance Comparison")

        chart_data = pd.DataFrame({
            "Category": [
                "10th %",
                "12th %",
                "Aptitude",
                "Attendance",
                "CGPA",
                "Coding",
                "Communication",
                "Certifications",
                "Projects"
            ],
            "Score": [
                tenth,
                twelfth,
                aptitude,
                attendance,
                cgpa * 10,
                coding,
                communication,
                min(certifications * 10, 100),
                min(projects * 10, 100)
            ]
        })

        st.bar_chart(chart_data.set_index("Category"))

        st.markdown("### 🤖 AI Placement Prediction")

        st.markdown(f"""
        <div class="prediction-card">
            <h1 style="color: black;">{result_icon} {result}</h1>
            <h2 style="color: black;">Placement Probability: {probability:.1f}%</h2>
            <p>Based on academic performance, technical skills and student profile.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🔍 Skill Gap Analysis")

        gaps = []

        if cgpa < 7:
            gaps.append("Improve CGPA")
        if aptitude < 60:
            gaps.append("Practice aptitude questions")
        if coding < 60:
            gaps.append("Improve coding skills")
        if communication < 60:
            gaps.append("Improve communication skills")
        if attendance < 75:
            gaps.append("Improve attendance")
        if certifications == 0:
            gaps.append("Complete at least one certification")
        if projects == 0:
            gaps.append("Build practical projects")
        if internship == "No":
            gaps.append("Gain internship experience")

        if gaps:
            for gap in gaps:
                st.warning("• " + gap)
        else:
            st.success("🌟 Excellent! No major skill gaps identified.")

        st.markdown("### 📝 Personalized Improvement Plan")

        if probability < 50:
            st.info("""
            1. Practice aptitude questions daily  
            2. Improve coding and problem-solving skills  
            3. Work on communication skills  
            4. Complete real-world projects  
            5. Gain internship experience  
            """)
        else:
            st.success("""
            1. Continue improving technical skills  
            2. Prepare for placement interviews  
            3. Practice HR and aptitude questions  
            4. Build a strong resume  
            5. Attend mock interviews  
            """)

st.markdown("---")

st.markdown(
    "<center>🎓 College Placement Intelligence & Prediction System<br>"
    "Built using Python, Machine Learning and Streamlit</center>",
    unsafe_allow_html=True
)
