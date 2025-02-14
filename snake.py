import random
import math
import config
import keyboard
import time
import pygame

def spawn_target(grid_size, snake):
    row = random.randint(0,grid_size-1)
    column = random.randint(0,grid_size-1)
    print(row, column)
    if([row, column] in snake):
        spawn_target(grid_size,snake)

    return [row, column]

def move(grid_size, snake, move, target_pos):
    
    row = move[0]
    col = move[1]
    snake.insert(0,[row, col])
    
    if(move == target_pos):
        print("snake: ",snake)
        target_pos = spawn_target(grid_size, snake)
    else:
        snake.pop()
    return snake, target_pos

def game_over(grid_size, row,col, snake):
    if(not -1<row<grid_size or not -1<col<grid_size):
        print("Out Of Boundary")
        return True
    if([row, col] in snake):
        print("Collision with itself")
        return True

    return False

def compute_distance(position, destination):
    distance = math.sqrt(((destination[0]-position[0])**2)+((destination[1]-position[1])**2))
    return int(distance)


def compute_destination(current_pos, difference):
    return current_pos + difference


def on_key_press(event):
    global direct_key
    if event.name in list(config.direction.keys()):
        if(config.wrong_directions[config.direct_key] != event.name):
            config.direct_key = event.name


def display(snake, target, block_size,screen):

    for event in pygame.event.get():  # Process system events
        if event.type == pygame.QUIT:
            exit()
    screen.fill((0, 0, 0))  # Black background

        # Draw target
    pygame.draw.rect(screen, (255, 0, 0), 
                    (target[1] * block_size, target[0] * block_size, 
                    block_size, block_size))

        # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), 
                        (segment[1] * block_size, segment[0] * block_size, 
                        block_size, block_size))

        pygame.display.flip()

def main():
    
    keyboard.on_press(on_key_press)

    while True:
        
        grid_size = 20
        pygame.init()
        window_size = 450  
        block_size = window_size // grid_size
        screen = pygame.display.set_mode((window_size, window_size))
        display(config.snake, config.target, block_size, screen)

        to_row = compute_destination(config.snake[0][0],config.direction[config.direct_key][0])
        to_col = compute_destination(config.snake[0][1],config.direction[config.direct_key][1])


        if(game_over(grid_size, to_row, to_col, config.snake)):
            break
        config.snake, config.target= move(grid_size,config.snake, [to_row, to_col], config.target)

        print(config.snake)

        time.sleep(0.2)

# main()