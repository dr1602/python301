from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

# Definir el archivo de salida
output_file('mexico_paralympics.html')

# Datos ordenados cronológicamente
paralympic_event = [
    "Toronto 1976", "Arnhem 1980", "US 1984", "Seoul 1988", "Barcelona 1992",
    "Atlanta 1996", "Sydney 2000", "Athens 2004", "Beijing 2008", "London 2012",
    "Rio 2016", "Tokyo 2020"
]

total_gold_medals = [16, 20, 6, 8, 0, 3, 10, 14, 10, 6, 4, 7]
total_silver_medals = [14, 16, 14, 9, 1, 5, 12, 10, 3, 4, 2, 2]
total_bronze_medals = [9, 6, 17, 7, 10, 4, 12, 10, 7, 11, 9, 13]

# Crear las posiciones para las barras
x_gold = [event + " - Oro" for event in paralympic_event]
x_silver = [event + " - Plata" for event in paralympic_event]
x_bronze = [event + " - Bronce" for event in paralympic_event]

# Crear fuente de datos para Bokeh
source = ColumnDataSource(data=dict(
    events=paralympic_event,
    x_gold=x_gold,
    x_silver=x_silver,
    x_bronze=x_bronze,
    gold=total_gold_medals,
    silver=total_silver_medals,
    bronze=total_bronze_medals
))

# Crear figura
p = figure(x_range=x_gold + x_silver + x_bronze, height=400, width=800, title="Medallas Paralímpicas de México por Año",
           toolbar_location=None, tools="")

# Graficar las barras para cada tipo de medalla
p.vbar(x='x_gold', top='gold', width=0.2, source=source, legend_label="Oro", color="gold", line_color='black')
p.vbar(x='x_silver', top='silver', width=0.2, source=source, legend_label="Plata", color="silver", line_color='black')
p.vbar(x='x_bronze', top='bronze', width=0.2, source=source, legend_label="Bronce", color="#cd7f32", line_color='black')

# Configurar el gráfico
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.major_label_orientation = 1.2
p.title.text_font_size = "14pt"
p.legend.title = 'Tipo de Medalla'
p.legend.title_text_font_size = '12pt'
p.legend.label_text_font_size = '10pt'

show(p)
