# Objetivos

1. Medir eficiencia temporal y espacial de los algoritmos
2. Entender como y por que graficar
3. Aprender a resolver porblemas de busqueda, ordenacion y optimizacion

# introduccion a la complejidad algoritmica

a. Por que comparamos la eificiencia de un algoritmo
b. Complejidad temporal vs complejidad espacial
c. Podemos definirla como T(n)

Como analizar paginas de internet, la diferencia entre un algoritmo y otro genera una gran diferencia
para resolver un problema en horas, dias, semanas, anios, etc.

Hay que saber si un algoritmo es capaz de resolver un problema en el tiempo esperado.

La complejidad no solo es temporal, tambien puede ser espacial, espacio en memaorai necesario para resolver un
problema.

Si queremos saber como se relacionan las diferencias entre la complejidad temporarl y espacial
hay literatura en internet

# complejidad algoritmica temporal

Se marca como T(n)

# Aproximicaciones para definir T(n)

a. Cronometear el tiempo en el que corre un algoritmo, pero la diferencia de tiempo depende de muchos factores, como el equipo, los cpus, de los programas abiertos, etc.

b. Contar los pasos con una medidad abstracta de operacion, contar operaciones, asignaciones, etc, etc pero la solucion puede variar de implementacion a implementacion entre algoritmos pero entre crece el data set empieza a ser irrelevante

c. La forma estandar de medirlo es si con los pasos pero con una medida asintotica (viendo hacia el infinito).

# Abstraccion

Tomar el tiempo no es rasonable para medir T(n), sera mejor aproximar.

Con una funcion f(x), tenemos que contar los pasos que tenemos dentro de un programa

```py
def f(x):
    respuesta = 0

    for i in range(1000):
        repsuesta += 1

    for i in range(x):
        repsuesta += x

    for i in range(x):
        for i in range(x):
            respuesta += 1
            respuesta += 1

    return respuesta
```

No importa cual seal tamanio de x, el codigo correra 1000 veces por el for, entre mas crezca x, mas recursiones debera hacer.

Luego hay un loop dentro de un loop, en este caso j, cada que se haga i, se repetira el loop j, que sera x \* x = x^2, en este caso 2x^2

Para saber que pasa en el codigo podemos contar, aqui hay
1
1000
x
2x^2

en total:

1002 + x + 2x^2

con esto podemos ver el crecimiento de nuestra funcion, en este caso, es un polinomio, podria parecer que lo que mas pesa es la constante, pero entre mas crezca, esto no sera correcto, veamos en el caso de 100

1002 + 100 + 2\*(100)^2

Los terminos que de verdad importan son los mas grandes, esta es una medida es una gran aproximacion para tener una ecuacion para medir el tiempo, porque los terminos no important conforme el problema se hace mas grande y se acerca al infinito.

Para esto veremos el big O notacion para olvidarnos de los terminos que no estan sirviendo para poderlo determinar con el termino que nos importa.

Ahora podriamos comparar estos polinomios con los polinomios de otras funciones pero aun tenemos otros terminos que no nos estan importando y nos distraen de la solucion correcta para comprar rapidamente los tipos de algoritmos

# Notacion asintotica

Big O Notation que nos permite encuadrar cada uno de los algoritmos que veamos en una de las clases que permiten compararlo para entender de entrada como nuestro algoritmo va a crecer

## Crecimiento asintotico

Asintotico quiere decir conforme algo crece hacia al infinito, como se comporta una funcion conforme crece hacia el infinito.

a. No importan las varaciones pequenias
b. El enfoque se centra en lo que pasa conforme el tamanio del problema se acerca al infinito.
c. Mejor de los casos, promedio y peor de los casos. Lo que sirve mejor es el peor de los casos.
d. Big O, que lo define el termino de mayor tamanio.
e. Nada mas importa el termino de mayor tamanio.

## Ley de la suma

```py

def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

```

### O(n) + O(n) = O(n + n) = O(2n) = O(n)

La funcion crece en O(n), O de N.

```py

def f(n):
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

```

### O(n) + O(n \* n) = O(n + n^2) = O(n + n^@) = O(n^2)

La funcion crece en O(n^2), O de N cuadrada, es una funcion cuadratica.

## Ley de la multiplicacion

```py

def f(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# se vera como se mueve i con j, los loops no estan al mismo nivel
```

### O(n) _ O(n) = O(n _ n) = O(n^2)

