import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        # if we have 1x1 Matrix
        determinant = 0
        if self.h == 1:
            determinant = self.g[0]
            return determinant
        
        # if we have 2x2 Matrix:
        if self.h == 2:
            determinant = self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]
            return determinant
        
        print("the determinant of matrix: " + self + "is: " + determinant)

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        # initialize trace variable
        trace = 0
        # loop through the columns in matrix
        for i in range(self.w):
            trace += self.g[i][i]
        return trace
    
        print("the trace of matrix: " + self + "is: " + trace)

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        # if we have 1x1 Matrix
        if self.w == 1:
            return Matrix(1/self.g[0][0])
        # if we have 2x2 Matrix
        if self.w == 2:
            inversedGrid = zeroes(self.w, self.h)
            inversedGrid[0][0] = self.g[1][1] * (1/self.determinant())
            inversedGrid[0][1] = -self.g[0][1] * (1/self.determinant())
            inversedGrid[1][0] = -self.g[1][0] * (1/self.determinant())
            inversedGrid[1][1] = self.g[0][0] * (1/self.determinant())
            
            return inversedGrid
        
        print("the inversed grid of matrix: " + self + "is: " + inversedGrid)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        
        number_of_rows = self.w
        number_of_columns = self.h
        transposed_matrix = zeroes(number_of_rows, number_of_columns)
        
        for i in range(self.h):
            for j in range(self.w):
                original_value = self.g[i][j]
                transposed_matrix[j][i] = original_value
        return transposed_matrix
    
        print("the transposed copy of this Matrix: " + self + "is: " + transposed_matrix)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        added_grid = []
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                first_value = self.g[i][j]
                second_value = other.g[i][j]
                new_value = first_value + second_value
                new_row.append(new_value)
            added_grid.append(new_row)
        return Matrix(added_grid)
    
        print("The added matrix is: " + Matrix(added_grid))

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        
        # let's create new matrix using zeroes() function
        new_matrix = zeroes(self.h, self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                 new_matrix[i][j] = self.g[i][j]*-1.0
        return new_matrix
    
        print("The new matrix is: " + new_matrix)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        sub_matrix = self + (-other)
        return sub_matrix
    
        print("The new matrix is: " + sub_matrix)
    
                       

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        # let's create new matrix using zeroes() function
        grid = zeroes(self.h, other.w)
        
        for x in range(self.h):
            for y in range(other.w):
                for z in range(other.h):
                    grid[x][y] += self.g[x][z] * other.g[z][y]
        return grid
    
        print("The new matrix is: " + grid)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #   
            # TODO - your code here
            #
            multiply_by_number_matrix = self
            for i in range(self.h):
                for j in range(self.w):
                    multiply_by_number_matrix[i][j] *= other
            return multiply_by_number_matrix
        
            print("The new matrix is: " + multiply_by_number_matrix)
            
