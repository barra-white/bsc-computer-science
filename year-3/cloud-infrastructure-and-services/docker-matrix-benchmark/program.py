from random import randint
import time

def matrix(n: int) -> list[list[int]]:
     '''
     creates a n * n matrix

     Args:
          n - specifies size of matrix (n * n)
            - also used to specify range of numbers to be included in matrix (0, n)

     Returns:
          n * n matrix with random numbers from 0 to n
     '''
     # initialise empty list for matrix
     mat = []
     for i in range(n):
          # initialise empty list for matrix row
          row = []
          for j in range(n):
               row.append(randint(0, n))
          # append row to matrix
          mat.append(row)
     return mat

def mulMatrix(matA: list[list[int]], matB: list[list[int]]) -> list[list[int]]:
     '''
     multiplies input matrix and returns output

     Args:
          matA - first input matrix
          matB - second input matrix

     Returns:
          result - new matrix that is the result of multiplying matA and matB
     '''
     size = len(matA)

     output = [[0 for _ in range(size)] for _ in range(size)]
     for i in range(size):
        for j in range(size):
            for k in range(size):
                output[i][j] += matA[i][k] * matB[k][j]
     return output

def getRuntime(matA: list[list[int]], matB: list[list[int]]) -> float:
     '''
     returns runtime of matrix multiplication

     Args:
          matA - first input matrix
          matB - second input matrix

     Returns:
          runtime - runtime of matrix multiplication
     '''
     # start timer
     start = time.perf_counter()
     # multiply matrices
     mulMatrix(matA, matB)
     # stop timer
     end = time.perf_counter()
     # calculate runtime
     runtime = end - start

     return runtime
     
def getAvgRuntime(n: int, times: int) -> float:
     '''
     returns average runtime of matrix multiplication

     Args:
          n - specifies size of matrix (n * n)
            - also used to specify range of numbers to be included in matrix (0, n)
          times - specifies number of times to run matrix multiplication

     Returns:
          avgRuntime - average runtime of matrix multiplication
     '''
     # initialise empty value to store total runtime
     totalRuntime = 0
     for t in range(times):
          # create matrices
          matA = matrix(n)
          matB = matrix(n)
          # add runtime to totalRuntime
          totalRuntime += getRuntime(matA, matB)
          # increment t
          t += 1
     # calculate average runtime
     avgRuntime = totalRuntime / times

     return avgRuntime


def evaluate(max: int, times: int) -> dict[int, float]:
     """
     Args:
         max - specifies max matrix size
         times - specifies number of times to run matrix multiplication on each n value
                 including this parameter will give a more accurate representation of average runtime
                 while minimising the effect of outliers

     Returns:
         results - dictionary of runtimes for each n value with n as key and average runtime as value
     """
     # initialise starting value for matrix size (must be at least 2)
     n = 2
     # initialise starting value for number of times to run matrix multiplication (must run at least once)
     t = 1
     # empty dictionary to store results for each n value
     results = {}
     while n <= max:
          # call get average runtime for each n value and store in dictionary with key=n and value=avgRuntime
          results[n] = getAvgRuntime(n, times)
          # increment n
          n += 1
     # print results dictionary
     for k, v in results.items():
          print(f'{k}: {v}' + ',')
     return results

if __name__ == '__main__':
     evaluate(200, 20)