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
plt.show()
