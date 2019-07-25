# A > 79 , B - 60 to 78, C -  59 to 49, D - 48 to 40, E - less 40

def grades(grade):

    if grade >= 79:
        print('A')
    elif grade < 78 and grade >= 60:
        print('B')
    elif grade < 59 and grade >= 50:
        print('C')
    elif grade < 49 and grade >= 40:
        print('D')
    elif grade < 39 and grade >= 0:
        print('E')
    else:
        print('Invalid')
    return grade

grades(45)



def max(list_of_numbers):
    largest = 0
    for i in list_of_numbers:
        if int(i) > int(largest):
            largest = i
    return largest

list2 = [10,5,0,15,20,0,50,5,15]
print(int(max(list2)))

list1 = []
count = 0
number_of_items = int(input('How many numbers are in your list? '))


while count < int(number_of_items):
    j = input('Insert a number into the list: ')
    count += 1
    list1.append(j)

print(str(int(max(list1))) + ' is the largest number in your list!')


x = 0
while x < 5:
    print(x * '*')
    x += 1
y = 4
while y > 0:
    print(y * '*')
    y -= 1

