## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Software](#software)
4. [Project](#project)
5. [Credits](#credits)


### General Info

The Floyd Algorithm was built recursively through nested loops in such a way that it was interactive (RecursiveCode.py), that is, the computer would question the user about the number of vectors and the distance between them to later offer an optimal solution after a series of calculations. There were added two modules one that can verify the results of the code vs the optimal solution (UnitTest.py), as well as another module (Performance.py) that compares the performance of the recursive model vs. the results of the imperative model (Imperative.py). It is worth mentioning that the imperative model makes use of the itertools module to solve the Floyd algorithm.

### Technologies

A list of technologies used within the project:
* [Python](https://www.python.org/downloads/): Version 3.11.0 
* [visualstudio](https://visualstudio.microsoft.com/es/):Version: 1.73.v 


### Software
To run this project, it is recommended that the tools specified in section 2 be installed, as well as the modules numpy, itertools, sys, timeit and unittest.

### Project
This project consists of 4 different modules.

1. RecursiveCode.py -- This module solves Floyd's algorithm recursively using nested loops.
2. Imperative.py el --- This module solves Floyd's algorithm using the itertools tool.
3. UnitTest.py --- This module validates the results of the recursive model against the optimal solution.
4. Performance.py --- This module compares the performance of the recursive vs. imperative model.

### Credits
The recursive model is an adaptation of the following web page. https://favtutor.com/blogs/floyd-warshall-algorithm
The imperative model that was used was a collaboration of Dr Brett Dury of the University of Liverpool.




