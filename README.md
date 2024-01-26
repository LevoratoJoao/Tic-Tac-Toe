# Tic-Tac-Toe

This is a Tic Tac Toe Game using Minimax Algorithm.

## Installation

Install the dependencies using pip3

```bash
pip3 install -r requirements.txt
```

To run the game

```bash
python runner.py
```

## The Game

* S₀: Initial state (in our case, an empty 3X3 board)
* Players(s): a function that, given a state s, returns which player’s turn it is (X or O).
* Actions(s): a function that, given a state s, return all the legal moves in this state (what spots are free on the board).
* Result(s, a): a function that, given a state s and action a, returns a new state. This is the board that resulted from performing the action a on state s (making a move in the game).
* Terminal(s): a function that, given a state s, checks whether this is the last step in the game, i.e. if someone won or there is a tie. Returns True if the game has ended, False otherwise.
* Utility(s): a function that, given a terminal state s, returns the utility value of the state: -1, 0, or 1.

## Minimax Algorithm

A type of algorithm in adversarial search, Minimax represents winning conditions as (-1) for one side and (+1) for the other side. Further actions will be driven by these conditions, with the minimizing side trying to get the lowest score, and the maximizer trying to get the highest score.

### How the algorithm works:

Recursively, the algorithm simulates all possible games that can take place beginning at the current state and until a terminal state is reached. Each terminal state is valued as either (-1), 0, or (+1).

Knowing based on the state whose turn it is, the algorithm can know whether the current player, when playing optimally, will pick the action that leads to a state with a lower or a higher value. This way, alternating between minimizing and maximizing, the algorithm creates values for the state that would result from each possible action.