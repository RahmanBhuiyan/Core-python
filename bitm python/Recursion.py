# !n = n *!n - 1
# !5 = 5 *!5 - 1
# =5 *!4
# =5 * (4 * 3 * 2 * 1)
# =5 * 24
# =120
#
#
# def recurSum(n):
#     if n <= 1:
#         return n
#     return *recurSum(n - 1)


# Driver code
# print(recurSum(5))
#
# this is factorial


# Jok korce


# def recurSum(n):
#     print(n)
#     if n==1:
#         return n
#     return n + recurSum(n-1)
#
#     # Driver code
# print(recurSum(5))


# gun korce


# def recurSum(n):
#     print(n)
#     if n==1:
#         return n
#     return n + recurSum(n-1)
#
#     # Driver code
# print(recurSum(5))


# used list to solve the problem

# L=[1,2,3,4,5]
# for i in L:
#     def chill(i):
#         # print(i)
#         if i==1:
#             return i
#         return i+ chill(i-1)
#     print(chill(i))


L=[100]
for i in L:
    def chill(i):
        # print(i)
        if i==1:
            return i
        return i+ chill(i-1)
    print(chill(i))