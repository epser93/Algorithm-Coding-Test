def isWall(row, col):
    if 0 <= row < 8 and 0 <= col < 8:
        return False
    return True

def move(row_direction, col_direction):
    global king_row, king_col, rock_row, rock_col
    if isWall(king_row+row_direction, king_col+col_direction):
        return
    king_row += row_direction
    king_col += col_direction
    if king_row == rock_row and king_col == rock_col:
        if isWall(rock_row+row_direction, rock_col+col_direction):
            king_row -= row_direction
            king_col -= col_direction
            return
        rock_row += row_direction
        rock_col += col_direction
    
king_location, rock_location, N = input().split()
commands = [input() for _ in range(int(N))]
king_row, king_col = 8-int(king_location[1:]), ord(king_location[0])-65
rock_row, rock_col = 8-int(rock_location[1:]), ord(rock_location[0])-65
for command in commands:
    if command == 'R':
        move(0, 1)
    elif command == "L":
        move(0, -1)
    elif command == "B":
        move(1, 0)
    elif command == "T":
        move(-1, 0)
    elif command == "RT":
        move(-1, 1)
    elif command == "LT":
        move(-1, -1)
    elif command == "RB":
        move(1, 1)
    elif command == "LB":
        move(1, -1)
print(chr(king_col+65) + str(8-king_row))
print(chr(rock_col+65) + str(8-rock_row))