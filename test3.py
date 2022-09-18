# print("Hello")

# str = "Hello World"
# lst = list(str)
# unique_list = []
# for i in lst:
#     if i not in unique_list:
#         unique_list.append(i)
# s1 = "".join(unique_list)
# print(s1)




#
# lst = [12,1,2,3,4,5,6,7,8,9,10]
# k =2
# n = len(lst)
# for i in range(n):
#     for j in range(i+1, n):
#         if lst[i] - lst[j] == -k or lst[i] - lst[j] == k :
#             print(lst[i], lst[j])






#
# # print("Hello")
# lst = [1,4,7,3,8,9,2]
# # output = [False, True, False, True, False, True]
# output = []
# n = len(lst)
# def sum_check(lst):
#     for i in range(n-1):
#         # print(lst[i],lst[i+1])
#         if (lst[i] + lst[i+1]) == 11:
#             output.append(True)
#         else:
#             output.append(False)
#     print(output)
#
# sum_check(lst)


# Given a string representing an organizational hierarchy, it needs to be converted in different format using python. Attempt any 1 outputHere is how an employee information looks like in the String.
#
# <employee_id>:<Employee_name>:<manager_id>
#
# Input String
# #
# input = "1:Max:4, 4:Ann:0, 2:Jim:4, 3:Tom:1"
# # output = [Tom, Max, Jim, Ann,]
# lst_str = input.split(",")
# inter_list = []
# output = []
# print(lst_str)
# for i in lst_str:
#     l = i.split(":")
#     inter_list.append(l)
# print(inter_list)
# n1 = len(inter_list)
# for j in range(n1):
#     for k in range(n1):
#         if inter_list[j][2] == inter_list[k][0]:
#             output.append(inter_list[j][1])
#             output.append(inter_list[k][1])
# print(output)
#
#     # if j[0][2] == j[1][2] or

# print("Hello")
# lst = [4,5,8,1,45,78, 87,98,56, 56, 45,2]
# max_item = lst[0]
# min_item = lst[0]
# for i in lst:
#     if i > max_item:
#         max_item = i
#     if i < min_item:
#         min_item = i
# print(max_item, min_item)
# unique_list = []
# for i in lst:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)

def fibbo(n):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range(n-2):
        sum = n1 + n2
        print(sum)
        n1 = n2
        n2 = sum

fibbo(15)















































