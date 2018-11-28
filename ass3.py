"""
Question 3
Rock, Paper, Scissors Game
"""

from random import randint

comp = randint(1, 3)

user = input('Enter your choice of “rock”, “paper” or “scissors”: ')

compchoice = ['rock', 'paper', 'scissors']

compans = compchoice[comp-1]

print('The computer picked %s' % compans)

if user == compans:
    print('Draw!!, the game must be played again to determine the winner')

elif user == 'rock' and compans == 'scissors':
    print('Player / Rock Wins')

elif compans == 'rock' and user == 'scissors':
    print('Computer / Rock Wins')

elif user == 'scissors' and compans == 'paper':
    print('Player / scissors Wins')

elif compans == 'scissors' and user == 'paper':
    print('Computers / scissors Wins')

elif user == 'paper' and compans == 'rock':
    print('Player / paper Wins')

elif compans == 'paper' and user == 'rock':
    print('Computer / paper Wins')

else:
    print('Error')
