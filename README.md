# Programacion 1 - Python

## Nicolás Ríos
## riosnicolas618@gmail.com

# Proyecto
EL objetivo del programa es que tenga una función que reciba por parámetros una matriz de strings con los caracteres válidos (A, T, C, G), y devuelva True si contiene mas de una secuencia de caracteres iguales ya sea de forma horizontal, vertical o diagonal en ambos sentidos.

# Solución
Mi resolución consiste en la creacion de 3 funciones, la primera es para que el usuario llene la matriz, la segunda funcion muestra la matriz ingresada por el usuario, y la tercera y mas importante es la funcion que determina si la matriz ingresada por el usuario pertenece a un mutante o no.

La funció es_mutante(matriz) primero realiza la verificación horizontal, luego la vertical y por último la verificación oblicua.

# ¿Cómo correr el programa?
Para correr el programa el primer paso sería clonar el repositorio con el siguiente comando:
	`git clone url del repositorio`

Una vez clonado el repositorio y abierto en el editor de codigo, podés correrlo con el botón de "Run", en el caso de Visual Studio Code proporciona el clasico botón de play en la parte superior derecha y una vez clickeado debe elegir la opción de "Run Python File"

Otra forma de correr el programa es ingresando el siguiente comando en la consola:
	`python nombre_del_archivo.py`