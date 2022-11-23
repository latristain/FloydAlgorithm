####The RecursiveCode.py model is an adaptation of the code of following web page. https://favtutor.com/blogs/floyd-warshall-algorithm 

#### Interaction between the user and the computer

#NumPy library is imported this is a Python library used for working with arrays
import numpy as np

#Interaction between the user and the computer

#Step where the user enters a value for infinite
inf = 999

#Code that asks you the number of vectors to enter
nV = int(input("Enter the number of vectors:"))

#The rows and columns are set equal to the number of vectors
R = nV 
C = nV

#Step where the computer will ask you for the distances or the relative weights between each vector separated by spaces

print("Please enter", R*C, "the distances in a single line (separated by space):")
print("For infinite input 999")
print("Note The first number will be the distance between V1 and V2 the second between V1 and V2 and so on")

#### Initial Matrix

#The variable entries saves the values imputed by the user in a list
entries = list(map(int, input().split()))

#Step where the matrix is constructed and some possible errors that the user could make are corrected

#The variable enties is transposed by the reshape function and
matrix_Floyd = np.array(entries).reshape(R, C)

# The diagonal vectors are filled into zero in case the user imputed a value greater than zero between the same vectors 
np.fill_diagonal(matrix_Floyd, 0)

#The value of 999 takes the value of the variable inf which can be changed by the user in the code. 
matrix_Floyd[matrix_Floyd == 999] = inf 


#The matrix on which Floyd's algorithm will be solved is shown in the terminal
print("The matrix on which the Floyd Algorithm will be run is the following \n", matrix_Floyd)

#### Recursive Algorithm
# A function for Floyd's Algorithm is developed 
def floyd(matrix_Floyd):
    #A map function will iterate over the matrix_Floyd matrix to get the distances
    dist = list(map(lambda p: list(map(lambda q: q, p)), matrix_Floyd))

    # 3 Loops are created to add vertices individually
    for k in range(nV):
        for p in range(nV):
            for q in range(nV):
                #The minimum distances between the two vertices p and q are calculated
                dist[p][q] = min(dist[p][q], dist[p][k] + dist[k][q])
    print(dist)
    return dist


#### Results
# The solution for Floyd's algorithm is printen on the terminal leaving the value of infinity imputed by the user 
print ("The solution for the Floyd Algorithm is the following")   
floyd_matrix = floyd(matrix_Floyd)

#The Solution for Floyd's algorithm substituting the infinity value imputed by the user by the legend NoPath is printed on the terminal
print ("If you have an infinite path, the value of infinity will be replaced by NoPath, otherwise the same result will appear as above")   
floyd_matrix = [["NoPath" if y == 999 else y for y in x ] for x in floyd_matrix]
print(floyd_matrix)