La funcion crece en O(n^2), O de N cuadrada, es una funcion cuadratica.

Lo importante es poder identificar estos patrones. Con un loop tengo uno lineal, si es un loop dentro de otro loop es probablemente cuadratico.

## Ley de la multiplicacion

```py

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

```

### O(2^n)

La funcion crece en O(2^n).

Por cada llamada de fibonacci, llammamos dos llamadas de funciones. 2 por cada n. Esto no escala, se tiene un crecimiento exponencial.

Primeros segmentos de BigO.

Una funcion recursiva que genera mas de una llamada recursiva,se puede tener un crecimiento exponencial.

# Complejidad Algoritmica

# Algoritmos de busqueda y ordenacion (Busqueda lineal)

Aplicar los conceptos de complejidad algoritmica, y existen varios algoritmos para resolver un problema.

Lo mas importante para un computer scientist es poder reducir un problema a un problema del que ya sabemos su resolucion.

## Busqueda lineal

Es ver cada uno de los elementos en un array y ver si podemos identificar x elemento en un array ordenado o no ordenado

### Cual es el peor caso o BigO de este tipo de algoritmos?

Seria O(n)

## Busqueda Binaria

a. Divide y conquista
b. El problema se divide en 2 en cada iteracion
c. Cual es el peor caso?

Se hace el problema cada vez mas pequenio hasta llegar a la solucion, se divide entre dos en cada iteracion y asume que el algoritmo esta ordenado, pero no existe un buen algoritmo para poder ordenar.

Pero, debemos ordenar para luego hacer la busqueda?

Si vas a usar muchas veces tu algoritmo, peude que valga la pena, porque amortizamos el costo de la busqueda, porque podremos usar un codigo muy eficiente de busqueda, que es la busqueda ordinaria.

Preguntate

### Esta ordenada la lista?

Aqui hay un gran trade off, podemos cambiar tiempo por espacio, para optimizar tiempo es probable que tengamos que gastar mas memoria. Es complejo tener lo bueno de ambos conceptos.

### Cual es el peor caso?

# Algoritmos de Ordenaciones != algoritmos de busqueda

## Ordenamiento de burbuja o bubble sort

Es uno de los mas intuitivos, es un algoritmo que recorre repetidamente una lista que necesita ordenarse, comparaw elementos adyacentes y los intercambia si es estan en desorden. Este procedimiento se repite hasta que no se requiren mas intercambios, lo que indica que la lsita se encuentra ordenada.

Recorreremos la lista y compararemos cada elemento, y su uno es mas grande que el otro, los ordenaremos. Se recorre la lista, n por n, es deicr, el tamanio de elementos e slas veces que se recorrera.

Es importante tener una visualizacion de lo que va a pasar.

### Caracteristicas y ventajas

Despues de la primera ronda, tenemos al garantia de que el elemento mas grande se encuentra hasta el final.

Una ventaja es que si buscamos el elemento mas grande, con bubble sort nos aseguramos que al final del primer ciclo, tendremos el valor mas grande hasta al final.

Recorremos la lista n veces, n veces

### Cual es la complejidad algoritmica

Pienso O(n^2)

## Ordanamiento por mezcla

Es un algoritmo de divide y conquitsa. Primero divide una lista en partes iguales hasta que quedan sublistas de 1 o 0 elementos. Luego las recombina en forma ordenada

Cuando una lista tiene cero elementos, esta ordenada por definicion, luego se comparan las listas cada vez mas pequenias y mas pequenias hasta que tenemos una lista totalmente ordenada. Fue creada por Newman.

Los codigos hasta ahora son relativamente sencillos pero merge sort es un poco mas dificil de comprender, por eso es importante dominar conceptualmente primero.

Se divide constante a la mitada hasta ser indivisible, luego se compara en cantidades iguales para luego ser ordenado, y esta operacion se repite hasta devolver la cadena de longitud original pero ordenada.

No solo es el algoritmo, sino poder ver el algoritmo O(nlogn)

# Ambientes virtuales

a. Permiten aislar el ambiente para poder instalar diversas versiones de paquetes
b. A partir de python3 se incluye en la libreria estandar en el modulo venv
c. Ningun ingeniero profesional de Python trabaja sin ellos

```sh
mkdir graficado
cd graficado
python3 -m venv env
source env/bin/activate

pip install bokeh
pip freeze

deactivate
```

