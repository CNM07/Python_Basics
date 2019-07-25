#List Tuple Dictionary

#Lists
person = ['Jane', 'Doe', 30, 65.54, 'Mombasa', True]
print(person[0])
print(person[1])
print(person[2])
print(person[3])
print(person[4])
print(person[5])

print(type(person[0]))
print(type(person[1]))
print(type(person[2]))
print(type(person[3]))
print(type(person[4]))
print(type(person[5]))

print(person[2:4])
print(person[-4:-2])



#Tuples

person_t = ('Jane', 'Doe', 30, 65.54, 'Mombasa', True)
print(person_t)
print(person_t[2:4])
print(person_t[-4:-2])

person[2] = 31
print(person)

# person_t[2] = 31
print(person)

print(person.count('Jane'))
print(len(person))
person.append('HOW_NOW')
print(person)
person.remove('HOW_NOW')
print(person)
person.append('HOW_NOW')
print(person)
person.pop()
print(person)



#dictionaries
#data structure which holds variables in key:value pairs

person_dict = {'first_name': 'Jane', 'Surname': 'Doe', 'age': 31, 'Weight': 65.54, 'Location': 'Mombasa', 'Active': True}
print(person_dict)
print(person_dict['first_name'])
print(person_dict['Location'])
print(person_dict['first_name'], person_dict['Location'])


taskList = [23, 'Jane', ['Lesson 23', 560, {'currency': 'KES'}], 987, (76, 'John')]

#Determine the type of variable taskList is using an inbuilt function
print(type(taskList))

#print KES
print(taskList[2][2]['currency'])

#print 560
print(taskList[2][1])

#Use a function to determine the length of the taskList
print(len(taskList))

#Change 987 to 789 using an inbuilt function

print(str(taskList[3]))
print(str(taskList[3])[::-1])
print(int((str(taskList[3])[::-1])))


