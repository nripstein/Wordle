from main import Wordle
import random
from typing import Type

class Player:
    def __init__(self, game_instance: Wordle, human: bool = True):
        self.game: Wordle = game_instance
        self.human: bool = human

    def make_guess(self, guess: str):
        self.game.accept_guess(guess)
        print(self.game)
        if self.game.state() == 1:
            print("CORRECT! (IN PLAYER)")
        elif self.game.state() == 2:
            print("GAME OVER, you lose (IN PLAYER)")

    def new_instance(self, game: Wordle):
        self.game = game


class RandomGuesser(Player):
    def __init__(self, game_instance: Wordle):
        super().__init__(game_instance, human=False)

    def random_guess(self):
        """if there are no rules about legal words, can make up random letter combos. guesses one"""
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        selected_letters = random.choices(letters, k=len(self.game.answer))
        super().make_guess("".join(selected_letters))

    def guess_from_words(self, legal_words: list):
        """if there is a list of legal words, this chooses one randomly from the list and guesses it"""
        selected_word = random.choice(legal_words)
        super().make_guess(selected_word)


class StrategyTest:
    def __init__(self, strategy: Type[Player], possible_answers: list):  # make sure player also means any of its children
        self.results: list = []
        self.possible_answers: list = possible_answers

        self.player = None
        self.current_game: Wordle = self.new_game()
        self.player: Player = strategy(self.current_game)

    def new_game(self) -> Wordle:
        selected_word = random.choice(self.possible_answers)
        game = Wordle(selected_word)
        if self.player is not None:
            self.player.new_instance(game)
        return game

    def play_instance(self):
        while self.current_game.state() == 0:
            self.player.guess_from_words(self.possible_answers)  # figure out why pycharm thinks this is wrong
        self.results.append(self.current_game.state())
        if self.current_game.state() == 1:
            print("you win (in test)")
        if self.current_game.state() == 2:
            print("you lose (in test)")

    def many_instances(self, runs: int = 5):
        for i in range(runs):
            self.play_instance()
            #self.new_game()
        print(f"results:\n{self.results}")