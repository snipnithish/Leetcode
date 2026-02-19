# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
#     return sorted(s) == sorted(t)
# s=input("Enter the first string: ")
# t=input("Enter the second string: ")
# print("Are the two strings anagrams?", isAnagram(s, t))

# n=int(input("enter the number :"))
# if n!=0:
#     if n==1:
#         print(n)
#         if n==2:
#             print(n)
#         dp=[1]*n
#         dp[1]=2
#         for i in range(2,n):
#             dp[i]=dp[i-1]+dp[i-2]
#         print(dp[-1])
#         print("no steps")

# nums = [0, 1, 3]
# def missingNumber(nums):
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum

# print("The missing number is:", missingNumber(nums))


# nums = [0, 1, 2,4]
# n = len(nums)
# expected_sum = n * (n + 1) // 2
# actual_sum = sum(nums)
# missing_number = expected_sum - actual_sum
# print("The missing number is:", missing_number)

# nums=[2,2,1,1,1,2,2]
# for num in nums:
#     if nums.count(num)>len(nums)//2:
#         print(num)
# #         break

# s="hello world"
# strip=s.strip()
# # split=s.split()
# # len(split[-1])
# print(len(strip))



# s="Hello World"
# strip=s.strip()
# split=strip.split()
# print(len(split[-1]))


# a=[1,2,3,4,5]
# b=[1,2,6,4,5]
# res=[]
# for i in a:
#     if i in b and i not in  res:
#         res.append(i)
# print(res)



a=[1,2,3,4,5]
b=[1,2,6,4,5]
res=[]
for i in a:
    if i not in res:
        res.append(i) 
for i in b:
    if i not in res:
        res.append(i)   
print(res)

l1=[1,2,3,4,5]
l2=[1,2,6,4,5]

m=l1+l2
m.sort()
print(m)