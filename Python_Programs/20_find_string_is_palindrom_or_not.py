# Approach 1: a. First reverse the string
            # b. then check original string and reverse string is same or not

# s = input("Enter a String: ")
# rev_str = s[::-1]
#
# if rev_str == s:
#     print("String is Palindrom")
# else:
#     print("String is not Palidrom")


# Approach 2 :
# function to check string is
# palindrome or not
def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


# main function
s = "malayalam"
print(len(s)-0-1)
print(s[0])
print(s[len(s) - 0 - 1])
print(int(len(s)/2))
# ans = isPalindrome(s)
#
# if (ans):
#     print("Yes")
# else:
#     print("No")