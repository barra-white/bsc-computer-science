from evaluation import *
'''
File used for comparing sorting algorithms in sorting_algorithms.py using the functions
defined in the assignment (Part 1-6) contained in evaluation.py
'''



#variable for number of lists to be tested
numberOfLists: int = 100

#variable containing a list of sorting algorithms to be tested
listOfFunctions: list = [heapSort]

#parameters to be tested on evaluateAll
parameters: list[tuple] = [(10, 4), (100, 25), (1000, 250), (10000, 2500)]
#parameters to be tested on evaluateAllPartial
partialParameters: list[tuple] = [(10, 4, 2), (100, 25, 2), (1000, 250, 2), (10000, 2500, 2)]
#parameter set to be implemented in evaluate all partial to test nearly already sorted lists
basicallySortedParameters: list[tuple] = [(10, 4, 2), (100, 25, 25), (1000, 250, 250), (10000, 2500, 2500)]

#runs evaluateAllScale using variables outlined above
#-- evaluateAllScale(numberOfLists, listOfFunctions, parameters)

#runs evaluateAllPartialScale using variables outlined above with a mostly shuffled list
#-- evaluateAllPartialScale(numberOfLists, listOfFunctions, partialParameters)

#runs evaluateAllPartialScale using variables outlined above with a mostly shuffled list
#-- evaluateAllPartialScale(numberOfLists, listOfFunctions, basicallySortedParameters)