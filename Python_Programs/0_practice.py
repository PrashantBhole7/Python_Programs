# # Swapping
# num1 = 7
# num2 = 8
# temp = num1
# num1 = num2
# num2 = temp
#
# num1 , num2 = num2, num1
#
# # prime number:
# 2,3, 5, 7, 11
# num = int(input())
# count = 0
# if num > 1:
#     for i in range(1,num+1):
#         if num%i == 0:
#             count = count + 1
#     if count == 2:
#         print("Number is prime")
#     else:
#         print("Number is not prime")
# else:
#     print("Number is not prime")
#
# # Factoral of given number_by_iterative
#
# num = 5
# fact_value = 1
# for i in range(1,num+1):
#     fact_value = fact_value * i
#     i = i - 1
# print(fact_value)
#
# # fibonacci_numbers:
# a = 0, 1,1,2,3,5,8,13
# n1 = 0
# n2 = 1
# print(n1)
# print(n2)
#
# # factorial of given number by recurrcive approach
# num = int(input("Enter the number which you want to find factorial"))
#
# def factorial(n):
#     if n == 0 or n== 1:
#         return 1
#     elif n < 0:
#         return "factorial does not exist"
#     else:
#         return n * factorial(n-1)
# fact = factorial(num)
# print("Factorial of given number is :", fact)
# for i in range(2, 10):
#     sum = n1 + n2
#     print(sum)
#     n1 = n2
#     n2 = sum
#
# # Swap any element of the list
# myList = [1, 4, 23 ,32, 34]  # index starts from 0
# print("List before swapping: ", myList)

#
#
# l1 = [12, 23, 45, 12, 23, 56, 67, 45, 78, 49]
# max_ele = max(l1)
# print(max_ele)
# second_max = l1[0]
# for i in range(len(l1)):
#     if l1[i]>second_max and l1[i] != max_ele:
#         second_max = l1[i]
# print("Second Max elememtn in list is :", second_max)



# l1 = (12, 34, [1,2,3], 45, 67, [4,5,6])
# print(l1)
# print(l1[2])
# l1[2][0] = 23
# print(l1)


# # # # num = 10
# # # # def show_num():
# # # #     global num
# # # #     num = 20
# # # #     print("show num ", num)
# # # # show_num()
# # # # print("Outside of show_num ", num)
# # #
# # # l1 = [4, 6, 34, 23, 12, 78, 3]
# # # # m = min(l1)
# # # # l2 = []
# # # # l2.append(m)
# # # # for i in range(len(l1)):
# # # #     m2 = max(l2)
# # # #     if l1[i] > m2:
# # # #         l2.append(l1[i])
# # # # print(l2)
# # # # # print(l1[3])
# # # # l2 = []
# # # # for i in range(len(l1)):
# # # #     m = min(l1)
# # # #     l2.append(m)
# # # #     l1.remove(m)
# # # # print(l2)
# # # #
# # # # n= 4
# # # # for i in range(n):
# # # #     print(" "* (n-i)," * "*(i+1))
# # #
# # # def outer(func):
# # #     def inner(name):
# # #         if name == "Rakesh":
# # #
# # #         print("How are you")
# # #         func()
# # #         print("Chetan")
# # #     return inner()
# # #
# # #
# # #
# # # @outer
# # # def hello(name):
# # #     print("Hello", name)
# # #
# # # hello()
# #
# #
# # class A:
# #     name = "sudhir"
# #     def show(self):
# #         print("I am in show")
# #         print(A.name)
# #
# # a = A()
# # a.show()
# # a1 = A()
# #
# #
# #
# #
# #
# #
# #
# #
#
#
# class A:
#     def __init__(self):
#         print("I am in Parent class constructor")
#
#     def show(self):
#         print("I am in A")
# class B:
#     def show(self):
#         print("I am in B")
# class C(A,B):
#     def __init__(self):
#         print("I am in child class constructor")
#         super().__init__()
# c = C()
# c.show()










# class X:
#     def __init__(PrashantB):
#         print("first constrcutor")
#
#     def __init__(Prashant):
#         print("Second constrcutor")
# x = X()


# l = [[[[1,2]]],[3]],[[[4]]]
# print(type(l[0]))
# print(l)
# print(l[0][0][0][0][0])
# print(l[0][0][0][0][1])
# print(l[0][1][0])
# print(l[1][0][0][0])
# for i in range(len(l)):
#     if type(l[i])









# op = []
# l = [[[[1,2]]],[3]],[[[4]]]
#
# def get_integers(l2):
#     for x in l2:
#         if type(x) == list:
#             get_integers(x)
#         else:
#             op.append(x)
# get_integers(l)
# print(op)

#
# # input = "a1b2c3d4a2"
# # output= "abbcccddddaa"
# output = ''
# def str_cmp(s):
#     for i in s:
#         if i.isalpha():
#             global output
#             output = output + i
#             previous = i
#         else:
#             num = previous*(int(i)-1)
#             output += num
#     print(output)
#
# str_cmp("a1b2c3d4a2")





# input = "abbcccdddd"
# Output = "a2b2c3d4"
# Approach 1
# str = "abbcccdddd"
# list = list(str)
# unique_list = []
# for i in list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(f"{str} = ", end=" ")
# for j in unique_list:
#     print(f"{j}{list.count(j)}", end="", sep="")

# Approach 2
# my_str = "abcdabcdeeefffgggggaa"
# d = {}
# for x in my_str:
#     if x in d.keys():
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1
# print(f"{my_str} = ", end="")
# for k,v in d.items():
#     # print("Occurences of character {} = {} times".format(k,v))
#     print(f"{k}{v}", end="")





