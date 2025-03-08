import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# 📌 Título del Dashboard
st.title("📊 University Student Trends Dashboard")

# 🚀 Cargar datos desde GitHub
url = "https://raw.githubusercontent.com/giuliannaac/ExamenG/main/university_student_dashboard_data.csv"
df = pd.read_csv(url)

# ✅ Mostrar vista previa de los datos
st.write("### 🔍 Data Preview")
st.dataframe(df.head())

# 📊 Agrupar datos por 'Year' y 'Term'
summary_df = df.groupby(['Year', 'Term'])[['Applications', 'Admitted', 'Enrolled']].sum().reset_index()

# 📈 Gráfico de tendencias
st.write("### 📈 Applications, Admissions & Enrollments Over Time")

plt.figure(figsize=(12, 6))
for col in ['Applications', 'Admitted', 'Enrolled']:
    plt.plot(summary_df['Year'].astype(str) + " " + summary_df['Term'], summary_df[col], marker='o', linestyle='-', label=col)

plt.xticks(rotation=45, ha='right')
plt.xlabel("Year Term")
plt.ylabel("Count")
plt.title("Applications, Admissions, and Enrollments Over Time")
plt.legend()
plt.grid(True)

st.pyplot(plt)

# 🔑 Key Findings & Insights
st.write("### 🔑 Key Findings & Actionable Insights")
total_applications = df['Applications'].sum()
total_admitted = df['Admitted'].sum()
total_enrolled = df['Enrolled'].sum()

admission_rate = (total_admitted / total_applications) * 100 if total_applications > 0 else 0
enrollment_rate = (total_enrolled / total_admitted) * 100 if total_admitted > 0 else 0

st.write(f"✅ **Total Applications:** {total_applications:,}")
st.write(f"✅ **Total Admitted:** {total_admitted:,} ({admission_rate:.2f}% Admission Rate)")
st.write(f"✅ **Total Enrolled:** {total_enrolled:,} ({enrollment_rate:.2f}% Enrollment Rate)")

# ⚠️ Alertas y recomendaciones
if admission_rate < 50:
    st.warning("⚠️ The admission rate is below 50%. Consider analyzing admission criteria.")
if enrollment_rate < 60:
    st.warning("⚠️ Enrollment rate is low. More engagement may be needed for admitted students.")

st.success("📊 Use this data to improve student recruitment and retention strategies!")
