from sorting_algorithms import *
import time, random, copy
'''
File used to store all functions used to test the sorting algorithms on a range of different
unsorted lists using different parameters in each of the functions. Functions split in to parts
1-6 as specified in the assignment.
'''



               ### PART 1 ###
def testOneAlgorithm(userList: list[int], f) -> float:
     '''
     Measures the performance of a sorting algorithm on an inputted list.
     Args:
          userList - inputted list to be sorted
          f - sorting algorithm to be used on userList
     '''
     start_time = time.perf_counter()
     f(userList)
     end_time = time.perf_counter()
     checkSorted(userList, f)
     return end_time - start_time

def checkSorted(userList: list[int], f) -> None:
     '''
     Checks if inputted list has been sorted, display error if not
     Args:
          userList - list to be checked if sorted
          f - function used to sort the list
     '''
     for i in range(1, len(userList)):
          #check if the list isn't sorted
          if userList[i] < userList[i-1]:
               #print error message for first instance of list not being sorted
               listMessage = f'Inputted List: {userList}\n'
               funcMessage = f'Sorting Function: {f.__name__}\n'
               errorMessage = f'{userList[i]} at index {i} is smaller than {userList[i-1]} at index {i-1}.\n'
               print(listMessage, funcMessage, errorMessage)
               #exit loop after error message printed
               break





               ### PART 2 ###
def randomList(n: int, k: int) -> list[int]:
     '''
     Generates a random unsorted list of integers
     Args:
          n - length of the list
          k - amount of duplicate items in list
     '''
     newList = []
     #append values in range
     for i in range(1, (n-k+1)):
          newList.append(i)
     #append k duplicate values
     for j in range(k):
          newList.append(newList[random.randint(0, (n-k-1))])
     #shuffle list
     random.shuffle(newList)
     return(newList)





               ### PART 3 ###
def evaluate(n: int, k: int, num: int, f) -> None:
     '''
     Creates random lists and sorts them using inputted function,
     displaying the average performance
     Args:
          n - length of the lists
          k - amount of duplicate items in lists
          num - number of lists to be sorted
          f - function used to sort list
     '''
     #set parameters for total and avg run time
     avgRunTime = 0
     totalRunTime = 0
     #check if there is at least one list to be tested
     if num > 0:
          #for each list get total run time
          for i in range(num):
               newList = randomList(n, k)
               totalRunTime += testOneAlgorithm(newList, f)
               #get avg run time
          avgRunTime = totalRunTime / num
     functionMessage = f'Sorting Function: {f.__name__}\n'
     runTimeMessage = f'Runtime: {avgRunTime}\n'
     listMessage = f'List Length: {n}\nDuplicates: {k}\nNumber of Lists Tested: {num}\n'
     #print function name, list length, duplicates, number of lists and avg run time
     print(functionMessage, runTimeMessage, listMessage)





               ### PART 4 ###
def evaluateAll(n: int, k: int, num: int, funcs: list) -> None:
     '''
     Like evaluate, but sorts the same lists on a range of inputted functions.
     Used to compare run times between different sorting algorithms.
     Args:
          n - length of the lists
          k - amount of duplicate items in lists
          num - number of lists to be sorted
          funcs - list of functions to be tested
     '''
     #create a list to store all lists to be tested
     randomLists = []
     #check if there is at least one list to be tested      
     if num > 0:
          #for every list to be tested, append to parent list
          for i in range(num):
               newList = randomList(n, k)
               randomLists.append(newList)
     #for every function to be tested
     for f in funcs:
          #set parameters for total and avg run time
          totalRunTime = 0
          avgRunTime = 0
          #create a copy of the parent list randomLists, so they aren't affected for each function
          copiedList = copy.deepcopy(randomLists)
          #compute run time for each of the copied lists
          for c in copiedList:
               totalRunTime += testOneAlgorithm(c, f)
          #compute average run time
          avgRunTime = totalRunTime / num
          functionMessage = f'Sorting Function: {f.__name__}\n'
          runTimeMessage = f'Runtime: {avgRunTime}\n'
          listMessage = f'List Length: {n}\nDuplicates: {k}\nNumber of Lists Tested: {num}\n'
          #print function name, list length, duplicates, number of lists and avg run time
          print(functionMessage, runTimeMessage, listMessage)
          




               ### PART 5 ###
#scaler for evaluateAll
def evaluateAllScale(num: int, funcs: list, parameters: list[tuple]) -> None:
     '''
     Runs evaluateAll() on inputted functions using multiple different parameters
     Args:
          num - number of lists to be sorted
          funcs - list of functions to be tested
          parameters(n, k) - Tuple of parameters to specify:
                                                  n: length of the lists
                                                  k: amount of duplicate items in list
     '''
     for (n, k) in parameters:
          evaluateAll(n, k, num, funcs)

#scaler for evaluateAllPartial
def evaluateAllPartialScale(num: int, funcs: list, parameters: list[tuple]) -> None:
     '''
     Runs evaluateAllPartial() on inputted functions using multiple different parameters
     Args:
          num - number of lists to be sorted
          funcs - list of functions to be tested
          parameters(n, k, d) - Tuple of parameters to specify:
                                                  n: length of the lists
                                                  k: amount of duplicate items in list
                                                  d: helps specify amount of items to be swapped
                                                     (n // d = number of swaps)
     '''
     for (n, k, d) in parameters:
          evaluateAllPartial(n, k, d, num, funcs)





               ### PART 6 ###
def evaluateAllPartial(n: int, k: int, d: int, num: int, funcs: list) -> None:
     '''
     Like evaluateAll, but only partially shuffles list with a specified number of swaps.
     Used to compare run times between different sorting algorithms on partially sorted lists.
     Args:
          n - length of the lists
          k - amount of duplicate items in lists
          d - helps specify amount of items to be swapped
              (n // d == number of swaps)
          num - number of lists to be sorted
          funcs - list of functions to be tested
     '''
     #create a list to store all lists to be tested
     randomLists = []
     #set parameter for amount of swaps
     swaps = n // d
     #check if there is at least one list to be tested
     if num > 0:
          #for every list to be tested, append to parent list
          for i in range(num):
               newList = randomList(n, k)
               randomLists.append(newList)
     #for every randomised list
     for r in randomLists:
          #use python inbuilt sort to sort the lists
          r.sort()
          #loop to swap the amount of items needed to be swapped
          for i in range(swaps):
               #get two random indexes in the list
               pos1 = r[random.randint(0, len(r)-1)]
               pos2 = r[random.randint(0, len(r)-1)]
               #swap the items at the random indexes
               r[pos1], r[pos2] = r[pos2], r[pos1]
     #for every function to be tested
     for f in funcs:
          totalRunTime = 0
          avgRunTime = 0
          #create a copy of the parent list randomLists, so they aren't affected for each function
          copiedList = copy.deepcopy(randomLists)
          #compute run time for each of the copied lists
          for c in copiedList:
               totalRunTime += testOneAlgorithm(c, f)
          #compute average run time
          avgRunTime = totalRunTime / num
          functionMessage = f'Sorting Function: {f.__name__}\n'
          runTimeMessage = f'Runtime: {avgRunTime}\n'
          listMessage = f'List Length: {n}\nDuplicates: {k}\nNumber of Lists Tested: {num}\n'
          swapMessage = f'Number of Swaps: {swaps}\n'
          #print function name, list length, duplicates, number of lists, avg run time and number of swaps
          print(functionMessage, runTimeMessage, listMessage, swapMessage)