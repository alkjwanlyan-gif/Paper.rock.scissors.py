# Paper.rock.scissors.py
لعبة حجرة ورقة مقص 
import random
print('welcome to the rock , paper , scissors , games :')
tot = input(' press enter to cotinue or type (Help) for the rules help ').capitalize()

if tot == 'Help':
    print('********* RULES *********\n1)You choose and the computer chooses\n2)Rock smashes Scissors -> Rock wins\n3)Scissors cut Paper -> Scissors win\n4)Paper covers Rock -> Paper wins')
    person_choise = input(' enter your choise (rock , scissors , paper )').lower()
else:
    person_choise = input (" enter your choise (rock , scissors , paper )").lower()

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
      ______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''



choices = [ 'paper' , 'rock' , 'scissors']
computer_choise  = random.choice(choices)

print ('you choise... \n ')
if person_choise == 'paper' :
	print (paper)
elif person_choise == 'scissors' :
	print (scissors)
elif person_choise == 'rock' :
	print (rock)
else:
	print (' please enter rock , paper , scissors ')
	
print (' comuter choise... \n ')
if computer_choise == 'paper' :
	print (paper)
elif computer_choise == 'scissors' :
	print (scissors)
else:
	print (rock)


if computer_choise == person_choise :
	print ('draw')
elif person_choise == 'rock' and computer_choise == 'scissors' or person_choise == 'paper' and computer_choise == 'rock' or person_choise == 'scissors' and computer_choise == 'paper' :
	print ('you win !')
else:
	print ('you lose ')
