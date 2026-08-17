from buddy_system import *
from fifo import *

b = BuddySystem(4096)
b.split(b.root)
f = FIFO()

# method to test buddy system
def buddySystemTest():
        # variable for free blocks
        freeBlocks = b.getFreeBlocks()

        # allocate memory to requests
        b.allocate(Request(1, 4), freeBlocks)
        b.allocate(Request(2, 8), freeBlocks)
        b.allocate(Request(3, 16), freeBlocks)
        b.allocate(Request(4, 32), freeBlocks)
        b.allocate(Request(5, 64), freeBlocks)
        
        # print tree
        print("\n")
        print(b)
        print("\n")

        # allocate memory to requests
        b.allocate(Request(6, 128), freeBlocks)
        b.allocate(Request(7, 256), freeBlocks)
        b.allocate(Request(8, 512), freeBlocks)
        b.allocate(Request(9, 1024), freeBlocks)
        b.allocate(Request(10, 2048), freeBlocks)

        # free memory (deallocate)
        b.free(Request(1, 4))
        b.free(Request(2, 8))
        b.free(Request(3, 16))
        b.free(Request(4, 32))
        b.free(Request(5, 64))

        # print tree
        print("\n")
        print(b)
        print("\n")

def pageReplacementTest():
        
        mainMemory = []
        # add requests to FIFO
        f.enqueue(Page(1, 4))
        f.enqueue(Page(2, 4))
        f.enqueue(Page(3, 4))
        f.enqueue(Page(4, 4))
        f.enqueue(Page(5, 4))

        # print FIFO
        print(f)

        # add requests from FIFO
        f.enqueue(Page(6, 4))
        f.enqueue(Page(7, 4))
        f.enqueue(Page(8, 4))
        f.enqueue(Page(9, 4))
        f.enqueue(Page(10, 4))

        # check for fault
        Page(6, 4).checkFault(f.body)

        # print FIFO
        print(f)

        # load page into main memory
        Page(7, 4).loadPage(mainMemory)

        print(mainMemory)

        # check if page is in main memory
        Page(7, 4).inMainMemory(mainMemory, Page(7, 4))

        # unload from main memory
        Page(7, 4).unloadPage(mainMemory)

        # print FIFO
        print(f)

        # clear FIFO queue
        f.clear()

        # print FIFO
        print(f)


buddySystemTest()

#pageReplacementTest()