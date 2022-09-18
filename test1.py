# data = {
#   "EmployeeSummary": {
#     "TableEntry": [
#       {
#         "Id": "000123",
#         "Name": "Chadd Smith",
#         "Designation": "Software Engineer",
#         "Address": {
#           "TemporaryAddress": {
#             "StreetNumber": "2463",
#             "StreetName": "Sw 153rd Dr",
#             "City": "Beaverton",
#             "Region": "Oregon",
#             "PostalCode": "97006",
#             "Country": "USA"
#           },
#           "PermanentAddress": {
#             "StreetNumber": "8963",
#             "StreetName": "Fw 151rd Dr",
#             "City": "Beaverton",
#             "Region": "Oregon",
#             "PostalCode": "97006",
#             "Country": "USA"
#           }
#         },
#         "BloodGroup": "B+ve",
#         "Age": "22"
#       },
#       {
#         "Id": "000124",
#         "Name": "Ben Bruser",
#         "Designation": "Senior Software Engineer",
#         "Address": {
#           "TemporaryAddress": {
#             "StreetNumber": "1263",
#             "StreetName": "Sw 153rd Dr",
#             "City": "Beaverton",
#             "Region": "Oregon",
#             "PostalCode": "97006",
#             "Country": "USA"
#           },
#           "PermanentAddress": {
#             "StreetNumber": "7263",
#             "StreetName": "Fw 151rd Dr",
#             "City": "Beaverton",
#             "Region": "Oregon",
#             "PostalCode": "97006",
#             "Country": "USA"
#           }
#         },
#         "BloodGroup": "B+ve",
#         "Age": "22"
#       }
#     ]
#   }
# }
#
# print(data["EmployeeSummary"]["TableEntry"][0]["Id"])
#
#
# # def sequence(n):
# #   count = 0
# #   lst1 = []
# #   for i range(n):
# #
# # lst1 = []
# # lst2 = []
# # def sequence(n):
# #     if n%2 == 0:
# #         e = int(n/2)
# #         o = int(n/2)
# #         print(e)
# #         print(o)
# #         for i in range(1,e+1):
# #             lst1.append(i*i*i)
# #         for j in range(1, o+1, 3):
# #             lst2.append(j)
# #     print(lst1)
# #     print(lst2)
# #
# # sequence(20)
#
# # lst1 = [1,4,7,10,13]
# # lst2 = [1, 8, 27, 64, 125]
# # lst3 = []
# # for i in range(5):
# #     lst3.append(lst1[i])
# #     lst3.append(lst2[i])
# # print(lst3)
#
#
#
# #
# #   lst = [1,1,4,8,7,27,10,64,13]
# #   for i in range(len(lst)):
# #     if i == n:
# #       return lst[i]
# #     else:
# #       print("Index Out of Range")
# #
# # value = sequence(2)
# # print(value)
#
#
#
# # # Program to generate list dynamically based on requirement and give particular value
# # lst1 = []
# # lst2 = []
# # lst3 = []
# # def sequence(n):
# #     for i in range(1, n+1):
# #         lst1.append(i*i*i)
# #     for j in range(1,3*n,3):
# #         lst2.append(j)
# #     print(lst1)
# #     print(lst2)
# #     for j in range(n):
# #         lst3.append(lst1[j])
# #         lst3.append(lst2[j])
# #     print(lst3)
# #     print(lst3[n])
# #
# #
# # sequence(5)
# #
#
#
#
#
#
# print("Hello")
#
#
#
#
#
#
#
# # print("Hello")
# n = 1, w = 0
# n = 2, w = 1
# n = 3 ways = 2
# n = 4, w = 3
# n = 5 , w = 6
# n = 6, w =
#
#
# 123456
# 12456
# 13456
# 1356
#
#
#
# Write an algorithm to determine if a number n is SMILING.
#
# A SMILING number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are SMILING.
# Return true if n is a SMILING number, and false if not.
#
#
# Example 1:
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
# Example 2:
# Input: n = 2
# Output: false
# 2^2 = 4
# 4^4 = 16
# 1^2 + 6^2 = 37
# 3^2 + 7^2 = 58
#
# def smilie(n):
#     sum_col = []
#     s = str(n)
#     l = list(s)
#     sum = 0
#     for i in l:
#         sum += int(i) * int(i)
#     print(sum)
#     while sum != 1:
#         print(sum)
#         s1 = str(sum)
#         l = list(s1)
#         sum = 0
#         for i in l:
#             sum += int(i)*int(i)
#         if sum in sum_col:
#             return False
#         col = sum_col.append(sum)
#
#     return True
# print(smilie(2))
#
#
#
# input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
# print(list(set([x for x in input_list if input_list.count(x) > 1])))
#
#
#
#
# numbers_x = [10, 20, 30, 40, 10, 30]
#
# def check_list(lst):
#     if lst[0] == lst[-1]:
#         return True
#     else:
#         return False
# print(check_list(numbers_x))
#
#
#
# input_01 = ['xyz', 'abc', '123']
# # output = ['zyx', 'cba', '321']
# output = []
#
# def list_check(lst1):
#     for i in lst1:
#         output.append(i[::-1])
#     print(output)
#
# lst_check()
#
#
#
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
#
# input_01 = ['xyz', 'abc', '123']
# output = []
#
#
# def list_check(lst1):
#     for i in lst1:
#         output.append(i[::-1])
#     print(output)
#
# list_check(input_01)





# print("Hello")


class Calculator:
    def div(self, a, b):
        try:
            c = a/b
        except Exception as e:
            return e
        return c

    def muiltiplication(self, a , b):
        c = a * b
        return c

obj = Calculator()
t = obj.div(4,1)
print(t)
m = obj.muiltiplication(4,5)
print(m)
#
# def test_calculation():
#     obj1  = Calculator()
#     result = obj1.div(4,0)
#     assert result == 2.0

