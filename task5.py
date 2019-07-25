#With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
# write a program to print the first half values in one line
# and the last half values in one line.

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12)
x = int(len(a)/2)
print(x)


b = a[:x]
c = a[x:]
print(b)
print(c)


a = (1)
def half_list(list):
    x = int(len(a) / 2)

    if type(list) is tuple:
        print('NO!')
    else:
        b = list[:x]
        c = list[x:]
        print(b)
        print(c)

        return b, c

(half_list(a))

# \n