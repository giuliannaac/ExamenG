import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
file_path = "university_student_dashboard_data.csv"
df = pd.read_csv(file_path)

# Title
st.title("University Admissions & Student Satisfaction Dashboard")

# Metrics Section
st.header("Key Admissions Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Applications", df["Applications"].sum())
col2.metric("Total Admissions", df["Admitted"].sum())
col3.metric("Total Enrollments", df["Enrolled"].sum())

# Admissions Trends
st.subheader("Admissions Over Time")
fig_applications = px.line(df, x="Year", y=["Applications", "Admitted", "Enrolled"], color_discrete_map={"Applications": "blue", "Admitted": "green", "Enrolled": "red"})
st.plotly_chart(fig_applications)

# Retention Rate Trends
st.subheader("Retention Rate Over Time")
fig_retention = px.line(df, x="Year", y="Retention Rate (%)", markers=True, title="Retention Rate Trends")
st.plotly_chart(fig_retention)

# Student Satisfaction Trends
st.subheader("Student Satisfaction Over Time")
fig_satisfaction = px.line(df, x="Year", y="Student Satisfaction (%)", markers=True, title="Student Satisfaction Trends")
st.plotly_chart(fig_satisfaction)

# Enrollment Breakdown by Department
st.subheader("Departmental Enrollment Trends")
department_cols = ["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]
fig_departments = px.line(df, x="Year", y=department_cols, title="Enrollment by Department")
st.plotly_chart(fig_departments)

# Spring vs. Fall Trends
st.subheader("Comparison of Spring vs. Fall Enrollment")
fig_term_comparison = px.bar(df, x="Year", y="Enrolled", color="Term", barmode="group", title="Spring vs. Fall Enrollment Trends")
st.plotly_chart(fig_term_comparison)

