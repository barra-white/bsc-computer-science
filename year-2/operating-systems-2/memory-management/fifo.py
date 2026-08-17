class FIFO:
    """
    A queue using a python list, with an internal head pointer.
    End of the list is the end of the queue.
    """
    def __init__(self):
        self.body: list[int] = []
        self.head: int = 0
        
    def __str__(self):
        '''
        method to represent the FIFO queue in string format
        '''
        output = '<-'
        i = self.head
        while i < len(self.body):
            output = output + str(self.body[i]) + '\n--<<--'
            i = i+1
        output = output +'<'
        return output
    
    def fragmention(self): 
            """
            Return the total fragmention in the queue.
            """
            return sum(self.body.size)
    
    def clear(self):
        """
        Remove all items from the queue.
        """
        self.body = []
        self.head = 0
    
    def enqueue(self, page):
        """
        Add an page to the replacement queue.
        """
        self.body.append(page)

    def dequeue(self):
        """
        Return (and remove) the page in the queue for longest.
        """
        if self.length() == 0:
            print('no pages in queue')
            return
        page = self.body[self.head]
        self.body[self.head] = None
        self.head = self.head + 1
        return page
    
    def length(self) -> int:
        """
        Return the number of items in the queue.
        """
        return len(self.body) - self.head
    
    def first(self) -> int:
        """
        Return the first item in the queue.
        """
        return self.body[self.head]
    
class Page:
     """
     Class to represent a page.
     """
     def __init__(self, page: int, size: int, request=None):
          #variable to keep track of request
          self.request = None
          # variable for page size
          self.size = size
          # variable for page number
          self.page = page
          # variable for page fault
          self.fault = False

     def __str__(self):
          """
          method to represent the page in string format
          """
          return f'\nPage: {self.page}\nSize: {self.size}\nRequest: {self.request}\nFault: {self.fault}'

     def checkFault(self, queueBody) -> None:
          """
          Return True if page is not in the queue.
          """
          print('checking for page fault')
          for i in queueBody:
               if i == self.page:
                    self.fault = False
                    print('page fault not found')
               else:
                    self.fault = True
                    print('page fault found')
                    break

     def add(self, queueBody: list) -> None:
          """
          Add page to the queue.
          """
          if len(queueBody)-1 == 0:
               print('no pages in queue')
               return
          queueBody.append(self.page)

     def remove(self, queueBody: list) -> None:
          """
          Remove page from the queue.
          """
          if self.size == 0:
               print('no pages in queue')
               return
          queueBody.remove(self.page)
     
     def inMainMemory(self, mainMemPages: list, page) -> bool:
          """
          Check if a page is in main memory
          """
          print('scanning main memory')
          # variable to keep track of whether the page is in main memory
          for i in mainMemPages:
               if i == page:
                    print('page found in main memory')
                    return True
               else:
                    print('page not found in main memory')
                    return False
          
    
     def loadPage(self, mainMem: list) -> None:
          """
          Load a page into main memory
          """
          #check if page is in main memory
          if not self.inMainMemory:
               print('page already in main memory')
               return
          else:
               print('loading page')
               # if not load page
               mainMem.append(self.page)
               print('page loaded successfully')

     def unloadPage(self, mainMem: list) -> None:
          """
          Unload a page from main memory
          """
          #check if page is in main memory
          if self.inMainMemory:
               print('unloading page')
               #unload page
               mainMem.remove(self.page)
               print('page unloaded successfully')
          else:
               # else exit
               print('page not in main memory')
               return

if __name__ == "__main__":
     print('FIFO working... begin test')