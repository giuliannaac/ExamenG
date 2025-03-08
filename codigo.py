import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "university_student_dashboard_data.csv"
datos = pd.read_csv(file_path)

st.title("University Admissions & Student Satisfaction Dashboard")

# Agrupar por 'Year' y 'Term' y sumar las columnas relevantes
summary_df = datos.groupby(['Year', 'Term'])[['Applications', 'Admitted', 'Enrolled']].sum().reset_index()

# Crear una gráfica de líneas para visualizar la tendencia de aplicaciones, admisiones e inscripciones por término
st.subheader("Applications, Admissions, and Enrollments Over Time")
fig, ax = plt.subplots(figsize=(12, 6))
for col in ['Applications', 'Admitted', 'Enrolled']:
    ax.plot(summary_df['Year'].astype(str) + " " + summary_df['Term'], summary_df[col], marker='o', linestyle='-', label=col)
ax.set_xticklabels(summary_df['Year'].astype(str) + " " + summary_df['Term'], rotation=45, ha='right')
ax.set_xlabel("Year Term")
ax.set_ylabel("Count")
ax.set_title("Applications, Admissions, and Enrollments Over Time")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Gráfica de tendencia de Retention Rate
datos_sorted = datos.sort_values(by=['Year', 'Term'])
st.subheader("Retention Rate Trend Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(datos_sorted['Year'].astype(str) + " " + datos_sorted['Term'], datos_sorted['Retention Rate (%)'], marker='o', linestyle='-')
ax.set_xticklabels(datos_sorted['Year'].astype(str) + " " + datos_sorted['Term'], rotation=45, ha='right')
ax.set_xlabel("Year Term")
ax.set_ylabel("Retention Rate (%)")
ax.set_title("Retention Rate Trend Over Time")
ax.grid(True)
st.pyplot(fig)

# Gráfica de tendencia de Student Satisfaction
st.subheader("Student Satisfaction Trend Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(datos_sorted['Year'].astype(str) + " " + datos_sorted['Term'], datos_sorted['Student Satisfaction (%)'], marker='o', linestyle='-', color='r')
ax.set_xticklabels(datos_sorted['Year'].astype(str) + " " + datos_sorted['Term'], rotation=45, ha='right')
ax.set_xlabel("Year Term")
ax.set_ylabel("Student Satisfaction (%)")
ax.set_title("Student Satisfaction Trend Over Time")
ax.grid(True)
st.pyplot(fig)

# Inscripciones por departamento
enrollment_columns = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']
enrollment_summary = datos[enrollment_columns].sum().reset_index()
enrollment_summary.columns = ['Department', 'Total Enrollment']

st.subheader("Enrollment Breakdown by Department")
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(enrollment_summary['Department'], enrollment_summary['Total Enrollment'], color=['blue', 'green', 'red', 'purple'])
ax.set_xlabel("Department")
ax.set_ylabel("Total Enrollment")
ax.set_title("Enrollment Breakdown by Department")
ax.set_xticklabels(enrollment_summary['Department'], rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Comparación de Retention Rate entre Spring y Fall
spring_data = datos[datos['Term'] == 'Spring'].sort_values(by=['Year'])
fall_data = datos[datos['Term'] == 'Fall'].sort_values(by=['Year'])

st.subheader("Spring vs Fall Term Retention Rate Trends")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(spring_data['Year'], spring_data['Retention Rate (%)'], marker='o', linestyle='-', color='b', label="Spring Retention Rate")
ax.plot(fall_data['Year'], fall_data['Retention Rate (%)'], marker='s', linestyle='--', color='r', label="Fall Retention Rate")
ax.set_xlabel("Year")
ax.set_ylabel("Retention Rate (%)")
ax.set_title("Spring vs Fall Term Retention Rate Trends")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Instrucciones para subir a GitHub
st.subheader("Deploy on GitHub with SmartLib")
st.markdown("""
### Steps to Deploy on GitHub:
1. **Create a GitHub Repository**: Name it `university-dashboard`.
2. **Upload This Script**: Save this script as `app.py` and push it to GitHub.
3. **Create a `requirements.txt` File**: Add the following dependencies:
   ```
   streamlit
   pandas
   matplotlib
   ```
4. **Deploy Using Streamlit Cloud**:
   - Go to [Streamlit Cloud](https://share.streamlit.io/)
   - Connect your GitHub repository
   - Select `app.py` as the main file
   - Deploy!
""")
