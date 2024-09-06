from bokeh.plotting import figure, output_file, show
# ventatna para graficar
# determinar el nombre del archivo a generar
# para generar un servidor que muestre el html directo en el navegador

if __name__ == '__main__':
    output_file('mexico_paraolimpics.html')
    
    paralympic_event = [
        "Toronto 1976", "Arnhem 1980", "Stoke Mandeville & New York 1984",
        "Seoul 1988", "Barcelona 1992", "Atlanta 1996", "Sydney 2000",
        "Athens 2004", "Beijing 2008", "London 2012", "Rio de Janeiro 2016",
        "Tokyo 2020"
    ]

    total_gold_medals = [16, 20, 6, 8, 0, 3, 10, 14, 10, 6, 4, 7]
    total_silver_medals = [14, 16, 14, 9, 1, 5, 12, 10, 3, 4, 2, 2]
    total_bronze_medals = [9, 6, 17, 7, 10, 4, 12, 10, 7, 11, 9, 13]

    # Sorgin the graphs
    
    sorted_events = sorted( paralympic_event, key=lambda x: total_gold_medals[paralympic_event.index(x)])
    
    p = figure(x_range=sorted_events, height=350, title="Medallas Paraolímpicas",
            toolbar_location=None, tools="")

    p.vbar(x=paralympic_event, top=total_gold_medals, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    show(p)