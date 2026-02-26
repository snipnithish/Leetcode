# priority queue
# removes element based on priority instead of order

# highest priority removed first 
# not normal fifo
# smaller number =highest priorty

# task-1
# task-2
# task-3

# real time example
# hospital emergency room
# cpu task scheduling
# printer task priority
# network packet routing


# normal queue vs priority queue

# heap
# smallest number=highest priority 
# automatic sorting 
# uses heap module

# pseudocode
# insert
# create empty priority queue-create empty list
# insert element with priority
# heap arranges automatically 

# removes
# removes smallest priority element 


# priority example program
# import heapq

# pq=[]

# heapq.heappush(pq,3)
# heapq.heappush(pq,1)
# heapq.heappush(pq,2)

# print ("priority queue",pq)

# print ("removed",heapq.heappop(pq))
# print ("removed",heapq.heappop(pq))
# print ("removed",heapq.heappop(pq))

# 2)example

import heapq

pq=[]

heapq.heappush(2,"medium task")
heapq.heappush(1,"high task")
heapq.heappush(3,"low task")
while pq:
    priority,task=heapq.heappop(pq)
    print(priority,task)
