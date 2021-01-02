from random import randint
from random import seed
from enum import IntEnum


# region Exception classes
class NegativeNumberError(Exception):
    def __str__(self):
        return "\nThe number can't be negative!\n"


class OutOfRangeError(Exception):
    def __str__(self):
        return "\nInvalid input! The number can't be bigger than 1000000\n"


class StringInputError(Exception):
    def __str__(self):
        return "\nA string is not a valid input!\n"

# endregion


# Application class
class Robogotchi:
    player_wins = 0
    robot_wins = 0
    draw_count = 0

    def __init__(self):
        self.rps_game = RockPaperScissors()
        self.numbers_game = Numbers()

        self.robo_name = "Robo"
        self.battery_level = 100
        self.overheat_level = 0
        self.skill_level = 0
        self.boredom_level = 0

    @property
    def overheat(self):
        return self.overheat_level

    @overheat.setter
    def overheat(self, amount):
        self.overheat_level += amount
        if self.overheat_level < 0:
            self.overheat_level = 0
        elif self.overheat_level > 100:
            self.overheat_level = 100

    @property
    def boredom(self):
        return self.boredom_level

    @boredom.setter
    def boredom(self, amount):
        self.boredom_level += amount
        if self.boredom_level < 0:
            self.boredom_level = 0
        elif self.boredom_level > 100:
            self.boredom_level = 100

    @property
    def battery(self):
        return self.battery_level

    @battery.setter
    def battery(self, amount):
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100
        elif self.battery_level < 0:
            self.battery_level = 0

    def change_boredom(self, boredom_amt):
        prev_boredom_lvl = self.boredom
        self.boredom = boredom_amt
        print(f"{self.robo_name}'s level of boredom was {prev_boredom_lvl}. Now it is {self.boredom}.")

    def change_overheat(self, overheat_amt):
        prev_overheat_lvl = self.overheat
        self.overheat = overheat_amt
        print(f"{self.robo_name}'s level of overheat was {prev_overheat_lvl}. Now it is {self.overheat}.")

    def change_battery(self, battery_amt):
        prev_battery_lvl = self.battery
        self.battery = battery_amt
        print(f"{self.robo_name}'s level of the battery was {prev_battery_lvl}. Now it is {self.battery}.")

    @classmethod
    def print_stats(cls):
        print(f"\nYou won: {cls.player_wins},")
        print(f"The robot won: {cls.robot_wins},")
        print(f"Draws: {cls.draw_count}.")

    def print_menu(self):
        print(f"\nAvailable interactions with {self.robo_name}:")
        print("exit - Exit")
        print("info - Check the vitals")
        print("recharge - Recharge")
        print("sleep - Sleep mode")
        print("play - Play\n")

    def run(self):
        print("How will you call your robot?")
        self.robo_name = input()

        is_running = True
        while is_running:
            self.print_menu()
            user_input = input("Choose:\n")
            if user_input == "exit":
                is_running = False
                print("Game over.")
            elif user_input == "info":
                self.print_info()
            elif user_input == "recharge":
                self.recharge()
            elif user_input == "sleep":
                self.sleep()
            elif user_input == "play":
                is_running = self.play()
            else:
                print("\nInvalid input, try again!")

    def print_info(self):
        print(f"{self.robo_name}'s stats are:")
        print(f"battery is {self.battery_level},")
        print(f"overheat is {self.overheat_level},")
        print(f"skill level is {self.skill_level},")
        print(f"boredom is {self.boredom_level}.")

    def recharge(self):
        if self.battery_level == 100:
            print(f"\n{self.robo_name} is charged!")
        else:
            self.change_overheat(-5)
            self.change_battery(10)
            self.change_boredom(5)

    def sleep(self):
        if self.overheat == 0:
            print(f"\n{self.robo_name} is cool!")
        else:
            print(f"\n{self.robo_name} cooled off!")
            self.change_overheat(-20)

    def play(self):
        print("\nRock-paper-scissors or Numbers?")

        is_playing = True
        while is_playing:
            user_input = input()
            print()  # Newline to fit the tests output format

            if user_input.lower() == "numbers":
                is_playing = self.numbers_game.run()
            elif user_input.lower() == "rock-paper-scissors":
                is_playing = self.rps_game.run()
            else:
                print("Please choose a valid option: Numbers or Rock-paper-scissors?\n")

        Robogotchi.print_stats()
        print()
        self.change_boredom(-10)
        self.change_overheat(10)

        if self.overheat == 100:
            print(f"The level of overheat reached 100, {self.robo_name} has blown up! Game over. Try again?")
            return False
        return True


# region Game classes

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

    @staticmethod
    def compute_results(usr_input):
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


class RockPaperScissors:
    moves = ["rock", "paper", "scissors"]

    @staticmethod
    def get_random_hand():
        random_move = randint(0, 2)
        if random_move == Hand.ROCK:
            return "rock"
        elif random_move == Hand.PAPER:
            return "paper"
        elif random_move == Hand.SCISSORS:
            return "scissors"

    @staticmethod
    def compute_result(user_move):
        if user_move not in RockPaperScissors.moves:
            print("\nNo such option! Try again!\n")
            return

        comp_move = RockPaperScissors.get_random_hand()
        print(f"\nRobot chose {comp_move}")

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

# endregion


def main():
    seed()
    app = Robogotchi()
    app.run()


if __name__ == "__main__":
    main()
