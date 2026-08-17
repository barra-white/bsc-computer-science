from math import log2

# class to represent each block (or BT Node)
class Block():
     #registry to keep track of all instances of Node
     _nodes: list = []

     def __init__(self, memorySize: int, parent=None, request=None):
          # append self to registry
          self._nodes.append(self)
          # variable to keep track of left child
          self.leftChild = None
          # variable to keep track of right child
          self.rightChild = None
          # variable to keep track of parent
          self.parent = parent
          # variable to keep track of memory size of the block
          self.memorySize = int(memorySize)
          # variable to keep track of if the block is free or now
          self.free: bool = True
          # variable to keep track of what request is being stored in the block
          self.request = request
          # variable to check if the block exists
          self.exists = True

     # method to represent block in string format
     def __str__(self):
          return f'\nBlock Size: {self.memorySize}\nCurrent RequestID: {self.request}'
     

# class to represent each request to be allocated
class Request():
     # registry to keep track of all instances of Request
     _requests: list = []

     def __init__(self, reqID: int, reqSize: int):
          self._requests.append(self)
          # variable to keep track of request ID
          self.reqID = reqID
          # size of the request
          self.reqSize = reqSize
          # size to nearest power of 2
          self.powerOf2 = int(2**(self.reqSize-1).bit_length())
          # size of k
          self.k = int(log2(self.powerOf2))
          

     # method to represent request in string format
     def __str__(self):
          return f'\nRequest ID: {self.reqID}\nRequest Size: {self.reqSize}'
     
     

# class to represent a binary tree implementation
# this is the algorithm used to track free memory and to allocate memory
class BuddySystem():

     def __init__(self, maxMemSize: int):
          # variable to keep track of tree root
          self.root = Block(maxMemSize)
          # list to store tree nodes
          self._list: list = [self.root]
          # list to store waiting requests
          self.waitingList: list = []

     def __str__(self):
          output = ''
          for b in self._list:
               output += str(b)
          return output
     
     def fragmentation(self) -> int:
          """
          Return the total fragmentation in the system
          """
          print('calculating fragmentation')
          # variable to keep track of fragmentation
          fragmentation = 0
          # loop through all blocks
          for b in self._list:
               # check if block is free
               if b.free:
                    # add block size to fragmentation
                    fragmentation += b.memorySize
          return fragmentation

     # method to allocate memory to a request
     def allocate(self, request: Request, freeBlocks: list) -> None:
          assignedBlock = self._list[self.findBlock(request.k, freeBlocks)]
          print('assigning memory to request')
          # check if block is free
          if not assignedBlock.free:
               print('no block found, adding to queue')
               self.waitingList.append(request)
               return
          else:
             
               # check if block is too big
               if assignedBlock.memorySize > request.powerOf2:
                    self.split(assignedBlock)
                    if assignedBlock.leftChild.free:

                         assignedBlock.leftChild.free = False
                         assignedBlock.leftChild.request = request.reqID
                         print('memory allocated successfully')
                         return
                    else:
                         assignedBlock.rightChild.free = False
                         assignedBlock.rightChild.request = request.reqID
                         print('memory allocated successfully')
                         return
               else:
                    assignedBlock.free = False
                    assignedBlock.request = request.reqID
                    print('memory allocated successfully')
                    return
          

     # get method to check for free blocks
     def getFreeBlocks(self, freeBlocks=[]) -> list:
          print('finding free blocks')
          for b in self._list:
               if b.free:
                    freeBlocks.append(b)
          return freeBlocks
     
     #method to split a block
     def split(self, block: Block):
          print('splitting block')
          # create left child
          block.leftChild = Block(block.memorySize/2, block)
          block.leftChild.parent = block
          # create right child
          block.rightChild = Block(block.memorySize/2, block)
          block.rightChild.parent = block
          # add left child to list
          self._list.append(block.leftChild)
          # add right child to list
          self._list.append(block.rightChild)
          print('block split successfully')

     # method to merge blocks
     def merge(self, block: Block):
          print('merging blocks')
          for b in self._list:
               if b.free and b.memorySize == block.memorySize:
                    b.free = True
                    b.request = None
                    self._list.remove(b)
                    print('blocks merged successfully')
                    return
          else:
               print('no blocks to merge')
               return
          
     # method to find block of right size
     def findBlock(self, k: int, freeBlocks: list) -> int:
          print('obtaining block of right size')
          for block in freeBlocks:
               if block.memorySize == 2**k:
                    return self._list.index(block)
               else: continue
          else:
               self.findBlock(k+1, freeBlocks)
          return self._list.index(block)
          
          
     # method to free memory
     def free(self, request: Request) -> None:
          print('freeing memory')
          for block in self._list:
               if block.request == request.reqID:
                    block.free = True
                    block.request = None
                    print('memory freed successfully')
                    self.merge(block)
                    return
          else:
               print('request not currently allocated')
               return
          
     

if __name__ == "__main__":
     print('BuddySystem working... begin test')