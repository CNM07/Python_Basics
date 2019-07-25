#for loops

for x in range(3):
    print(x)

valList = []
for x in range(10):
    valList.append(x)
print(valList)


valList = []
count = 0
for x in range(5):
    valList.append(x)
    count += 1
print(valList)

for i in valList:
    print(i)

new = ['John', 'James', 'Mary']
for name in new:
    print(name)
print(name)

valList = []
for x in range(18):
    if x % 2 == 0 and x % 3 != 0:
        valList.append(x)
print(valList)


#while loop

i = 0
while i <= 10:
    print(i)
    i += 1

i = 0
while i <= 5:
    i += 1
    print(i)

count = 0
while count < len(new):
    print(new[count])
    count += 1


def max(a):
    largest = 0
    for i in a:
        if i > largest:
            largest = i
    return largest

my_list = [1,51,33,8,25,19,0,2,10]
print(max(my_list))

