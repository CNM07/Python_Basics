#def function is a block of code or statements that performs a certains and returns a result

def addTwoNumbers():
    sum = 34 + 56
    print(sum)
    return sum

addTwoNumbers()

def addTwoNumbers():
    sum = 34 + 56
    return sum

print(addTwoNumbers())


def add(a, b):
    sum = a + b
    return sum

print(add(34,56))

list1 = [5, 10, 4, 12, 7, 9]
print(max(list1))
print(min(list1))

def maximum(a):
   largest = 0
   for i in a:
       if i > largest:
           largest = i
   return largest

list2 = [1,5,8,77,24,95]
print(maximum(list2))



def findTotal(a,b,c,d,e):
    total = a + b + c + d + e
    return total

def findAverage(total):
    average = total/5
    return average

def findGrade(average):
    if average > 50:
        return 'Pass'
    else:
        return 'Fail'

total = findTotal(55,67)