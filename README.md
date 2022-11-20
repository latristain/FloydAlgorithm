## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Software](#software)
4. [Project](#project)
5. [Credits](#credits)


### General Info

Se construyó el Algoritmo de Floyd de manera recursiva a través de bucles anidados. Este código se construyó de tal forma que fuera interactivo es decir, el computador cuestionara al usuario sobre el número de vectores y distancia entre estos para posteriormente tras una serie de cálculos ofrecer la solución óptima. Existe un módulo que a traves del modulo UnitTest sea capaz de testear los resultados del código vs la solución óptima, asi como otro modulo que compara los resultados de un modelo que utiliza la version recursiva vs otro que utiliza el modulo itertools llamado para este caso version imperativa.

### Technologies

A list of technologies used within the project:
* [Python](https://www.python.org/downloads/): Version 3.11.0 
* [visualstudio](https://visualstudio.microsoft.com/es/):Version: 1.73.v 


### Software
Para correr este proyecto es recomendable que se tenga instalado las herramientas especificadas en el punto 2 asi mismo, se instalen para python los modulos, numpy, itertools, sys, timeit, unittest.

### Project

Este proyecto consta de 4 diferentes modulos recursive_code.py . Este modulo corre  el algoritmo de floyd de manera recursiva mediante es decir mediante bucles anidados. El modulo imperative.py el cual corre el algoritmo de Floyd mediante la herramienta itertools. El modulo unittest.py el cual valida los resultados del modelo recursivo vs la solucion optima y el modulo performance.py el cual compara el desempeno del modelo recursivo vs el imperativo.

### Credits
El modelo recursivo es una adaptacion de la siguiente pagina web. https://favtutor.com/blogs/floyd-warshall-algorithm
El modelo imperativo se utilizo fue una colaboracion de Brett Dury de la Universidad de Liverpool




