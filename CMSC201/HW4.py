#CMSC 201 Homework 4
#Nicole Attram - April 30, 2024

#PROBLEM 1

# p = [1,1,1]
#
# goal = int(input('What number do you want to reach in the Padovan sequence? '))
#
# if goal == 1:
#     print('It takes 1 step to reach your goal number: ' + str(goal))
# else:
#     while p[-1] < goal:
#         p.append(p[-2]+p[-3])
#     print('It takes ' + str(len(p)) + " steps to reach your goal number: " + str(goal))

#PROBLEM 2

# list = input('Please input a comma separated list: ')
# items = list.split(',')
# num = ['1','2','3','4','5','6','7','8','9','0']
#
# for l in items: #goes through each item in list
#     for n in num: #goes through wach number
#         if n in l: #checks for each number in the item
#             print(l,n)
#             items.remove(l) #removes all items with numbers
#
# reverse = []
# while len(items) != 0:
#     reverse.append(items[-1])
#     items.remove(items[-1])
#
# print(reverse)


#PROBlEM 3
# import sys
# from random import choice, seed
#
# if len(sys.argv) >= 2:
#    seed(sys.argv[1])
#
# if __name__ == '__main__':
#     the_choice = choice(['rock', 'paper', 'scissors'])
#     user = input('Please pick rock, paper, or scissors to play. Type stop to end play. ')
#
#     while user.lower() != 'stop':
#         if user.lower() == 'rock' and the_choice == 'scissors':
#             print('You win because '+user+' cruhses '+the_choice)
#         elif  the_choice == 'rock' and  user.lower() == 'scissors':
#             print('You lose because '+the_choice+' cruhses '+user)
#
#         elif user.lower() == 'paper' and the_choice == 'rock':
#             print('You win because ' + user + ' covers ' + the_choice)
#
#         elif the_choice == 'paper' and user.lower() == 'rock':
#             print('You lose because ' + the_choice + ' cruhses ' + user)
#
#         elif user.lower() == 'scissors' and the_choice == 'paper':
#             print('You win because ' + user + ' covers ' + the_choice)
#
#         elif the_choice == 'scissors' and user.lower() == 'paper':
#             print('You lose because ' + the_choice + ' cruhses ' + user)
#         else:
#             print("It's a tie")
#
#         print(the_choice, user)
#         user = input('Please pick rock, paper, or scissors to play. Type stop to end play. ')
#         the_choice = choice(['rock', 'paper', 'scissors'])

# PROBLEM 4

# if __name__ == '__main__':
#
#     user = input('What do you want to add? ') #beigns burger creation
#     toppings = [] #creates an empty array for toppings
#     num = 0
#     burger = 'hamburger'
#
#     while user.lower() != 'bottom bun':
#
#         print('You need to start with the bottom bun!')
#         user = input('What do you want to add? ')
#
#     if user.lower() == 'bottom bun':
#         while user.lower() != "top bun":
#             toppings.append(user)  # adds topping to list
#
#             if user.lower() == 'burger':
#                 num += 1
#             elif user.lower() == 'cheese':
#                 burger = 'cheeseburger'
#                 toppings.remove(user) #removes cheese from topping
#
#             elif user.lower() == "bottom bun":
#                 toppings.remove(user)
#
#             user = input('What do you want to add? ')
#         print('You have created a ' + str(num) + '-' + burger + ' with the toppings', end=' ')
#         for t  in toppings:
#             print(t, end=", ")
#         print("thank you for ordering.")

#PROBLEM 5
import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])
    randint(1, 100)

if __name__ == '__main__':
    guess = int(input('Please guess a number between 1 and 100: '))
    tries = 1 #Sets number of tries to 1 after the first guess
    choice = randint(1, 100)

    while guess != choice:
        if guess > choice:
            print('Your guess is too high')

        elif guess < choice:
            print('Your guess is too low')

        guess = int(input('Please guess a number between 1 and 100: '))
        tries += 1  # adds a try to each guess

    if guess == choice:
        print("You guessed it! And it only took you", tries, 'tries!')