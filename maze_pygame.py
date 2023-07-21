import pygame
import random

y = 10
x = 10
maze_width = x * 2 + 1
maze_height = y * 2 + 1

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Random Maze Generation using Randomized Prim's")

path_list = []

elem_list = []
direction = 0

cur_x = 1
cur_y = 1
zero_amount = y * x


def generate():
    for i in range(0, maze_width):
        elem_list.append([])
        for j in range(0, maze_height):
            if (
                i in [0, maze_width - 1]
                or j in [0, maze_height - 1]
                or i % 2 == 0
                or j % 2 == 0
            ):
                elem_list[i].append(1)
            else:
                elem_list[i].append(0)

    print(elem_list)

    find_path()


def find_path():
    global direction
    global cur_x
    global cur_y
    elem_list[cur_x][cur_y] = 2
    global zero_amount
    zero_amount -= 1
    while zero_amount > 0:
        possible_list = check_valid()
        if len(possible_list):
            direction = random.choice(possible_list)
            if len(possible_list) > 1:
                path_list.append([cur_x, cur_y])
            set_path()
            zero_amount -= 1
        else:
            print("path list : ", path_list)
            print("Possible list : ", possible_list)

            path = random.choice(path_list)
            path_list.remove(path)
            cur_x = path[0]
            cur_y = path[1]


def set_path():
    global cur_x
    global cur_y
    global direction

    if direction == 0:
        elem_list[cur_x + 1][cur_y] = 3
        elem_list[cur_x + 2][cur_y] = 2
        cur_x += 2
    if direction == 1:
        elem_list[cur_x][cur_y + 1] = 3
        elem_list[cur_x][cur_y + 2] = 2
        cur_y += 2
    if direction == 2:
        elem_list[cur_x - 1][cur_y] = 3
        elem_list[cur_x - 2][cur_y] = 2
        cur_x -= 2
    if direction == 3:
        elem_list[cur_x][cur_y - 1] = 3
        elem_list[cur_x][cur_y - 2] = 2
        cur_y -= 2


def draw_maze():
    cell_width, cell_height = screen_width // maze_width, screen_height // maze_height
    for y in range(maze_height):
        for x in range(maze_width):
            color = (0, 0, 0) if elem_list[y][x] == 1 else (255, 0, 0)
            pygame.draw.rect(
                screen,
                color,
                (x * cell_width, y * cell_height, cell_width, cell_height),
            )
    pygame.display.flip()


def check_valid():
    temp_list = []

    if cur_x + 1 != maze_width - 1:
        print(cur_x)
        if elem_list[cur_x + 1][cur_y] != 3 and elem_list[cur_x + 2][cur_y] != 2:
            temp_list.append(0)

    if cur_y + 1 != maze_height - 1:
        print(cur_y + 1)
        if elem_list[cur_x][cur_y + 1] != 3 and elem_list[cur_x][cur_y + 2] != 2:
            temp_list.append(1)

    if cur_x - 1 != 0:
        if elem_list[cur_x - 1][cur_y] != 3 and elem_list[cur_x - 2][cur_y] != 2:
            temp_list.append(2)

    if cur_y - 1 != 0:
        if elem_list[cur_x][cur_y - 1] != 3 and elem_list[cur_x][cur_y - 2] != 2:
            temp_list.append(3)

    return temp_list


def main():
    generate()
    draw_maze()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
    pygame.quit()