no instalar de manera global, siempre de manera local

# Graficar

Por que es importante graficar?

a. Reconocer patrones
b. Prediccion de una serie
c. Simplifica la interpretacion y las conclusiones acerca de los datos

# Graficado Simple

a. Bokeh permite construir graficas complejas de manera rapida y con comandos simples
b. Permite exportar a varios formatos como html, notebooks, imagenes, etc
c. Bokeh se puede utilizar en el servidor con Flask y Django

Hay que determinar para que queremos la visualizacion, incluso si es programatica para que la vean los usuarios.

Para Bokeh, se puede hacer aqui:
https://docs.bokeh.org/en/latest/

Tiene multiplicidad de graficos pero eso tiene sus riegos, hay que seleccionar correctamente el tipo de grafico. No porque se puede hacer algo, quiere decir que sea la forma correcta.

Para poder ver las gráficas:

```sh

sudo apt-get update
sudo apt-get install firefox
BROWSER=firefox python3 6_graphs.py

```

# Optimizacion

a. El concepto de optimizacion permite resolver muchos problemas de manera computacional
b. Una funcion objetivo que debemos maximizar o minimizar
c. Una serie de limitantes que debemos respetar

Para problemas computacionales, muchos de los problemas del mundo se pueden reducir a algoritmos de maximizacion y minimizacion.

Siempre se pueden tener limitantes, o constrains, por ejemplo optimizar vuelos, el vuelo mas barato dentro de ciertas fechas y sin escalas y que este cerca de salidas de emergencia.

Si los resuelves puedes tener empresas billonarias, como waze que resuleve el algoritmo del trafico.

Un problema famoso es el travelling salesman, buscar la ruta mas eficiente para recorrer todas las ciudades, hoy en dia no existe un problema que lo pueda resolver.

Serian algoritmos O(n np)

Problemas del milenio por Un millón de dólares

    P versus NP
    La conjetura de Hodge
    La conjetura de Poincaré
    La hipótesis de Riemann
    Existencia de Yang-Mills y del salto de masa
    Las ecuaciones de Navier-Stokes
    La conjetura de Birch y Swinnerton-Dyer

diferencia de np contra np, sin son iguales o no son iguales o son diferentes, o son diferentes te ganas el turin award.

Estudiar Travelling Sales Man.

# El problema del morral

Un ladron en un museo, con solo un morral para llevarse cosas pero con mas cosas de las que puede cargar. Que cosas puede llevarse para garantizar que se puede llevar el mayor valor posible?

## 1-0 valor del morral

No se pueden dividir los objetos, en este caso, pero en la programacion dinamica si se podria.

Este problema se puede resolver con greedy algorythms, nosotros escogemos los 1ro mas alto, luego lo 2do mas alto, etc, pero como no los podemos partir no podemos usar greedy algo.

Un ejemplo seria el oro molido, plata molida y al final el arroz, pero aqui no aplica porque no se pueden subdividir los elementos.

Funcion recursiva para solucionar este problema de manera eficiente, o la modalidad de problema que vemos es 1-0 valor del morral.

## que complejidad tiene?

Como es una funcion recursiva es probable que sea O(n^n)

Por cierto, este algoritmo es reutilizable:

```py

def morral(tamano_morral, pesos, valores, n):
    # n es indice del morral donde estamos trabajando
    # hay que pensar en nuestro caso base al ser recursivo
    # en python no hay problema pues tiene un break interno
    # pero para otros programas es como tener un whil einfinito

    # si no mas elementos o morral lleno ya no puedo regresar valores
    if n == 0 or tamano_morral == 0:
        return 0

    # si peso de elemento n es mayor que el morral
    if pesos[n - 1] > tamano_morral:
        # checamos el siguiente elemento sin hacer el morral mas chico
        return morral(tamano_morral, pesos, valores, n - 1)

    # si si me quedan elementos y espacios tengo que tomar un decision, y si lo meto si es el valor maximo entre meterlo o no meterlo
    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos,valores, n - 1), morral(tamano_morral, pesos, valores, n - 1))

```

# Retos

Paginas para retos de python u otros lenguajes. Es importante practicar.

https://www.hackerrank.com
https://codewars.com
http://codeforces.com/
https://coderbyte.com/
https://www.codingame.com/
https://www.codechef.com/
https://www.topcoder.com/challenges/
https://leetcode.com/problemset/
