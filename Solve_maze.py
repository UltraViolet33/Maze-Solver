import random 
from settings import *
import pygame as pg


class SolveMaze:
    def __init__(self, elem_maze, draw):
        self.draw = draw
        self.cur_x = 1
        self.cur_y = 1
        self.elem_list = elem_maze
        self.maze_width = MAZE_WIDTH * 2 + 1
        self.maze_height = MAZE_HEIGHT * 2 + 1
        self.solve_path = []
        self.is_solve = False
        self.goal_x = 19
        self.goal_y = 19
        self.direction = 0

    def solve(self):
        while not self.is_solve:
            self.elem_list[self.cur_x][self.cur_y] = 5
            pg.time.delay(50)  # Add a small delay to visualize the final maze
            self.draw()

            if self.cur_x == self.goal_x and self.cur_y == self.goal_y:
                self.is_solve = True
                return True
            possibles_moves = self.check_valid_moves()

    #     print(possibles_moves)
            if len(possibles_moves):
                self.direction = random.choice(possibles_moves)
                if len(possibles_moves) > 1:
                    self.solve_path.append([self.cur_x, self.cur_y])
                self.set_solution_path()
            else:
                if not self.solve_path:
                    return False
    #         # Print the contents of solve_path for debugging
    #         print("solve_path:", solve_path)

                path = random.choice(self.solve_path)
                self.solve_path.remove(path)
                self.cur_x = path[0]
                self.cur_y = path[1]

    # return False

    def check_valid_moves(self):
        temp_list = []

        if self.cur_x + 1 != self.maze_width - 1:
            if (
                self.elem_list[self.cur_x + 1][self.cur_y] != 1
                and self.elem_list[self.cur_x + 1][self.cur_y] != 5
            ):
                temp_list.append(0)

        if self.cur_y + 1 != self.maze_height - 1:
            if (
                self.elem_list[self.cur_x][self.cur_y + 1] != 1
                and self.elem_list[self.cur_x][self.cur_y + 1] != 5
            ):
                temp_list.append(1)

        if self.cur_x - 1 != 0:
            if (
                self.elem_list[self.cur_x - 1][self.cur_y] != 1
                and self.elem_list[self.cur_x - 1][self.cur_y] != 5
            ):
                temp_list.append(2)

        if self.cur_y - 1 != 0:
            if (
                self.elem_list[self.cur_x][self.cur_y - 1] != 1
                and self.elem_list[self.cur_x][self.cur_y - 1] != 5
            ):
                temp_list.append(3)

        return temp_list
    
    def set_solution_path(self):
        if self.direction == 0:
            self.elem_list[self.cur_x + 1][self.cur_y] = 5
            self.cur_x += 2
        if self.direction == 1:
            self.elem_list[self.cur_x][self.cur_y + 1] = 5
            self.cur_y += 2
        if self.direction == 2:
            self.elem_list[self.cur_x - 1][self.cur_y] = 5
            self.cur_x -= 2
        if self.direction == 3:
            self.elem_list[self.cur_x][self.cur_y - 1] = 5
            self.cur_y -= 2
