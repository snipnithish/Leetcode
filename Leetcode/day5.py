# 217 contains duplicate
# from pyparsing import nums
# nums=[1,2,3,1]
# def containsDuplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#             seen.add(num)
        
#         return False
# print(containsDuplicate(nums))

# 136) single number
# nums=[2,2,1]
# def singleNumber(nums):
#     result = 0
#     for num in nums:
#         result ^= num
#     return result
# print(singleNumber(nums))


# n=int(input("Enter a number: "))
# if n<=0:
#     print(false)
# else:
#     for i in range(31):
#         if 4**i == n:
#             print("true")
#             break
#         else:
#             print("false")
#             break

# prices=[7,1,5,3,6,4]
# max_profit=0
# buy_daty=0
# sell_day=0
# for i in range(len(prices)):
#     for j in range(i+1,len(prices)):
#         if prices[j]>prices[i]:
#             profit=prices[j]-prices[i]
#             if profit>max_profit:
#                 max_profit=profit
#                 buy_day=i
#                 sell_day=j
# print("Buy on day",buy_day,"and sell on day",sell_day,"for a profit of",max_profit)

# oops funtion
# class student:
#     def details (self,name,mark):
#         if mark>=90:
#             result="pass"
#             print(result)
#             print(name,mark)
#         else:
#             result="fail"
# sl=student()
# s2=student()
# sl.details("sneha",95)
# s2.details("nithish",85)

# class methoad syntax
# lass classname:
#     def methodname(self):
#         print ("message")


# # with constructor
# class classname:
#     def __init__(self):

# class student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def show_result(self):
#         if self.mark>=40:
#             result="pass"
#             print(result)
#             print(self.name,self.mark)
#         else:
#             result="fail"
#             print(result)
# sl=student("sneha",95)
# s2=student("nithish",85)
# sl.show_result()
# s2.show_result()

celcius=[10,20,30,40,50]
fahrenheit=[]
for c in celcius:
    f=(c*9/5)+32
    fahrenheit.append(f)
print(fahrenheit)