from random import randint
from random import seed
from enum import IntEnum


# Exception classes
class NegativeNumberError(Exception):
    def __str__(self):
        return "\nThe number can't be negative!\n"


class OutOfRangeError(Exception):
    def __str__(self):
        return "\nInvalid input! The number can't be bigger than 1000000\n"


class StringInputError(Exception):
    def __str__(self):
        return "\nA string is not a valid input!\n"


# Static functions
def print_stats():
    print(f"\nYou won: {Robogotchi.player_wins},")
    print(f"The robot won: {Robogotchi.robot_wins},")
    print(f"Draws: {Robogotchi.draw_count}.")


def get_random_hand():
    random_move = randint(0, 2)
    if random_move == Hand.ROCK:
        return "rock"
    elif random_move == Hand.PAPER:
        return "paper"
    elif random_move == Hand.SCISSORS:
        return "scissors"


# Application class
class Robogotchi:
    player_wins = 0
    robot_wins = 0
    draw_count = 0

    def __init__(self):
        self.rps_game = RockPaperScissors()
        self.numbers_game = Numbers()

    def run(self):
        print("Which game would you like to play?")

        is_running = True
        while is_running:
            user_input = input()
            print()  # Newline to fit the tests output format

            if user_input == "Numbers":
                is_running = self.numbers_game.run()
            elif user_input == "Rock-paper-scissors":
                is_running = self.rps_game.run()
            else:
                print("Please choose a valid option: Numbers or Rock-paper-scissors?\n")


# Game class
class Numbers:
    min_num = 0
    max_num = 1_000_000

    def process_input(self, str_input):
        try:
            int_input = int(str_input)

            if int_input < Numbers.min_num:
                raise NegativeNumberError
            elif int_input > Numbers.max_num:
                raise OutOfRangeError

        except (StringInputError, ValueError):
            print("\nA string is not a valid input!\n")
        except NegativeNumberError as err:
            print(err)
        except OutOfRangeError as err:
            print(err)
        else:
            self.compute_results(int_input)

    def compute_results(self, usr_input):
        random_num = randint(Numbers.min_num, Numbers.max_num)
        robot_input = randint(Numbers.min_num, Numbers.max_num)
        print(f"\nThe robot entered the number {robot_input}.")
        print(f"The goal number is {random_num}.")

        usr_abs_value = abs(usr_input - random_num)
        rob_abs_value = abs(robot_input - random_num)

        if usr_input == robot_input:
            Robogotchi.draw_count += 1
            print("It's a draw!\n")
        elif usr_abs_value < rob_abs_value:
            Robogotchi.player_wins += 1
            print("You won!\n")
        else:
            Robogotchi.robot_wins += 1
            print("The robot won!\n")

    def run(self):
        while True:
            print("What is your number?")
            user_input = input()

            if user_input == "exit game":
                return False
            else:
                self.process_input(user_input)


# Enum class for RockPaperScissors game
class Hand(IntEnum):
    ROCK = 0,
    PAPER = 1,
    SCISSORS = 2


# Game class
class RockPaperScissors:
    moves = ["rock", "paper", "scissors"]

    def compute_result(self, user_move):
        if user_move not in RockPaperScissors.moves:
            print("No such option! Try again!\n")
            return

        comp_move = get_random_hand()
        print(f"Robot chose {comp_move}")

        # TODO: Replace all this logic with dictionary
        # TODO: Replace strings with enums?
        if user_move == comp_move:
            Robogotchi.draw_count += 1
            print("It's a draw!\n")
        elif user_move == "rock":
            if comp_move == "paper":
                Robogotchi.robot_wins += 1
                print("Robot won!\n")
            elif comp_move == "scissors":
                Robogotchi.player_wins += 1
                print("You won!\n")
        elif user_move == "paper":
            if comp_move == "scissors":
                Robogotchi.robot_wins += 1
                print("Robot won!\n")
            elif comp_move == "rock":
                Robogotchi.player_wins += 1
                print("You won!\n")
        elif user_move == "scissors":
            if comp_move == "rock":
                Robogotchi.robot_wins += 1
                print("Robot won!\n")
            elif comp_move == "paper":
                Robogotchi.player_wins += 1
                print("You won!\n")

    def run(self):
        while True:
            print("What is your move?")
            user_input = input().lower()
            if user_input == "exit game":
                return False
            self.compute_result(user_input)


def main():
    seed()
    app = Robogotchi()
    app.run()
    print_stats()


if __name__ == "__main__":
    main()
