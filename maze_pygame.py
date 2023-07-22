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

# solve_path = []

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

    # print(len(elem_list))
    # print(elem_list[20][20])

    find_path()


# def solve_maze(x, y):
#     solve = False
#     # check if the cell is the solution


#     while not solve:
#         if x == 20 and y == 20:
#             solve = True
#             return True

#         # mark as visited the cell
#         elem_list[x][y] = 5

#         possibles_moves = check_valid_moves(x, y)
#         if len(possibles_moves):
#             direction_solve = random.choice(possibles_moves)
#             if len(possibles_moves) > 1:
#                 solve_path.append([x, y])
#             x, y = set_solution_path(x, y, direction_solve)
#         else:
#                 # print("path list : ", path_list)
#                 # print("Possible list : ", possible_list)

#             path = random.choice(solve_path)
#             solve_path.remove(path)
#             x = path[0]
#             y = path[1]

# if yes return true
# else
# possibles moves

# take one move

# mark as visited and repeat


def solve_maze(x, y):
    solve_path = []  # Make sure solve_path is initialized
    solve = False


    while not solve:
        elem_list[x][y] = 5
        if x == 19 and y == 19:
            solve = True
            return True
        
        # pygame.display.update()

        
        print("x ",x)
        print("y ", y)

          # Mark as visited
        pygame.time.delay(50)  # Add a small delay to visualize the final maze
        draw_maze()

        possibles_moves = check_valid_moves(x, y)
        print(possibles_moves)
        if len(possibles_moves):
            direction_solve = random.choice(possibles_moves)
            if len(possibles_moves) > 1:
                solve_path.append([x, y])
            x, y = set_solution_path(x, y, direction_solve)
        else:
            if not solve_path:
                return False
            # Print the contents of solve_path for debugging
            print("solve_path:", solve_path)

            path = random.choice(solve_path)
            solve_path.remove(path)
            x = path[0]
            y = path[1]

    

    return False


def set_solution_path(x, y, direction):
    if direction == 0:
        elem_list[x + 1][y] = 5
        x += 2
    if direction == 1:
        elem_list[x][y + 1] = 5
        y += 2
    if direction == 2:
        elem_list[x - 1][y] = 5
        x -= 2
    if direction == 3:
        elem_list[x][y - 1] = 5
        y -= 2

    return (x, y)


def check_valid_moves(x, y):
    temp_list = []

    if x + 1 != maze_width - 1:
        if elem_list[x + 1][y] != 1 and elem_list[x + 1][y] != 5:
            temp_list.append(0)

    if y + 1 != maze_height - 1:
        if elem_list[x][y + 1] != 1 and elem_list[x][y + 1] != 5:
            temp_list.append(1)

    if x - 1 != 0:
        if elem_list[x - 1][y] != 1 and elem_list[x - 1][y] != 5:
            temp_list.append(2)

    if y - 1 != 0:
        if elem_list[x][y - 1] != 1 and elem_list[x][y - 1] != 5:
            temp_list.append(3)

    return temp_list


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
            # print("path list : ", path_list)
            # print("Possible list : ", possible_list)

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
    for y in range(maze_height):  # Iterate through y first
        for x in range(maze_width):  # Then iterate through x

            if elem_list[y][x] == 1:
                color = (0, 0, 0)  # Wall cell
            elif elem_list[y][x] in [2, 3]:
                color = (255, 255, 255)  # Empty cell
            elif elem_list[y][x] == 5:
                color = (255, 255, 0)  # Solution path cell

            # Goal cell
            if x == 19 and y == 19:
                color = (255, 0, 0)

            pygame.draw.rect(
                screen,
                color,
                (x * cell_width, y * cell_height, cell_width, cell_height),
            )
    pygame.display.flip()


           

def check_valid():
    temp_list = []

    if cur_x + 1 != maze_width - 1:
        # print(cur_x)
        if elem_list[cur_x + 1][cur_y] != 3 and elem_list[cur_x + 2][cur_y] != 2:
            temp_list.append(0)

    if cur_y + 1 != maze_height - 1:
        # print(cur_y + 1)
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
    # pygame.time.delay(1000)  # Add a small delay to visualize the final maze

    print(elem_list)
    print(solve_maze(1, 1))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
    pygame.quit()
