# stack -LIFO OR queue -FIFO
# operation 
# push() - add element to stack
# pop() - remove element from stack
# peek() - return top element of stack
# isEmpty() - check if stack is empty
# size() - return number of elements in 


# push-add an item at top
# 1)create empty stack
# 2)input value
# 3)add value to stack
# 4)print stack

# pseudocode
# push(data)
# if(stack is full):
#     print stack OverflowError
# else:
#     top++
#     stack[top or index]=data

# pseudocode
# pop()
# if(stack is empty):
#     print stack underflow
# else:
#     top--
#     stack(arr(top++))data


# peek pseudocode
# peek()
# if (stack is empty):
#     print stack underflow
# else:
#     return arr[top]

# code

# stack=[]

# while True:
#     print("\n1.push 2.pop 3.peek 4.display 5.exit")
#     choice=int(input("enter the choice:"))
#     if choice==1:
#         val=int(input("enter the number:"))
#         stack.append(val)
#         print('pushed',val)
#     elif choice==2:
#         if not stack:
#             print("stack empty")
#         else:
#             print("popped",stack.pop())
#     elif choice==3:
#         if not stack:
#             print("stack empty")
#         else:
#             print("Top")
#     elif choice==4:
#         print("STack",stack)
#     else:
#         print("invalid chioce")
#         break 

# queue opertions
# enqueue-add an item at rear
# dequeue-remove an item from front
# front/peek-view first item
# isEmpty
# size


# queue=[]

# while True:
#     print("\n1.enqueue 2.dequeue 3.peek 4.display 5.exit")
#     choice=int(input("enter the choice:"))
#     if choice==1:
#         val=int(input("enter the number:"))
#         queue.append(val)
#         print('added',val)
#     elif choice==2:
#         if not queue:
#             print("queue empty")
#         else:
#             print("removed",queue.pop())
#     elif choice==3:
#         if not queue:
#             print("queue empty")
#         else:
#             print("front",queue[0])
#     elif choice==4:
#         print("Queue",queue)
#     else:
#         print("invalid chioce")
#         break 

# circular queue-enqueue,dequeue,isEmpty
# 1)reuse empty space
# save memory

# i front is free,rear can resuse it

# n=3
# queue=[None]*n
# front=0
# rear=0

# insertelement in circular queue
# queue[rear]=10
# rear=[rear+1]%size

# important condition 
# queue is full when (rear+1)%size==front
# queue is empty when front==-1
 
# circular movements
# rear=(rear+1)%size
# front=(front+1)%size

# psedocode
# ENQUEUE

# *if queue full->print "queue full"
# *if first element->set front=0
# *move rear circularly
# *insert element

# DEQUEUE

# *if queue empty->print"queue empty"
# *remove front element
# *if last element removed->reset front & rear
# *else move front circularly

# display 
# 1.if empty -> print message
# 2.start from _frozen_importlib
# 3.print until ResourceWarning

# step by step logic
# enqueue steps

# 1.check full condition
# 2.set front if first insert
# 3.move rear using ModuleNotFoundError
# 4.insert missing