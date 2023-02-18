import random
import word_list_from_file


class Wordle:
    def __init__(self, answer: str, legal_guesses: list = [], max_guesses: int = 6) -> None:
        self.legal_guesses: list = legal_guesses
        self.check_legal: bool = legal_guesses != []

        self.guesses: list = []
        self.answer: str = answer.lower()
        self.current_board: str = f"_"*len(answer)  # need to set the default to something with len(answer)

        self.max_guesses: int = max_guesses
        self.final_guess: bool = False
        self.won: int = 0  # 0 for game in progress, 1 for game over and won, 2 for game over and lost

    def correct_guess(self, guess: str) -> bool:
        return guess == self.answer

    def state(self) -> int:
        return self.won

    def num_moves(self) -> int:
        return len(self.guesses)

    def accept_guess(self, guess: str) -> None:
        if self.legal_turn(guess):
            self.guesses.append(guess.lower())
            self.colour_dict(guess)

            if self.correct_guess(guess):
                self.won = 1

            if self.final_guess and not self.correct_guess(guess):
                self.won = 2
        else:
            print("ILLEGAL GUESS")

    def legal_turn(self, guess: str) -> bool:
        """if there's a rule that we need to check legal guesses, returns True if a legal guess was made, else False"""
        # sets final guess to true if this is our last attempt
        self.final_guess = len(self.guesses) + 1 == self.max_guesses

        if len(guess) != len(self.answer):
            return False

        if self.check_legal:
            # print("self.check is true")
            if guess not in self.legal_guesses:
                return False
        return True

    def colour_dict(self, guess: str) -> None:
        output_dict = {}
        local_guess = ""
        local_answer = ""
        for letter_index in range(len(self.answer)):
            # print(f"in loop; index = {letter_index}, answer[{letter_index}] = {self.answer[letter_index]}, guess[{letter_index}] = {guess[letter_index]}")
            if self.answer[letter_index] == guess[letter_index]:
                output_dict[letter_index] = "green"
            else:
                local_guess += guess[letter_index]
                local_answer += self.answer[letter_index]

        for letter_index in range(len(local_guess)):
            if local_guess[letter_index] in local_answer:
                output_dict[letter_index] = "yellow"

        for letter_index in range(len(self.answer)):
            if letter_index not in output_dict:
                output_dict[letter_index] = "grey"

        self.my_string(output_dict, guess)

    def my_string(self, colour_dict: dict, guess: str) -> str:
        """could combine this with colour dict fn bc that's the only way it's ever used"""
        printable_string = ""
        colours = {
            "yellow": "\033[1;30;43m",
            "green": "\033[1;30;42m",
            "grey": "\033[1;30;47m"
        }
        # print(f"dict = \n {colour_dict}")
        for letter_index in range(len(guess)):
            printable_string += colours[colour_dict[letter_index]] + guess[letter_index]
            # print(printable_string)
        printable_string += "\033[0m"
        self.current_board = printable_string
        return printable_string

    def __str__(self) -> str:
        return self.current_board


def run_game(answer: str = None):
    if answer is None:
        legal_words = word_list_from_file.remove_n(word_list_from_file.raw_file("valid-wordle-words.txt"))
        answer = random.choice(legal_words)

    game = Wordle(answer)
    total_guesses = 1
    while game.state() == 0:

        guess = input(f"Enter word guess {len(game.guesses) + 1}: ")
        game.accept_guess(guess)
        print(game)
        total_guesses += 1





if __name__ == '__main__':
    run_game("crane")






