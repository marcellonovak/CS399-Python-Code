"""
Marcello Novak
Purpose: To simulate a tournament of two different games, Chicago and DoubleRoll, and output winners for each.
Disclaimer: GitHub copilot was used for the program, mostly for the variable/function names and comments
Date: 11/12/2020
Midterm Assignment
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint


# Initialize a dataclass for a player
@dataclass
class Player:
    name: str
    score: int = 0

    # Define a string representation of a player
    def __str__(self) -> str:
        return f"{self.name} ({self.score})"


# Define an abstract base class for a game
class Game(ABC):

    # Initialize a game with a list of players and a counter for the number of games played
    def __init__(self, players: [Player]) -> None:
        self.players = players
        self.gamesPlayed = 0

    # Define a method to return a list of players with the highest score
    def champions(self) -> [Player]:

        # return list of players with the highest score, or an empty list if nobody scored
        if not self.gamesPlayed:
            return []

        # lambda function to return the max score and all players with that score
        max_score = max(self.players, key=lambda player: player.score).score
        return [player for player in self.players if player.score == max_score]

    # All games need to have a play method
    @abstractmethod
    def play(self) -> [Player]:
        pass


# Define a class for the Chicago game
class Chicago(Game):

    # Play method for Chicago
    def play(self) -> [Player]:

        # Set all players' scores to 0 and increment the number of games played
        for player in self.players:
            player.score = 0
        self.gamesPlayed += 1

        # Play the game
        for target in range(2, 12):
            for player in self.players:
                roll = randint(1, 6) + randint(1, 6)
                if roll == target:
                    player.score += target

        # Return a list of players with the highest score
        return self.champions()


# Define a class for the DoubleRoll game
class DoubleRoll(Game):

    # Play method for DoubleRoll
    def play(self) -> [Player]:

        # Set all players' scores to 0 and increment the number of games played
        for player in self.players:
            player.score = 0
        self.gamesPlayed += 1

        # Play the game
        for target in range(2, 12):
            for player in self.players:

                # Create two separate dice rolls
                roll1 = randint(1, 6)
                roll2 = randint(1, 6)
                if roll1 + roll2 == target:
                    player.score += target

                # Allow for re-roll is target not met
                else:
                    # Re-roll the lower of the two dice
                    if roll1 > roll2:
                        roll2 = randint(1, 6)
                    elif roll1 < roll2:
                        roll1 = randint(1, 6)
                    # Or pick the first die to re-roll if they are equal
                    else:
                        roll1 = randint(1, 6)

                    # Add the new rolls to the player's score if they match the target
                    if roll1 + roll2 == target:
                        player.score += target

        # Return a list of players with the highest score
        return self.champions()


# Create a list of players
contestants = [
    Player("Ricky Bell"),
    Player("Michael Bivins"),
    Player("Bobby Brown"),
    Player("Ronnie DeVoe"),
    Player("Johnny Gill"),
    Player("Ralph Tresvant")
]

# Play Chicago until at least two players win
chicagoGame = Chicago(contestants)

# Initialize a list to hold the final winners
finalWinners = []

# Play the game until at least two players win
while len(finalWinners) < 2:
    finalWinners = chicagoGame.play()
print(f"After {chicagoGame.gamesPlayed} Chicago games played, a single game had multiple winners:")
for finalist in finalWinners:
    print(f"{finalist.name}, Score: {finalist.score}")

# Spacer
print()

# Play DoubleRoll until at least two players win
doubleRollGame = DoubleRoll(contestants)

# Initialize a list to hold the final winners
finalWinners = []

# Play the game until at least two players win
while len(finalWinners) < 2:
    finalWinners = doubleRollGame.play()
print(f"After {doubleRollGame.gamesPlayed} DoubleRoll games played, a single game had multiple winners:")
for finalist in finalWinners:
    print(f"{finalist.name}, Score: {finalist.score}")
