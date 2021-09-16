# Start with grid- grid should be a dictionary.


# Used on turn 5 and onwards


def check_for_winner(grid):
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 1 4 7
    # 2 5 8
    # 3 6 9
    # 1 5 9
    # 3 5 7

    if grid[1] == grid[2] and grid[2] == grid[3]:
        return grid[1]
    elif grid[4] == grid[5] and grid[5] == grid[6]:
        return grid[4]
    elif grid[7] == grid[8] and grid[8] == grid[9]:
        return grid[7]
    elif grid[7] == grid[8] and grid[8] == grid[9]:
        return grid[7]
    
    return " "

def print_grid(grid):
    print(f"{grid[1]} | {grid[2]} | {grid[3]}")
    print("-+-+-")
    print(f"{grid[4]} | {grid[5]} | {grid[6]}")
    print("-+-+-")
    print(f"{grid[7]} | {grid[8]} | {grid[9]}")

def execute_move(grid):
    while True:
        print_grid(grid)
        try:
            move = int(input(("You are playing as", turn,
                    "Select the space you want to fill:")))
        except (ValueError):
            print("Please Enter a Valid Number")
        else:
            if (move < 1) or (move > 9):
                print("Please Enter a Valid Number")
            elif grid[move] != " ":
                print("That move has been played, try again.")
            else:
                grid[move] = turn
                return

#####################################################
grid = {
    1: " ", 2: " ", 3: " ", 
    4: " ", 5: " ", 6: " ", 
    7: " ", 8: " ", 9: " ", 
}

turn = "X"  # X goes first
move_counter = 0  # move counter - Game ends at 9#this resets

while True:
    execute_move(grid)
    move_counter += 1

    winner = check_for_winner(grid)
    if winner != " ": 
        print("Winner is :" + winner)
    elif move_counter == 9:
        print("Tie")
    else: 
        turn = "O" if turn == "X" else "X"
