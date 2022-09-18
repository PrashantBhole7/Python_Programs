# Approach 1: reverse():
# my_list = [10, 20, 30 ,40, 50, 60]
# print("My list before reverse: ", my_list)
# my_list.reverse()
# print("My list after reverse: ", my_list)

# Approach 2: using slicings
my_list = [10, 20, 30 ,40, 50, 60]
print("My list before reverse: ", my_list)
my_list = my_list[::-1]
print("My list after reverse: ", my_list)


# Approach 3:
# input list
lst = [10, 11, 12, 13, 14, 15]
# the above input can also be given as
# lst=list(map(int,input().split()))
l = []  # empty list

# iterate to reverse the list
for i in lst:
    # reversing the list
    l.insert(0, i)
# printing result
print(l)