#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.my_move = 0
        self.their_move = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        user_input = input("What would you like to throw?\n")
        user_input = user_input.lower()
        while user_input not in ['rock', 'paper', 'scissors', 'q']:
            user_input = input("Enter a valid choice, Please:\n")
        if user_input == "q":
            exit()
        else:
            return user_input


class ReflectPlayer(Player):

    def move(self):
        if self.their_move == 0:
            return "paper"
        else:
            return self.their_move


class CyclePlayer(Player):

    def move(self):
        if self.my_move == "rock":
            return "scissors"
        elif self.my_move == "scissors":
            return "paper"
        else:
            return "rock"


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"CPU: {move1}  User: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        result1 = beats(move1, move2)
        result2 = beats(move2, move1)
        if result1 is True:
            self.p1_score += 1
            print("CPU win!\n User : " + str(self.p2_score) + " \
 | CPU : " + str(self.p1_score))

        else:
            if result2 is True:
                self.p2_score += 1
                print("You win!\n User : " + str(self.p2_score) + " \
 | CPU : " + str(self.p1_score))
            else:
                print("It's a tie!!\n User : " + str(self.p2_score) + " \
 | CPU : " + str(self.p1_score))

    def play_game(self):
        round_times = 0
        while True:
            try:
                round_times = int(input("How many rounds do you want play\
 enter a number From 1 - 10:\n"))
                if round_times in range(1, 10):
                    break
            except ValueError:

                print("That was no valid number.  Try again...")

        print("Game start!")
        for round in range(round_times):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        if self.p1_score > self.p2_score:
            print ("CPU won!!\n Final Score:: CPU :\
" + str(self.p1_score) + " | User : " + str(self.p2_score))
        elif self.p2_score > self.p1_score:
            print ("You win!!\n Final Score:: User :" + str(self.p2_score) + "\
 | CPU : " + str(self.p1_score))
        else:
            print ("it's a tie!!\n Final Score:: User :\
" + str(self.p2_score) + " | CPU : " + str(self.p1_score))


if __name__ == '__main__':
    user_choice = input("Which mode do you want to play with:\n\
  random, reflect, reapet, cycle or q to quit:\n ")
    user_choice = user_choice.lower()
    while user_choice not in ["random", "reflect", "reapet", "cycle", "q"]:
        user_choice = input("Enter valide choice, Please:\n")

    if user_choice == "random":
        game = Game(RandomPlayer(), HumanPlayer())
        game.play_game()

    elif user_choice == "reflect":
        game = Game(ReflectPlayer(), HumanPlayer())
        game.play_game()

    elif user_choice == "reapet":
        game = Game(Player(), HumanPlayer())
        game.play_game()

    elif user_choice == "cycle":
        game = Game(CyclePlayer(), HumanPlayer())
        game.play_game()
    elif user_choice == "q":
        exit()
