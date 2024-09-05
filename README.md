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

Aquí tienes el texto corregido:

Abstracción
Tomar el tiempo no es razonable para medir T(n); será mejor aproximar.

Con una función f(x), tenemos que contar los pasos que tenemos dentro de un programa:

py
Copiar código
def f(x):
respuesta = 0

    for i in range(1000):
        respuesta += 1

    for i in range(x):
        respuesta += x

    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1

    return respuesta

No importa cuál sea el tamaño de x; el código correrá 1000 veces por el primer for. Entre más crezca x, más iteraciones deberá hacer.

Luego, hay un bucle dentro de otro bucle. En este caso, por cada iteración de i, el bucle j se repetirá, lo que será x \* x = x²; en este caso, 2x².

Para saber qué pasa en el código, podemos contar: 1 1000 x 2x²

En total:

1002 + x + 2x²

Con esto, podemos ver el crecimiento de nuestra función. En este caso, es un polinomio. Podría parecer que lo que más pesa es la constante, pero entre más crezca, esto no será correcto. Veamos el caso de x = 100:

1002 + 100 + 2 \* (100)²

Los términos que de verdad importan son los más grandes. Esta es una gran aproximación para tener una ecuación para medir el tiempo, porque los términos menos importantes desaparecen conforme el problema se hace más grande y se acerca al infinito.

Para esto, veremos la notación Big O, que nos permite olvidarnos de los términos que no son significativos para poder determinar el comportamiento del algoritmo usando el término que más importa.

Ahora podríamos comparar estos polinomios con los polinomios de otras funciones, pero aún tenemos otros términos que no nos importan y que nos distraen de la solución correcta para comparar rápidamente los tipos de algoritmos.
