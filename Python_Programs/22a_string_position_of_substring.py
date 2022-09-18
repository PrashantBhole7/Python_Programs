# Program to find position of substring in given string

msg = "Welcome to learning python"
sub_str = "to"
ret = msg.find(sub_str)
if ret == -1:
    print("Substring", sub_str, " is not present")
else:
    print(sub_str, "presents at position", ret)
