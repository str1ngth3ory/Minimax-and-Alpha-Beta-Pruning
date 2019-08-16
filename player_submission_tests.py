#!/usr/bin/env python
import traceback
from player_submission import OpenMoveEvalFn, CustomEvalFn, CustomPlayer
from isolation import Board, game_as_text
from test_players import RandomPlayer, HumanPlayer
import platform

if platform.system() != 'Windows':
    import resource

from time import time, sleep


def main():

    print()
    try:
        sample_board = Board(RandomPlayer(), RandomPlayer())
        # setting up the board as though we've been playing
        board_state = [
            ["Q1", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ","Q2", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " "]
        ]
        sample_board.set_state(board_state,True)
        test = sample_board.get_legal_moves()
        h = OpenMoveEvalFn()
        print('OpenMoveEvalFn Test: This board has a score of %s.' % (h.score(sample_board)))
    except NotImplementedError:
        print('OpenMoveEvalFn Test: Not implemented')
    except:
        print('OpenMoveEvalFn Test: ERROR OCCURRED')
        print(traceback.format_exc())

    print()
    """Example test to make sure
    your minimax works, using the
    OpenMoveEvalFunction evaluation function.
    This can be used for debugging your code
    with different model Board states. 
    Especially important to check alphabeta 
    pruning"""
    # create dummy 5x5 board
    print()
    try:
        def time_left(): # For these testing purposes, let's ignore timeouts
            return 10000
        player = CustomPlayer()
        sample_board = Board(player, RandomPlayer())
        # setting up the board as though we've been playing
        board_state = [
            ["Q1", " ", " ", " ", " ", "X", " "],
            [ " ", " ", " ", " ", " ", " ", " "],
            [ "X", " ", " ", " ", " ", " ", " "],
            [ " ", " ", "X","Q2", "X", " ", " "],   
            [ "X", "X", "X", " ", "X", " ", " "],
            [ " ", " ", "X", " ", "X", " ", " "],
            [ " ", " ", "X", " ", "X", " ", " "]
        ]
        sample_board.set_state(board_state,True)

        test_pass = True

        expected_depth_scores = [(1,3),(2,-4),(3,2),(4,-1),(5,1)]

        for depth, exp_score in expected_depth_scores:
            move, score = player.minimax(sample_board, time_left, depth=depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True)
            if exp_score != score:
                print("Minimax failed for depth: ", depth)
                test_pass = False

        if test_pass:
            print("Minimax Test: Runs Successfully!")
    except NotImplementedError:
        print('Minimax Test: Not implemented')
    except:
        print('Minimax Test: ERROR OCCURRED')
        print(traceback.format_exc())

    print()

    """Example test you can run
    to make sure your AI does better
    than random."""

    print("")
    try:
        r = RandomPlayer()
        h = HumanPlayer()
        game = Board(r, h, 7, 7)
        output_b = game.copy()
        winner, move_history, termination = game.play_isolation(time_limit=1000, print_moves=True)
        print("\n", winner, " has won. Reason: ", termination)
        # Uncomment to see game
        # print game_as_text(winner, move_history, termination, output_b)
    except NotImplementedError:
        print('CustomPlayer Test: Not Implemented')
    except:
        print('CustomPlayer Test: ERROR OCCURRED')
        print(traceback.format_exc())


if __name__ == "__main__":
    main()
