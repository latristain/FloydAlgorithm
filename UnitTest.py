#It was validated that the result of the Floyd function(RecursiveCode.py) coincided with the expected result, that is, if the function did not return the optimal result, the program will show an error.

# In this part the user needs to change the solution depending on the initial matrix 
solution =[[0  ,5 , 15 , 10], [20 , 0  ,10 , 5], [30  ,35,  0,  15], [15  ,25  ,5  ,0]]

# All functions are imported from RecursiveCode.py 
from RecursiveCode import *
result = floyd(matrix_Floyd)

#The module UnitTest is imported
import unittest

#The self.assertEqual function is used to compare the optimal solution (entered by the user in the code) with the Floyd algorithm solution of RecursiCode.py
class TestFloydAlgorithm (unittest.TestCase):
    def test_valid(self):
        result = floyd_matrix
        self.assertEqual(result[0:100], solution)
if __name__ == '__main__':
                
    unittest.main()
