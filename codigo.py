# Agrupar por 'Year' y 'Term' y sumar las columnas relevantes
summary_df = datos.groupby(['Year', 'Term'])[['Applications', 'Admitted', 'Enrolled']].sum().reset_index()

# Crear una gráfica de líneas para visualizar la tendencia de aplicaciones, admisiones e inscripciones por término
plt.figure(figsize=(12, 6))

# Graficar cada métrica
for col in ['Applications', 'Admitted', 'Enrolled']:
    plt.plot(summary_df['Year'].astype(str) + " " + summary_df['Term'], summary_df[col], marker='o', linestyle='-', label=col)

# Configuración de la gráfica
plt.xticks(rotation=45, ha='right')
plt.xlabel("Year Term")
plt.ylabel("Count")
plt.title("Applications, Admissions, and Enrollments Over Time")
plt.legend()
plt.grid(True)

datos_sorted = datos.sort_values(by=['Year', 'Term'])

    # Crear la gráfica de tendencia de Retention Rate
plt.figure(figsize=(10, 5))
plt.plot(datos_sorted['Year'].astype(str) + " " + datos_sorted['Term'], datos_sorted['Retention Rate (%)'], marker='o', linestyle='-')
plt.xticks(rotation=45, ha='right')
plt.xlabel("Year Term")
plt.ylabel("Retention Rate (%)")
plt.title("Retention Rate Trend Over Time")
plt.grid(True)

# Ordenar los datos por 'Year' y 'Term' para una visualización adecuada
datos_sorted = datos.sort_values(by=['Year', 'Term'])

# Crear la gráfica de tendencia de Student Satisfaction
plt.figure(figsize=(10, 5))
plt.plot(datos_sorted['Year'].astype(str) + " " + datos_sorted['Term'],
         datos_sorted['Student Satisfaction (%)'], marker='o', linestyle='-', color='r')

# Configuración de la gráfica
plt.xticks(rotation=45, ha='right')
plt.xlabel("Year Term")
plt.ylabel("Student Satisfaction (%)")
plt.title("Student Satisfaction Trend Over Time")
plt.grid(True)

# Seleccionar las columnas de inscripción por departamento
enrollment_columns = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']

# Sumar las inscripciones por departamento
enrollment_summary = datos[enrollment_columns].sum().reset_index()
enrollment_summary.columns = ['Department', 'Total Enrollment']

# Crear gráfico de barras para visualizar la distribución de inscripciones por departamento
plt.figure(figsize=(8, 5))
plt.bar(enrollment_summary['Department'], enrollment_summary['Total Enrollment'], color=['blue', 'green', 'red', 'purple'])

plt.xlabel("Department")
plt.ylabel("Total Enrollment")
plt.title("Enrollment Breakdown by Department")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Filtrar datos para los términos Spring y Fall
spring_data = datos[datos['Term'] == 'Spring'].sort_values(by=['Year'])
fall_data = datos[datos['Term'] == 'Fall'].sort_values(by=['Year'])

# Crear figura para comparar tendencias
plt.figure(figsize=(10, 5))

# Graficar tendencias para Retention Rate
plt.plot(spring_data['Year'], spring_data['Retention Rate (%)'], marker='o', linestyle='-', color='b', label="Spring Retention Rate")
plt.plot(fall_data['Year'], fall_data['Retention Rate (%)'], marker='s', linestyle='--', color='r', label="Fall Retention Rate")

# Configuración del gráfico
plt.xlabel("Year")
plt.ylabel("Retention Rate (%)")
plt.title("Spring vs Fall Term Retention Rate Trends")
plt.legend()
plt.grid(True)

# Seleccionar las columnas necesarias
departments = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']

# Crear una figura
plt.figure(figsize=(10, 5))

# Graficar Retention Rate para cada departamento
for dept in departments:
    plt.plot(datos['Year'], datos['Retention Rate (%)'] * (datos[dept] / datos[departments].sum(axis=1)),
             marker='o', linestyle='-', label=f"Retention - {dept}")

# Graficar Satisfaction Rate para cada departamento
for dept in departments:
    plt.plot(datos['Year'], datos['Student Satisfaction (%)'] * (datos[dept] / datos[departments].sum(axis=1)),
             marker='s', linestyle='--', label=f"Satisfaction - {dept}")

# Configuración de la gráfica
plt.xlabel("Year")
plt.ylabel("Percentage (%)")
plt.title("Comparison of Retention Rates and Satisfaction Levels Across Departments")
plt.legend()
plt.grid(True)

