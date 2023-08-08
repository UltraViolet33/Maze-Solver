import pygame as pg
import sys
from settings import *
import random
from Solve_maze import SolveMaze
from SolveDFS import SolveDFS


class Maze:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        pg.display.set_caption("Generation and solving maze using DFS")
        self.clock = pg.time.Clock()

        self.maze_width = MAZE_WIDTH * 2 + 1
        self.maze_height = MAZE_HEIGHT * 2 + 1
        self.elem_list = []
        self.zero_amount = 0
        self.cur_x = 1
        self.cur_y = 1
        self.direction = 0
        self.path_list = []
        self.zero_amount = MAZE_HEIGHT * MAZE_WIDTH
        self.goal_x = self.maze_width - 2
        self.goal_y = self.maze_height - 2

    def generate(self):
        for i in range(0, self.maze_width):
            self.elem_list.append([])
            for j in range(0, self.maze_height):
                if (
                    i in [0, self.maze_width - 1]
                    or j in [0, self.maze_height - 1]
                    or i % 2 == 0
                    or j % 2 == 0
                ):
                    self.elem_list[i].append(1)
                else:
                    self.elem_list[i].append(0)
        self.find_path()

    def find_path(self):
        self.elem_list[self.cur_x][self.cur_y] = 2
        self.zero_amount -= 1
        while self.zero_amount > 0:
            possible_list = self.check_valid()
            if len(possible_list):
                self.direction = random.choice(possible_list)
                if len(possible_list) > 1:
                    self.path_list.append([self.cur_x, self.cur_y])
                self.set_path()
                self.zero_amount -= 1
            else:
                path = random.choice(self.path_list)
                self.path_list.remove(path)
                self.cur_x = path[0]
                self.cur_y = path[1]

    def check_valid(self):
        temp_list = []

        if self.cur_x + 1 != self.maze_width - 1:
            if (
                self.elem_list[self.cur_x + 1][self.cur_y] != 3
                and self.elem_list[self.cur_x + 2][self.cur_y] != 2
            ):
                temp_list.append(0)

        if self.cur_y + 1 != self.maze_height - 1:
            if (
                self.elem_list[self.cur_x][self.cur_y + 1] != 3
                and self.elem_list[self.cur_x][self.cur_y + 2] != 2
            ):
                temp_list.append(1)

        if self.cur_x - 1 != 0:
            if (
                self.elem_list[self.cur_x - 1][self.cur_y] != 3
                and self.elem_list[self.cur_x - 2][self.cur_y] != 2
            ):
                temp_list.append(2)

        if self.cur_y - 1 != 0:
            if (
                self.elem_list[self.cur_x][self.cur_y - 1] != 3
                and self.elem_list[self.cur_x][self.cur_y - 2] != 2
            ):
                temp_list.append(3)

        return temp_list

    def set_path(self):
        if self.direction == 0:
            self.elem_list[self.cur_x + 1][self.cur_y] = 3
            self.elem_list[self.cur_x + 2][self.cur_y] = 2
            self.cur_x += 2
        if self.direction == 1:
            self.elem_list[self.cur_x][self.cur_y + 1] = 3
            self.elem_list[self.cur_x][self.cur_y + 2] = 2
            self.cur_y += 2
        if self.direction == 2:
            self.elem_list[self.cur_x - 1][self.cur_y] = 3
            self.elem_list[self.cur_x - 2][self.cur_y] = 2
            self.cur_x -= 2
        if self.direction == 3:
            self.elem_list[self.cur_x][self.cur_y - 1] = 3
            self.elem_list[self.cur_x][self.cur_y - 2] = 2
            self.cur_y -= 2

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
                sys.exit()

    def draw_maze(self):
        cell_width, cell_height = WIDTH // self.maze_width, HEIGHT // self.maze_height
        for y in range(self.maze_height):
            for x in range(self.maze_width):
                if self.elem_list[y][x] == 1:
                    color = (0, 0, 0)  # Wall cell
                elif self.elem_list[y][x] in [2, 3]:
                    color = (255, 255, 255)  # Empty cell
                elif self.elem_list[y][x] == 5:
                    color = (0, 255, 0)  # Solution path cell

                # Goal cell
                if x == self.goal_x and y == self.goal_y:
                    color = (255, 0, 0)

                pg.draw.rect(
                    self.screen,
                    color,
                    (x * cell_width, y * cell_height, cell_width, cell_height),
                )
        pg.display.flip()

    def run(self):
        print(self.maze_width)
        print(self.maze_height)

        self.generate()
        self.draw_maze()
        # solve = SolveMaze(elem_maze=self.elem_list, draw=self.draw_maze)
        solve = SolveDFS(elem_maze=self.elem_list, draw=self.draw_maze)
        # solve = SolveMaze(ele)

        solve.solve()
        while True:
            self.check_events()
