#CMSC 201 Homework 3
#Nicole Attram - April 28 - 29, 2024

#PROBLEM 1
items = int(input('What number of items would you like to calculate? '))

i = 1
total = 0

while i <= items:
    total = total +1/(i**2)
    i = i + 1
print(total)

#PROBELM 2
subject = input("Give me a subject: ")

myth = []
lie = []
t = []
f = []

while len(myth) < 5:
    myth.append(input("Please give me a myth regarding "+ subject+': '))
    lie.append(input("Is it actually true that "+myth[len(myth)-1]+ '?: '))

    if lie[len(lie)-1].lower() == 'yes':
        t.append(lie[len(lie)-1])
    else:
        f.append(lie[len(lie)-1])

print("It is following is true about "+subject+" and should not have been included:")

for true in t:
    print(true)

print("It is following is false about "+subject+": ")

for false in f:
    print(false)


#PROBLEM 3

i = int(input("What is the height of your triangle? "))
I = 1

while i > 0:
    print(' '*i+'*'*I)
    i = i - 1
    I = I + 1

#PROBLEM 4

step = int(input("How many steps should we run? "))

cstep = 1
names = []

while cstep <= step:
    com = input('Enter command: ')
    first = com.split() #splits command into individual strings

    if first[0].lower() == "remove": #checks to see if the first word is remove
        removed = first[1]

        if removed in names:
            names.remove(first[1]) #removes second word (name) from list
            print(removed, 'removed')
        else:
            print("Name not present.")

    elif first[0].lower() == "add": #checks to see if the first word is add
        names.append(first[1])
        print(names[len(names) - 1], 'added')

    elif com.lower() == "max":
        max_len = len(names[0])
        max_name = names[0]
        for name in names:
            if len(name) > max_len:
                max_len = len(name)
                max_name = name
        print('The longest name is '+max_name)

    cstep += 1

#PROBLEM 5

months = ('January', "February", 'March', 'April', 'May', 'June', 'July', 'August', 'Sept', 'October', 'November', 'December')

start = int(input('What month are we starting in? '))
travel = int(input('How many months into the future do you want to travel? '))

if start < 1 or start > 12:
    print('Please enter a valid start month. Thank you.')
else:
    end = (start + travel) % 12
    print('You are looking ahead to '+months[end]+'.')