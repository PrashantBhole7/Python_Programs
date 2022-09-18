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
# # print("Hello")
#
# list = [450,357,567,890,90,789,310,650]
# max_item = max(list)
# n = len(list)
# second_max = list[0]
# for i in range(1,n):
#     if list[i] > second_max and list[i] != max_item:
#         second_max = list[i]
# # print(second_max)
# third_max = list[0]
# for i in range(1,n):
#     if list[i] > third_max and list[i] != second_max and list[i] != max_item:
#         third_max = list[i]
# print(third_max)

#
def occurenece_char(c):
    s = "occurrence"
    l = list(s)
    if c not in l:
        return 0
    else:
        chr_occ = l.count(c)
        return chr_occ

print(occurenece_char("a"))





# print("Hello")

# names = ["Amogh", "Prashant", "Vikash", "Prashant", "Vikash", "Vikash"]
# d = {}
# for i in names:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
#
#
# class A:
#     name = "Prashant"
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def test(self, c, d):
#         return c+d
#
# obj = A()


#
# # employee - name salary
# select max(distnct salary) from employee order by salary desc limit 3,2
# select max(salary) from employee where salary <> (select max(salary) from employee))


#
# list1 = [1, 2, 3, 8, 3, 3]
# list2 = [10, 77, 3, 4, 3]
#
# def list_check(lst):
#     r_sum = 0
#     l_sum = 0
#     l = len(lst)
#     for i in range(1,l):
#         for j in range(i+1,l):
#             r_sum += lst[j]
#         for k in range(0,i+1):
#             l_sum += lst[k]
#         if l_sum == lst[i] and r_sum == lst[i]:
#             return lst[i]
#
# print(list_check(list1))














































