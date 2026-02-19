# a=int(input("Enter the fibanacci number:"))
# a1=0
# a2=1    
# if a<=0:
#     print("Please enter a positive integer")        
# elif a==1:
#     print(a1)
# else:
#     print(a1)
#     print(a2)
#     for i in range(2,a):
#         a3=a1+a2
#         print(a3)
#         a1=a2
#         a2=a3
                

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b

#     return b

# n =int(input("Enter the Fibonacci number: "))
# print("Fibonacci of", n ,"is:", fibonacci(n))


# # list indices
# list=[1,2,3,4,5]
# print(list[4])

# # list slicing makes a new data
# # syntax#[start index(included:end index(excluded)]
# print(list[1:4])

# list operators
# 1) concatenation operators(+)
# list1=[1,2,3]
# # list2=[4,5,6]
# # print(list1+list2)
# # 2) repetition operator(*)
# print(list1*3)
# # 3) membership operator(in or not in)
# fruits=['apple','banana','grapes']
# print('apple' in fruits)
# print('orange'not in fruits)
# # 4) comparison operators(==,!=,>,<,>=,<=)
# list3=[1,2,3]
# list4=[1,2,3]
# print(list3==list4)
# print(list3!=list4)
# print(list3>list4)
# print(list3<list4)
# print(list3>=list4)
# print(list3<=list4)

# examples of list operators
# list1=[1,2,3]
# list2=[4,5,6]
# print(list1[2])
# print(list1[0:2])
# print(list1+list2)
# print(list1*2)
# print(2 in list1)
# print(4 not in list1)
# print(list1==list2)
# print(list1!=list2)

# 5)list methods
# #1) append() method will add an element to the end of the list
# list1=[1,2,3]
# list1.append(4)
# print(list1)
# #2) insert() method will add an element at the specified index
# # syntax: list.insert(index,element)
# list1.insert(2,5)
# print(list1)

# 3) extend() method will add all the elements of the specified list to the end of the current list
# list2=[6,7,8]
# list3=[9,10]
# list3.extend(list2)
# list2.extend(list3)
# print(list3)
# print(list2)

#  4) remove() method will remove the first occurrence of the specified element from the list
# list1=[1,2,3,4,5]
# # list1.remove(4)
# print(list1)

# 5) pop() method will remove and return the element at the specified index
# list1=[1,2,3,4,5]
# list1.pop(2)   
# print(list1)

# 6) clear() method will remove all the elements from the list
# list1=[1,2,3,4,5]
# list1.clear()
# print(list1)

# 7) index() method will return the index of the first occurrence of the specified element in the list
# list=[1,2,3,4,5]
# print(list.index(3))

# # 8) count() method will return the number of occurrences of the specified element in the list
# list1=[1,2,3,4,5,3,3]
# print(list1.count(3))

# 9) sort() method will sort the elements of the list in ascending order
# list1=[5,4,3,2,1]
# list1.sort()    
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# # 10) reverse() method will reverse the order of the elements in the list
# list1.reverse()
# print(list1)

# 11) copy() method will return a shallow copy of the list
# list1=[1,2,3,4,5]
# list2=list1.copy()
# print(list2)

# list1=[1,2,3,4,5]
# list1.append(6)
# print(list1)
# list1.insert(2,7)
# print(list1)
# list2=[8,9,10]
# list1.extend(list2)
# print(list1)
# list1.remove(4)  
# print(list1)
# list1.pop(7)
# print(list1)
# list1.clear()
# print(list1)
# list3=[11,24,13,54,25]
# list3.sort()
# print(list3)
# list3.reverse()
# print(list3)

# map,filter and reduce functions
# 1) map() function will apply a given function to all the items in the list

# num=[1,2,3,4,5,6]
# def function(x):
#     return x*2
# result=list(map(function,num))
# print(result)

# result=list(map(lambda x:x*2,num))
# print(result)

# 2) filter() function will filter the items in the list based on a given function

# num=[1,2,3,4,5,6,7,8,9,10]
# result=list(filter(lambda x:x%2==0,num))
# print(result)

#  3) reduce() function will apply a given function to the items in the list and return a single value
# syntax: reduce(function, iterable)
# from functools import reduce
# num=[1,2,3,4,5]
# result=reduce(lambda a,b:a+b,num)
# print(result)

# from functools import reduce
#  num=[1,2,3,4,5,6,7,8,9,10]
# result=list(filter(lambda x:x%2==0,num))
# print(result)
# result=reduce(lambda a,b:a+b,result)
# print(result)
# result=list(filter(lambda x:x%2!=0,num))
# print(result)
# result=reduce(lambda a,b:a+b,result)    
# print(result)

# palindrome a value that reads the same backward as forward
# word=input("Enter a word: ")
# if word==word[::-1]:
#     print(word,"is a palindrome")
# else:
#     print(word,"is not a palindrome")

# word=input("Enter a word: ")
# rev=""
# for ch in word:
#     rev=ch+rev
# if word==rev:
#     print(word,"is a palindrome")
# else:
#     print(word,"is not a palindrome")

# without using slicing only for numbers

num=int(input("Enter a palindrome number: "))
temp=num
rev=0
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if num==rev:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")
