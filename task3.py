#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.

a = [0, 5, 10, 15, 20, 25, 30, 35]
b = []


def first_last(list1):

    for i in list1:
        if i == list1[0] or i == list1[-1]:
                b.append(i)
    return b

print(first_last(a))