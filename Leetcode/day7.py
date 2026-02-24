
# 118,119) pascals triangle

# numrow=int(input("enter the number:"))
# triangle=[]
# for i in range(numrow):
#     row=[1]*(i+1)
#     for j in range(1,i):
#         row[j]=triangle[i-1][j-1]+triangle[i-1][j]
#     triangle.append(row)
# print(triangle)

# a=[1,2,3,4,5]
# b=[1,2,5,6,7]
# res=[]
# for i in a:
#     if i in b and i not in res:
#         res.append(i)
# print(res)

# def detectcapital (word):
#     return (
# word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()))

# sol=solution()
# word=input("enter the word:")

# 13 roman to integer
# roman = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }
# s=input("enter the roman numeral:")
# total=0
# for i in range(len(s)):
#     value=roman[s[i]]
#     if i+1<len(s) and roman[s[i+1]]>value:
#         total-=value
#     else:
#         total+=value        
# print("The integer value is:", total)

# 628. Maximum Product of Three Numbers
# nums=[1,2,3]
# nums.sort()
# max_product=max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
# print("The maximum product of three numbers is:", max_product)


class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        
        for i in range(n + 1):
            if i not in nums:
                return i
nums = [0, 1, 2, 4]
solution = Solution()
print(solution.missingNumber(nums))

