from bokeh.plotting import figure, output_file, show
# ventatna para graficar
# determinar el nombre del archivo a generar
# para generar un servidor que muestre el html directo en el navegador

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()
    # type(fig)
    # help()
    
    total_vals = int(input('Cuantos valores quires graficar?'))
    x_vals = list(range(total_vals))
    
    y_vals =  []
    
    for x in x_vals:
        val = int(input(f'Valor Y para para {x}: '))
        y_vals.append(val)
        
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)