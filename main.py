import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Definir las etapas y sus actividades
etapas = [
  ("Primera Etapa", [
      ("Reunión inicial de trabajo", 1, 1),
      ("Confección y entrega del cronograma", 2, 4),
      ("Investigación y Desarrollo", 5, 11),
      ("Revisión Interna", 5, 11),
      ("Revisión con el Tribunal Constitucional", 12, 14)
  ]),
  ("Segunda Etapa", [
      ("Análisis y Poblamiento (25%)", 15, 44),
      ("Control de Calidad", 15, 44),
      ("Entrega de Reporte", 15, 44),
      ("Reunión de revisión", 15, 44)
  ]),
  ("Tercera Etapa", [
      ("Análisis y Poblamiento (50%)", 45, 74),
      ("Control de Calidad", 45, 74),
      ("Entrega de Reporte", 45, 74),
      ("Reunión de revisión", 45, 74)
  ]),
  ("Cuarta Etapa", [
      ("Análisis y Poblamiento (75%)", 75, 104),
      ("Control de Calidad", 75, 104),
      ("Entrega de Reporte", 75, 104),
      ("Reunión de revisión", 75, 104)
  ]),
  ("Quinta Etapa", [
      ("Análisis y Poblamiento (100%)", 105, 134),
      ("Control de Calidad", 105, 134),
      ("Entrega de Reporte", 105, 134),
      ("Reunión de revisión", 105, 134)
  ]),
  ("Sexta Etapa", [
      ("Revisión Completa", 135, 156),
      ("Corrección de Errores", 135, 156),
      ("Documentación Final", 157, 177),
      ("Reunión de Cierre", 157, 177)
  ])
]

# Colores para las actividades
colores = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666', '#66FF66']

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(12, 8))

# Iterar sobre las etapas y actividades para crear las barras
y_pos = 0
for i, (etapa, actividades) in enumerate(etapas):
  for actividad, inicio, fin in actividades:
      ax.barh(y_pos, fin - inicio + 1, left=inicio, color=colores[i % len(colores)], edgecolor='black')
      ax.text(inicio + (fin - inicio) / 2, y_pos, actividad, va='center', ha='center', color='black', fontsize=8)
      y_pos += 1
  y_pos += 0.5  # Espacio entre etapas

# Configurar el eje
ax.set_yticks([])
ax.set_xticks(range(0, 178, 10))
ax.set_xticklabels([f'Día {i}' for i in range(0, 178, 10)])
ax.set_xlim(0, 178)
ax.set_title('Carta Gantt del Plan de Trabajo', fontsize=14)
ax.set_xlabel('Días', fontsize=12)

# Crear leyenda en la parte inferior derecha
patches = [mpatches.Patch(color=colores[i], label=etapa) for i, (etapa, _) in enumerate(etapas)]
ax.legend(handles=patches, loc='lower right', bbox_to_anchor=(1, -0.2))

# Mostrar la gráfica
plt.tight_layout()
plt.show()
