
# In this part the user needs to change the solution depending on the initial matrix 
solution =[[0  ,5 , 15 , 10], [20 , 0  ,10 , 5], [30  ,35,  0,  15], [15  ,25  ,5  ,0]]


from RecursiveCode import *
result = floyd(matrix_Floyd)

import unittest

#Compares the results of the optimal solution vs those that the RecursiveCode gives you

class TestFloydAlgorithm (unittest.TestCase):
    def test_valid(self):
        result = floyd_matrix
        self.assertEqual(result[0:100], solution)
if __name__ == '__main__':
                
    unittest.main()