# # input= "abbcccddddaa"
# # output = "a1b2c3d4a2"




# Program to sort the words in string
# input = "python is very easy language"
# output = "easy is language python very"
# input = "python is very easy language"
# list = input.split()
# list.sort()
# output = " ".join(list)
# print(output)

#
# s = "389214"
# s1 = sorted(s)
# print(s1)  # ['1', '2', '3', '4', '8', '9']
# print(type(s1))  # 'list'
# print(type(s[0]))  # 'str'
# s2 = "ahdbt"
# s3 = sorted(s2)  # ['a', 'b', 'd', 'h', 't']
# print(s3)


# lst = [1, 4, 79, 3, 5, 43, 21]
# # lst.sort()
# # print(lst)
# l1 = sorted(lst)
# print(l1)

# # Sort the list without using sort() or sorted()
# # List of alphabets
# lst = ["g", "d", "t", "a", "d", "j", "k"]
# n = len(lst)
# s_list = []
# # print(min(lst))
# # lst.remove("d")
# print(lst)
# for i in range(n):
#     m = min(lst)
#     s_list.append(m)
#     lst.remove(m)
# print(s_list)



#
# # Sorting list without sort()
# my_list = ["g", "d", "t", "a", "d", "j", "k"]
# # my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
# new_list = []
#
# while my_list:
#     min = my_list[0]
#     for x in my_list:
#         if x < min:
#             min = x
#     new_list.append(min)
#     my_list.remove(min)
#
# print(new_list)
#
# # # lst.sort()
# # print(lst)
# # print(lst[0] > lst[1])  # True
# l1 = [x for x in lst[1:] if x <  lst[0]] + [lst[0]] + [x for x in lst[1:] if x >= lst[0]]
# print(l1)
# l11 = [x for x in l1[1:] if x <  l1[0]] + [lst[0]]
# print(l11)
# l2 = l1 + [lst[0]]
# l22 = [x for x in l2[1:] if x <  l2[0]]
# print(l22)
# print(l2)
# l3 = [x for x in lst[1:] if x >= lst[0]]
# print(l3)
# my_list = ["g", "d", "t", "a", "d", "j", "k"]
# def quicksort(lst):
#     print(lst)
#     if not lst:
#         return []
#     # return (quicksort([x for x in my_list[1:] if x < my_list[0]]) + [lst[0]] + quicksort(
#     #     [x for x in my_list[1:] if x >= my_list[0]]))
#     return (quicksort([x for x in lst[1:] if x < lst[0]])
#             + [lst[0]] +
#             quicksort([x for x in lst[1:] if x >= lst[0]]))
# sorted_list = quicksort(my_list)
# print(sorted_list)
#
# #
# # Python code to count the number of occurrences
# def countX(lst, x):
#     return lst.count(x)
#
# # Driver Code
# lst = [8, 6, 8, 10, 8, 20, 10, 6, 6, 8, 8]
# unique_list = []
# for i in lst:
#     if i not in unique_list:
#         unique_list.append(i)
# for j in unique_list:
#     print(f"{j} ocurres in {lst.count(j)}")




#
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = ["Even" if num%2 == 0 else "Odd" for num in list1]
# print(list2)

#
# # reversing a list
# # input list
# lst = [10, 11, 12, 13, 14, 15]
# # the above input can also be given as
# # lst=list(map(int,input().split()))
# l = []  # empty list
#
# # checking if elements present in the list or not
# for i in lst:
#     # reversing the list
#     l.insert(0, i)
# # printing result
# print(l)


# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = []
# import inflect
# p = inflect.engine()
# for i in list1:
#     word = p.number_to_words(i)
#     list2.append(word)
# print(list2)
# list3 = [p.number_to_words(i) for i in list1]
# print(list3)



#
#
#
# a = 1
# b = 1
# t1 = (1,2,3)
# t2 = (1,2,3)
# l1 = [1,2,3]
# l2 = [1,2,3]
# s1 = {1,2,3}
# s2 = {1,2,3}
# print(a is b)  # true
# print(l1 is l2)  # False
# print(t1 is t2)  # True
# print(s1 is s2)  # False
# print(a == b)  # True
# print(l1 == l2)  # True
# print(t1 == t2)  # True
# print(s1 == s2)  # True

# Conclusion : 1. For Mutable data types if we create two seperate object with same content, these are two seperate objects
              # 2. For Immutable data types if we create two objects with same content then there is only one object two reference variable variable pointing to one object



# Dict:


# Method  # 1 : Using OrderedDict() + reversed() + items()
# This
# method is
# for older versions of Python.Older versions don’t keep order in dictionaries, hence have to converted to OrderedDict to execute this task.

# # Python3 code to demonstrate working of
# # Reverse Dictionary Keys Order
# # Using OrderedDict() + reversed() + items()
# from collections import OrderedDict
#
# # initializing dictionary
# test_dict = {'gfg': 4, 'is': 2, 'best': 5}
#
# # printing original dictionary
# print("The original dictionary : " , test_dict)
#
# # Reverse Dictionary Keys Order
# # Using OrderedDict() + reversed() + items()
# res = dict(reversed(list(test_dict.items())))
#
# # printing result
# print("The reversed order dictionary : " ,res)

# initializing dictionary
# test_dict = {'silver': 4, 'gold': 2, 'diamond': 5}
#
# # printing original dictionary
# print("The original dictionary : " + str(test_dict))
# res = dict(reversed(list(test_dict.items())))
#
# # printing reversed order dictionary
# print("The reversed order dictionary : " + str(res))

s = {1,2,3,4,5,4,3}
print(s)






















































