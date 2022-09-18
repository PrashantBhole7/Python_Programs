# # A series of numbers in which each number is sum of two presceding numbers
# # 0 1 1 2 3 5 8 13
#
# n1 = 0
# n2 = 1
#
# print(n1)
# print(n2)
#
# for i in range(2, 10):
#     sum = n1 + n2
#     print(sum)
#     n1 = n2
#     n2 = sum
#
#
#






n1 = 0
n2 = 1
lst = []
lst.append(n1)
lst.append(n2)
for i in range(2, 10):
    sum = n1 + n2
    lst.append(sum)
    n1 = n2
    n2 = sum
print(lst)