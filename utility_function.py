import random


class PlayerSymbols:
    PLAYER_1_SYMBOL = 'X'
    PLAYER_2_SYMBOL = 'O'


def initialize_game_board():
    """Return the initial game board."""
    return """
             _______________________________
            |         |          |          |
            |    7    |     8    |     9    |
            |_________|__________|__________|
            |         |          |          |
            |    4    |     5    |     6    |
            |_________|__________|__________|
            |         |          |          |
            |    1    |     2    |     3    |
            |_________|__________|__________|
    """


def clear_space(space, player_symbol, board):
    """Replace an empty space on the board with the player's symbol."""
    updated_board = board.replace(space, player_symbol, 1)
    return updated_board


def show_board(board):
    """Print the current state of the game board."""
    print(board)


def check_for_winner(player_choices, player_name):
    winning_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
                       [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Convert player_choices to a set for easier comparison
    player_set = set(player_choices)

    # Check if any winning combination is a subset of the player's choices
    for combo in winning_numbers:
        if set(combo).issubset(player_set):
            print(f"Winner: {player_name}, Winning choices: {combo}")
            return True

    return False


def introduction():
    """Display an introduction message and prompt the user to choose a game mode."""
    print("Welcome to Tic-Tac-Toe!\n")
    print("Game Options:\n1. Player vs Bot\n2. Player vs Player\n")
    choice = input("Please choose option 1 or 2: ")
    return choice


def initiative_choice():
    """Randomly determine which player has the initiative."""
    choice = random.randint(1, 100)
    return "Player 1" if choice > 50 else "Player 2"


def play_again():
    """Ask the user if they would like to play again"""
    return input("Do you want to play again? (y/n): ").lower() == "y"


def clear_screen():
    print("\n" * 20)


def tic_tac_toe():
    """Run the Tic-Tac-Toe game."""
    player_1 = PlayerSymbols.PLAYER_1_SYMBOL
    player_2 = PlayerSymbols.PLAYER_2_SYMBOL

    player1_choices = []
    player2_choices = []

    game_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_board = initialize_game_board()
    game_mode = introduction()

    game_active = True
    while game_active:
        if game_mode == "1":
            print("Game Mode Selected: BOT GAME!\n")
            current_player = initiative_choice()
            print(f"{current_player} has won initiative!\n")
            show_board(game_board)

            for _ in range(1, 10):
                if current_player == "Player 1":
                    choice = input("Player 1, choose a number on the board to place your mark: ")
                    try:
                        choice = int(choice)
                        if choice in game_spaces:
                            player1_choices.append(choice)
                            game_board = clear_space(str(choice), player_1, game_board)
                            game_spaces.remove(choice)
                            show_board(game_board)
                            # Check for a winner after each move
                            if check_for_winner(player1_choices, "Player 1"):
                                print("Player 1 wins!")
                                game_active = False  # End the game
                                break
                            else:
                                if len(game_spaces) == 0:
                                    print("Game Over! It is a tie! Good game!")
                                    game_active = False
                                    break
                            current_player = "Player 2"
                        else:
                            print("Please look at the board and select an empty space!")
                    except ValueError:
                        print("Invalid input! Please enter a number.")
                else:
                    print("It is the AI's turn to make a move!")
                    choice = random.choice(game_spaces)
                    player2_choices.append(choice)
                    game_board = clear_space(str(choice), player_2, game_board)
                    game_spaces.remove(choice)
                    show_board(game_board)
                    # Check for a winner after each move
                    if check_for_winner(player2_choices, "AI Wins"):
                        print("Player 2 wins!")
                        game_active = False  # End the game
                        break
                    else:
                        if len(game_spaces) == 0:
                            print("Game Over! It is a tie! Good game!")
                            game_active = False
                            break
                    current_player = "Player 1"

        elif game_mode == "2":
            print("Game Mode Selected: Player vs Player!\n")
            current_player = initiative_choice()
            print(f"{current_player} has won initiative!\n")
            show_board(game_board)

            for _ in range(1, 10):
                if current_player == "Player 1":
                    choice = input("Player 1, choose a number on the board to place your mark: ")
                    try:
                        choice = int(choice)
                        if choice in game_spaces:
                            player1_choices.append(choice)
                            game_board = clear_space(str(choice), player_1, game_board)
                            game_spaces.remove(choice)
                            show_board(game_board)
                            # Check for a winner after each move
                            if check_for_winner(player1_choices, "Player 1"):
                                print("Player 1 wins!")
                                game_active = False  # End the game
                                break
                            else:
                                if len(game_spaces) == 0:
                                    print("Game Over! It is a tie! Good game!")
                                    game_active = False
                                    break
                            current_player = "Player 2"
                        else:
                            print("Please look at the board and select an empty space!")
                    except ValueError:
                        print("Invalid input! Please enter a number.")

                elif current_player == "Player 2":
                    choice = input("Player 2, choose a number on the board to place your mark: ")
                    try:
                        choice = int(choice)
                        if choice in game_spaces:
                            player2_choices.append(choice)
                            game_board = clear_space(str(choice), player_2, game_board)
                            game_spaces.remove(choice)
                            show_board(game_board)
                            # Check for a winner after each move
                            if check_for_winner(player2_choices, "Player 2"):
                                print("Player 2 wins!")
                                game_active = False  # End the game
                                break
                            else:
                                if len(game_spaces) == 0:
                                    print("Game Over! It is a tie! Good game!")
                                    game_active = False
                                    break
                            current_player = "Player 1"
                        else:
                            print("Please look at the board and select an empty space!")
                    except ValueError:
                        print("Invalid input! Please enter a number.")

    if play_again():
        clear_screen()
        tic_tac_toe()  # Start a new game session
    else:
        clear_screen()
        print("\nThanks for playing! Goodbye.")


# Run the game when this module is executed
if __name__ == "__main__":
    tic_tac_toe()
