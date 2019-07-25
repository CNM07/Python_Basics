#Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No".
#Hint: Use input () to get the persons input


word = input('Type a word:' )

if word == 'yes':
    print('Yes')
elif word == 'Yes':
    print('Yes')
elif word == 'YES':
    print('Yes')
else:
    print('No')


word = input('Type a word:').lower()

if word == 'yes':
    print('Yes')
else:
    print('No')




