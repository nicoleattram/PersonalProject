#CMSC 201 Homework 2
#Nicole Attram - April 27, 2024

#PROBLEM 1

mon1_name = input("What is the the name of the first monster: ")
mon1_dam = float(input('How much damage does ' + mon1_name + ' cause: '))
mon1_hit = float(input('How many hit points does '+mon1_name+' cause: '))

mon2_name = input('What is the name of the second monster: ')
mon2_dam = float(input('How much damage does '+mon2_name +' cause: '))
mon2_hit = float(input('How many hit points does '+mon2_name+' cause: '))

if mon2_hit/mon1_dam > mon1_hit/mon2_dam:
    print(mon2_name +' defeates '+ mon1_name)
elif mon2_hit/mon1_dam < mon1_hit/mon2_dam:
    print(mon1_name+' defeats '+mon2_name)
else:
    print("Cat's game! No winner.")

#PROBELM 2

print("Suppose you are a character in Lord of the Rings... Don't tell me. Let me guess. What race are you?")
race =  input('A human, dwarf, elf, maiar and hobbit: ')

if race.lower() == "human":
    king = input('Are you the King of Gondor? Y/N: ')
    if king.upper() == 'Y':
        print("That was easy! Try not to be so obvious next time, Your Highness Aaron, son of Arathorn.")
    else:
        ring = input("Did you try to take the ring from Frodo? Y/N: ")
        if ring.upper() != 'Y':
            print('Now why would you choose an irrelevant character? Choose better than Theoren next time.')
        else:
            print("Ah Ha! You're Boromir.")

elif race.lower() == 'dwarf':
    print("Noble choice,  Gimli son of Gloin.")

elif race.lower() == 'elf':
    matrix = input("Were you in the matrix? Y/N: ")
    if matrix.upper() == 'Y':
        print("Ooo, Elron. Great choice.")
    else:
        print("Ok, so you're Legolas. Am I right?")

elif race.lower() == 'maiar':
    good = input("Are a you good maiar?" )
    if good.upper() == 'Y':
        print("Gandolf is a fantastic character to be. With great power... you know the rest.")
    else:
        forger = input("A villian. Interesting... Did you forge the One Ring?: ")
        if forger.upper() == 'Y':
            print("Sauron is a wicked choice.")
        else:
            print('Saruman is almost worst that Sauron... interesting')

elif race.lower() == 'hobbit':
    carrier = input('Do you carry the One Ring? Y/N ')
    if carrier.upper() == 'Y':
        print('Frodo Baggins... where is it?! Just jokes!')
    else:
        garden = input("Are you a gardener? Y/N ")
        if garden.upper() == 'Y':
            print("I've got it! Samwise.")
        else:
            print("So you picked Merry or Pippin and honestly if doesn't matter which one.")

else:
    print("Orc's are pretty stupid. I don't expect them to follow directions.")

#PROBLEM 3

a = int(input('enter a'))
b = int(input('enter b'))
c = int(input('enter c'))
d = int(input('enter d'))
e = int(input('enter e'))

if a == 0:
    op=False
elif (b == 0 or c == 0) and d == 1 and e == 0:
    op=False
else:
    op=True

print("Based on the inputs, the output is "+str(op))

# PROBLEM 4

val1 = input('Would you like to calculate the \"rotation speed\" or \"radius of the station\"? ')
if val1.lower() == 'rotation speed':
    radius = float(input('What is the radius of the station? '))
    RPM = 60/(2 *3.14)*(9.8/radius)**0.5
    print("the Rotation of the station is "+str(RPM)+" rpm")
else:
    RPM = float(input('What is the rotation speed of the station? '))
    radius = 9.8/(2*3.14*RPM/60)**2
    print("the radius  is "+str(radius)+" meters")

# PROBLEM 5
m = int(input("What month are we in now? "))
if m > 12 or m < 1:
    print("Please provide a valid entry")

else:
    n = int(input("How many months in advance do you want to go? "))
    print("After " +str(n)+" months, you will be in Month "+  str((m+n)%12))