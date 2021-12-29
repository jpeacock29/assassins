import random
import time
import unittest
import os

PROMPT = """Welcome Assasin! Your fellow Assasins are:
{}\n
Type in your name only! Then hit "enter". Your target's name will be displayed for {} seconds."""

class AssassinsGame:


    def __init__(self, player_file):
        """
        player_file: str
            A plain text file with one player name per line.
        """

        self.DISPLAY_SECONDS = 3
        self.prompt = PROMPT

        # read each line of the player_file as a player
        with open(player_file) as f:
            self.players = f.read().splitlines()

        # check if the given list of players contains duplicates
        if len(self.players) != len(set(self.players)):
            raise ValueError('The list of players at {} contains duplicates!'\
                .format(player_file))

        # add the list of players to the prompt string
        players_string = ', '.join(self.players)
        self.prompt = self.prompt.format(players_string, self.DISPLAY_SECONDS)

        # shuffle the player list
        random.shuffle(self.players)

        # rewrite the shuffled list to ensure availability if the program
        # is interrupted
        with open(player_file, 'w') as f:
            f.write('\n'.join(self.players))

        self.main_event_loop()

    def main_event_loop(self):

        while True:

            print(self.prompt)

            # loop to get acceptable name
            while True:
                name = input()

                if name == 'q':
                    break

                try:
                    name_index = self.players.index(name)

                except ValueError:
                    print("There's no assasin by that name! Try again:")
                    continue
                break

            target = self.players[name_index - 1]
            print("You need to assasinate {}".format(target))

            # Display the assasin's target
            time.sleep(self.DISPLAY_SECONDS)
            # Clear the screen
            os.system('clear')

AssassinsGame('players.txt')
