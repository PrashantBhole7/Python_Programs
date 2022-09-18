# days = ["m", "t", "w", "th", "f", "st", "su"]
# for i in range(5, 7):
#     print(days[i])

s = "prashant"
r_s = ''
n = len(s)
i = -1
while i >= -n:
    # print(s[i])
    r_s += s[i]
    i = i - 1
print(r_s)
