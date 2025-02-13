import random
import math
import config

def spawn_target(board, snake):
    row = random.randint(1,len(board)-2)
    column = random.randint(1, len(board[3])-2)
    print(row, column)
    if([row, column] in snake):
        spawn_target(board,snake)
    board[row][column] = "a"

    return board, [row, column]

def board(rows, cols):
    board = []
    board.append((cols)*["─"])
    board[0].insert(0, "┌")
    board[0].append("┐")

    for i in range(0,rows):
        sub_board = []
        sub_board.append("│")
        for j in range(0,cols):
            sub_board.append(" ")
        sub_board.append("│")
        board.append(sub_board)
    board.append((cols)*["─"])
    board[-1].insert(0,"└")
    board[-1].append("┘")
    board[config.target[0]][config.target[1]] = "a"
    return board

def show(board, snake):
    
    for i in range(len(snake)):
        board[snake[i][0]][snake[i][1]]="1"

    for i in range(len(board)):
        print("".join(board[i]))

def move(board, snake, move, target_pos):
    
    row = move[0]
    col = move[1]
    snake.insert(0,[row, col])
    
    # print("row, col: ",row, col)
    if(board[row][col] =='a'):
        print("snake: ",snake)
        board[row][col]=" "
        board, target_pos = spawn_target(board, snake)
    else:
        board[snake[-1][0]][snake[-1][1]] = " "
        snake.pop()
    return board, snake, target_pos

def game_over(board, row,col):
    if(not 0<row<len(board)-1 or not 0<col<len(board[2])-1 or board[row][col]=="1"):
        print("Game Over")
        return True

    return False

def compute_distance(position, destination):
    distance = math.sqrt(((destination[0]-position[0])**2)+((destination[1]-position[1])**2))
    return int(distance)


def compute_destination(current_pos, difference):
    return current_pos + difference
