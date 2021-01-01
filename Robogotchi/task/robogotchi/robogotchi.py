from random import randint
from random import seed


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


# Game class
class GameOfNumbers:
    min_num = 0
    max_num = 1_000_000

    def __init__(self):
        self.player_wins = 0
        self.robot_wins = 0
        self.draw_count = 0

    def print_stats(self):
        print(f"\nYou won: {self.player_wins},")
        print(f"The robot won: {self.robot_wins},")
        print(f"Draws: {self.draw_count}.")

    def process_input(self, str_input):
        try:
            int_input = int(str_input)

            if int_input < GameOfNumbers.min_num:
                raise NegativeNumberError
            elif int_input > GameOfNumbers.max_num:
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
        random_num = randint(GameOfNumbers.min_num, GameOfNumbers.max_num)
        robot_input = randint(GameOfNumbers.min_num, GameOfNumbers.max_num)
        print(f"\nThe robot entered the number {robot_input}.")
        print(f"The goal number is {random_num}.")

        usr_abs_value = abs(usr_input - random_num)
        rob_abs_value = abs(robot_input - random_num)

        if usr_input == robot_input:
            self.draw_count += 1
            print("It's a draw!\n")
        elif usr_abs_value < rob_abs_value:
            self.player_wins += 1
            print("You won!\n")
        else:
            self.robot_wins += 1
            print("The robot won!\n")

    def run(self):
        while True:
            print("What is your number?")
            user_input = input()

            if user_input == "exit game":
                self.print_stats()
                return
            else:
                self.process_input(user_input)


def main():
    seed()
    game = GameOfNumbers()
    game.run()


if __name__ == "__main__":
    main()
