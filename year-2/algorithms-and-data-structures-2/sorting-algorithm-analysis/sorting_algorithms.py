import random
'''
File contains all sorting algorithms that will be tested:
      - Insertion Sort
      - Merge Sort
      - Heap Sort
      - Quick Sort
'''



               ### INSERTION SORT ###
def insertionSort(userList: list[int]) -> None:
     n = len(userList)
     i = 1
     while i < n:
          j = i-1
          while userList[i] < userList[j] and j > -1:
               j -= 1
          #insert i in the cell after j
          temp = userList[i]
          k = i-1
          while k > j:
               userList[k+1] = userList[k]
               k -= 1
          userList[k+1] = temp
          i += 1



               ### MERGE SORT ###
# merge helper function
def merge(list1: list[int], list2: list[int], userList: list[int]) -> None:
     f1 = 0
     f2 = 0
     while f1 + f2 < len(userList):
          if f1 == len(list1):
               userList[f1+f2] = list2[f2]
               f2 += 1
          elif f2 == len(list2):
               userList[f1+f2] = list1[f1]
               f1 += 1
          elif list2[f2] < list1[f1]:
               userList[f1+f2] = list2[f2]
               f2 += 1
          else:
               userList[f1+f2] = list1[f1]
               f1 += 1
# main merge sort function
def mergeSort(userList: list[int]) -> None:
     n = len(userList)
     if n > 1:
          list1 = userList[:n//2]
          list2 = userList[n//2:]
          mergeSort(list1)
          mergeSort(list2)
          merge(list1, list2, userList)



               ### HEAP SORT ###
# bubble up helper function
def bubbleUp(userList: list[int], index: int) -> None:
     while index > 0:
          parent = (index-1)//2
          if userList[index] > userList[parent]:
               userList[index], userList[parent] = userList[parent], userList[index]
               index = parent
          else:
               index = 0
# bubble down helper function
def bubbleDown(userList: list[int], index: int, last: int) -> None:
     while last > (index*2):
          leftChild = (index*2)+1
          rightChild = (index*2)+2
          biggestChild = leftChild
          if last > leftChild and userList[rightChild] > userList[leftChild]:
               biggestChild = rightChild
          if userList[index] < userList[biggestChild]:
               userList[index], userList[biggestChild] = userList[biggestChild], userList[index]
               index = biggestChild
          else:
               index = last
# main heap sort function
def heapSort(userList: list[int]) -> None:
     length = len(userList)
     for i in range(length):
          bubbleUp(userList, i)
     for j in range(length):
          userList[0], userList[length-1-j] = userList[length-1-j], userList[0]
          bubbleDown(userList, 0, length-2-j)



               ### QUICK SORT ###
def quickSort(userList: list[int]) -> list[int]:
    n = len(userList)
    for i in range(len(userList)):
        j = random.randint(0, n-1)
        (userList[i], userList[j]) = (userList[j], userList[i])
    _quickSort(userList, 0, n-1)
    return userList

#quickSort helper function
def _quickSort(userList: list[int], first: int, last: int) -> None:
    #sort elements of lst from first up to last
     if last > first:
          pivot = userList[first]
          f = first + 1
          b = last
          while f <= b:
               while f <= b and userList[f] <= pivot:
                    f += 1
               while f <= b and userList[b] >= pivot:
                    b -= 1
               if f < b:
                    (userList[f], userList[b]) = (userList[b], userList[f])
                    f += 1
                    b -= 1
          (userList[b], userList[first]) = (userList[first], userList[b])
          _quickSort(userList, first, b-1)
          _quickSort(userList, b+1, last)

               ### BUBBLE SORT ###
def bubbleSort(userList: list[int]) -> None:
     n = len(userList)
     for i in range(n):
          for j in range(n-1):
               if userList[j] > userList[j+1]:
                    userList[j], userList[j+1] = userList[j+1], userList[j]