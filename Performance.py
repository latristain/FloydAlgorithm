#### The performance of the imperative function is measured against the performance of the recursive function to resolve the Floyd algorithm

#In order to run adequately the Performance in the Imperative.py code you have to change the graph that is to be compared
#Import Modules
import timeit

#function returns the number of seconds it took to execute the code for the Recursive Code
Recursive_Time = (timeit.timeit(stmt='floyd', setup='from RecursiveCode import floyd', number=1))

#function returns the number of seconds it took to execute the code for the Imperative Code
Imperative_Time=(timeit.timeit(stmt='floyd', setup='from Imperative import floyd', number=1))


#Difference in time between Recursive vs Imperative Time
dif_Time = Recursive_Time - Imperative_Time

#Print the Results
print("The execution time taken by the function floyd in the recursive way takes:")
print(Recursive_Time)

print("The execution time taken by the function floyd in the Imperative way takes:")
print(Imperative_Time)

print("The difference in time between the execution time taken by the function floyd in the Recursive - Imperative way takes:")
print (dif_Time)
