
# element class
class Element:
     
     
     def __init__(self, k, v: tuple, i):
          self._key = k
          self._value = v
          self._index = i

     def __eq__(self, other):
          return self._key == other._key
     
     def __lt__(self, other):
          return self._key < other._key
          
     def __gt__(self, other):
          return self._key > other._key
     
     def __str__(self) -> str:
          return f'\nKey: {self._key}\nValue: {self._value}\nIndex: {self._index}'
     
     # get and set methods for key
     def getKey(self):
          return self._key
     
     def setKey(self, k) -> None:
          self._key = k

     # get and set methods for value
     def getValue(self):
          return self._value
     
     def setValue(self, v: tuple()) -> None:
          self._value = v

     # get and set methods for index
     def getIndex(self) -> int:
          return self._index
     
     def setIndex(self, i: int) -> None:
          self._index = i
     
     def _wipe(self):
          self._key = None
          self._value = None
          self._index = None

class UnsortedAPQ:
     def __init__(self):
          self._list = []

     def __str__(self) -> str:
          out = '\n<-----'
          for i in self._list:
               out += str(i) + '\n-----'
          return out + '>\n'
     
     # add method by key and value
     def add(self, key, value):
          if len(self._list) == 0:
               i = 0
          else:
               i = len(self._list)

          ele = Element(key, value, i)
          self._list.append(ele)
          return ele
     
     # method to iterate over all element keys in list and return element with minimum key
     def min(self):
          if len(self._list) == 0:
               return None
          else:
               minPriority = self._list[0]
               for ele in self._list:
                    if ele < minPriority:
                         minPriority = ele
          return minPriority.getKey(), minPriority.getValue()
     
     # get method for length of apq
     def length(self):
          return len(self._list)
     
     # method to remove and return element with minimum key
     def removeMin(self):
          if len(self._list) == 0:
               return None
          else:
               min = self._list[0]
               for ele in self._list:
                    if ele < min:
                         min = ele
               self._list.pop(min.getIndex())
          for ele in self._list:
               if ele.getIndex() > min.getIndex():
                    ele.setIndex(ele.getIndex()-1)
          return min
     
     # method to update element key
     def updateKey(self, element: Element, newKey: int):
          if len(self._list) == 0:
               return None
          else:
               element.setKey(newKey)
          for ele in self._list:
               ele.setIndex(self._list.index(ele))
          return element
     
     def getKey(self, element: Element):
          return element.getKey()
     
     def remove(self, element: Element):
          if len(self._list) == 0:
               return None
          else:
               index = element.getIndex()
               self._list.pop(index)
          
          for ele in self._list:
               if ele.getIndex() > element.getIndex():
                    ele.setIndex(ele.getIndex() - 1)
          return element.getKey(), element.getValue()
     
     def getBody(self):
          return self._list

class HeapAPQ:
     def __init__(self):
          self._heap = []
     
     def __str__(self) -> str:
          out = '\n<-----'
          for i in self._heap:
               out += str(i) + '\n-----'
          return out + '>\n'
     

     # bubble up helper function
     def bubbleUp(self, index: int) -> None:
          while index > 0:
               parent = (index-1)//2
               if self._heap[index] > self._heap[parent]:
                    self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
                    index = parent
               else:
                    index = 0

     # bubble down helper function
     def bubbleDown(self, index: int, last: int) -> None:

          while last > (index*2):
               leftChild = (index*2)+1
               rightChild = (index*2)+2
               biggestChild = leftChild
               if last > leftChild and self._heap[rightChild] > self._heap[leftChild]:
                    biggestChild = rightChild
               if self._heap[index] < self._heap[biggestChild]:
                    self._heap[index], self._heap[biggestChild] = self._heap[biggestChild], self._heap[index]
                    index = biggestChild
               else:
                    index = last

     # add method by key and value
     def add(self, key, value):
          if len(self._heap) == 0:
               i = 0
          else:
               i = len(self._heap)

          ele = Element(key, value, i)
          self._heap.append(ele)
          self.bubbleUp(i)
          return ele
     
     # method to return element with minimum key
     def min(self):
          if len(self._heap) == 0:
               return None
          else:
               return self._heap[0].getKey(), self._heap[0].getValue()
          
     # method to get length of heap
     def length(self):
          return len(self._heap)
     
     # method to remove and return element with minimum key
     def removeMin(self):
          if len(self._heap) == 0:
               return None
          else:
               min = self._heap[0]
               self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
               self._heap.pop()
               self.bubbleDown(0, len(self._heap)-1)

          for ele in self._heap:
               ele.setIndex(self._heap.index(ele))
          return min
     
     # method to update element key
     def updateKey(self, element: Element, newKey: int):
          if len(self._heap) == 0:
               return None
          else:
               element.setKey(newKey)
               self.bubbleUp(element.getIndex())
          for ele in self._heap:
               ele.setIndex(self._heap.index(ele))
          return element
     
     # method to get element key
     def getKey(self, element: Element):
          return element.getKey()
     
     # method to remove element
     def remove(self, element: Element):
          if len(self._heap) == 0:
               return None
          else:
               index = element.getIndex()
               self._heap[index], self._heap[-1] = self._heap[-1], self._heap[index]
               self._heap.pop()
               self.bubbleDown(index, len(self._heap)-1)
          for ele in self._heap:
               ele.setIndex(self._heap.index(ele))
          return element.getKey(), element.getValue()
     
     def getBody(self):
          return self._heap