# Cargar datos (ajusta la ruta según donde esté tu archivo)
df = pd.read_csv("https://github.com/giuliannaac/ExamenG/blob/main/university_student_dashboard_data.csv")

# Agrupar datos
summary_df = datos.groupby(['Year', 'Term'])[['Applications', 'Admitted', 'Enrolled']].sum().reset_index()

# Crear la gráfica
plt.figure(figsize=(12, 6))
for col in ['Applications', 'Admitted', 'Enrolled']:
    plt.plot(summary_df['Year'].astype(str) + " " + summary_df['Term'], summary_df[col], marker='o', linestyle='-', label=col)

# Configuración de la gráfica
plt.xticks(rotation=45, ha='right')
plt.xlabel("Year Term")
plt.ylabel("Count")
plt.title("Applications, Admissions, and Enrollments Over Time")
plt.legend()
plt.grid(True)

# Mostrar en Streamlit
st.pyplot(plt)
