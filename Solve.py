from settings import *
import pygame as pg
from util import Node


class Solve:
    def __init__(self, frontier, elem_maze, draw):
        self.frontier = frontier
        self.draw = draw
        self.cur_x = 1
        self.cur_y = 1
        self.elem_list = elem_maze
        self.maze_width = MAZE_WIDTH * 2 + 1
        self.maze_height = MAZE_HEIGHT * 2 + 1
        self.solve_path = []
        self.is_solve = False
        self.goal_x = self.maze_width - 2
        self.goal_y = self.maze_height - 2
        self.direction = 0

        self.start = (self.cur_x, self.cur_y)
        self.goal = (self.goal_x, self.goal_y)

    def solve(self):
        self.num_explored = 0

        start = Node(state=self.start, parent=None, action=None)
        frontier = self.frontier
        frontier.add(start)

        self.explored = set()

        while True:
            if frontier.empty():
                raise Exception("No solution")

            node = frontier.remove()

            self.num_explored += 1

            if node.state == self.goal:
                return

            self.explored.add(node.state)
            x, y = node.state
            self.elem_list[x][y] = 5
            # pg.time.delay(50)
            self.draw()

            for action, state in self.get_neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def get_neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1)),
        ]

        result = []
        for action, (r, c) in candidates:
            # if 0 <= r < self.maze_height and 0 <= c < self.maze_width and not self.walls[r][c]:
            if (
                0 <= r < self.maze_height
                and 0 <= c < self.maze_width
                and self.elem_list[r][c] != 1
            ):
                result.append((action, (r, c)))
        return result
