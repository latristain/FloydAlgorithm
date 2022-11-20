#NumPy library is imported this is a Python library used for working with arrays
import numpy as np
import sys


#Interaction between the user and the computer
#Code that asks you the number of vectors to enter
nV = int(input("Enter the number of vectors:"))

#Set the values of the different variables
R = nV 
C = nV

#Step where the computer will ask you for the distances or the relative weights between each vector separated by spaces

print("Please enter", R*C, "the distances in a single line (separated by space):")
print("For infinite input 999")
print("Note The first number will be the distance between V1 and V2 the second between V1 and V2 and so on")

entries = list(map(int, input().split()))

#Step where the user enters a value for infinite
inf = 999

#Step where the matrix is constructed and some possible errors that the user could make are corrected
# The diagonal vectors are filled into zero in case the user imputed a value greater than zero between the same vectors 

matrix_Floyd = np.array(entries).reshape(R, C)
np.fill_diagonal(matrix_Floyd, 0) 
matrix_Floyd[matrix_Floyd == 999] = inf 

print("The matrix on which the Floyd Algorithm will be run is the following \n", matrix_Floyd)


# Algorithm 
def floyd(matrix_Floyd):
    dist = list(map(lambda p: list(map(lambda q: q, p)), matrix_Floyd))

    # Adding vertices individually
    for k in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][k] + dist[k][q])
    print(dist)
    return dist


#Solution for Floyd's algorithm leaving the value of infinity imputed by the user 
print ("The solution for the Floyd Algorithm is the following")   
floyd_matrix = floyd(matrix_Floyd)

#Solution for Floyd's algorithm substituting the infinity value imputed by the user by the legend NoPath
print ("If you have an infinite path, the value of infinity will be replaced by NoPath, otherwise the same result will appear as above")   
floyd_matrix = [["NoPath" if y == 999 else y for y in x ] for x in floyd_matrix]
print(floyd_matrix)