import sys

#The process class
class Process():
     #a list to keep track of all instances of the process class
     _processes: list = []

     def __init__(self, state, priority, PID, operation, interrupt, function):
          #when created append self to instance list
          self._processes.append(self)
          #variable to show state of the process
          self.state: str = state
          #shows the process priority
          self.priority: int = priority
          #the process ID
          self.PID: int = PID
          #variable to keep track of waiting operation, such as I/O, to be completed
          self.operationCompleted: bool = False
          #variable to keep track of an interrupt occuring
          self.interrupt: bool = False
          #variable to keep track of ig the process has been fully executed
          self.executed: bool = False
          #what the process actually does
          self.function = function()

     #method to execute the process
     def execute(self):
          self.function()
          self.executed = True

     #method to terminate the process
     def terminate(self):
          self.state = 'terminated'
          self._processes.remove(self)

#class for the scheduler
class Scheduler():
     def __init__(self, carSpeed):
          #variable to keep track of what process is currently being executed
          self.running: Process = None
          #list to keep track of processes in the ready state
          self.readyQueue: list[Process] = []
          #list to keep track of processes in the blocked state
          self.blockedQueue: list[Process] = []
          #list to keep track of processes to be intialised
          self.intialisingQueue: list[Process] = []
          #variable to see if the scheduler can intitiate the idle process
          self.idle: bool = False
          #variable to keep track of speed of car to see when the scheduler needs to be activated
          self.carSpeed = carSpeed

     #method to add a process to the ready queue
     def addReadyProcess(self, process):
          if process.state == 'ready':
               self.readyQueue.append(process)

     #method to add a process to the blocked queue
     def addBlockedProcess(self, process):
          if process.state == 'blocked':
               self.blockedQueue.append(process)

     #process id allocation method
     def PIDAllocation(self):
          #as PID 0 and 1 are reserved by the kernel, they will not be allocated as ids
          i: int = 2
          #loop to assign PIDs in order, as each process will always be assigned the same PID
          while i < 7:
               self.intialisingQueue[i].PID = i
               #also gives the base priority when PID allocation first occurs
               self.intialisingQueue[i].priority = i
               i += 1

     #method to start the scheduler when the system is active
     def run(self):
          #assign PID to each process
          self.PIDAllocation()
          #move intialised process to ready queue
          for process in self.intialisingQueue:
               self.readyQueue.append(process)

          #main system loop, runs when system is not idle
          while not self.idle:
               #if there is no processes currently running, run the process with highest priority
               #in the ready queue, then shift up the priority of other processes in said queue
               if self.running == None:
                    for process in self.readyQueue:
                         if process.priority == 1:
                              self.running = process
                              self.readyQueue.remove(process)
                         process.priority += 1

               #loop to manage blocked processes, moving them back to the ready state, and increasing them to the highest priority to ensure complete execution on time
               for process in self.blockedQueue:
                    if process.operationCompleted == True:
                         self.addReadyProcess(process)
                         self.blockedQueue.remove(process)
                         for r in self.readyQueue:
                              r.priority += 1
                         process.priority = 1
               
               #execute the current process
               self.running.execute()

               #while the process is currently running, if it encounters an operation that requires it to be but in the blocked state, it will move to the blocked state and let another process run while this process is waiting on its operation to be completed
               if self.running.interrupt:
                    self.addBlockedProcess
                    self.running.priority = 1
                    self.running.interrupt = False
                    for i in self.blockedQueue:
                         i.priority += 1
                    self.readyQueue.remove(self.running)
                    self.running = None

               #check to see if current running process has completed, and if so, terminate the process and change running variable to none
               if self.running.executed == True:
                    self.running.terminate()
                    self.running = None

               #check to see if there is any processes currently waiting to be executed, if not, system enters idle state
               if self.readyQueue == []:
                    self.idle = True

          #loop while the system is currently idle
          while self.idle:
               #checks for process with PID == 2, as this is the process defined in task one as checking if there is an input from the parking sensor. It then runs the process with PID == 2
               for process in Process._processes:
                    if process.PID == 2:
                         self.running = process

               #if process with PID == 2 has been executed and has detected a signal, the system exits out of the idle state and runs the main loop again
               if process.executed == True:
                    self.idle = False
                    self.run()

               #if the speed of the car has exceeded 20 km/h, the system shuts down entirely
               if self.carSpeed > 20:
                    sys.exit()