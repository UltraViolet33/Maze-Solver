import random 
from settings import *
import pygame as pg

from util import Node, StackFrontier

class SolveDFS:

   
    def __init__(self, elem_maze, draw):
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

        frontier = StackFrontier()
        frontier.add(start)

        self.explored = set()

        while True:

            if frontier.empty():
                raise Exception("No solution")
            
            node = frontier.remove()

            self.num_explored += 1

            if node.state == self.goal:
                # actions = []
                # cells = []
                # while node.parent is not None:
                #     actions.append(node.action)
                #     cells.append(node.state)
                #     node = node.parent
                # actions.reverse()
                # cells.reverse()
                # self.solution = (actions, cells)
                return
            
            self.explored.add(node.state)
            x, y = node.state
            self.elem_list[x][y] = 5
            pg.time.delay(50)
            self.draw()

            for action, state in self.get_neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)





# def solve(self):
#     while not self.is_solve:
#         self.elem_list[self.cur_x][self.cur_y] = 5
#         pg.time.delay(50)  # Add a small delay to visualize the final maze
#         self.draw()

#         if self.cur_x == self.goal_x and self.cur_y == self.goal_y:
#             self.is_solve = True
#             return True
#         possibles_moves = self.check_valid_moves()

# #     print(possibles_moves)
#         if len(possibles_moves):
#             self.direction = random.choice(possibles_moves)
#             if len(possibles_moves) > 1:
#                 self.solve_path.append([self.cur_x, self.cur_y])
#             self.set_solution_path()
#         else:
#             if not self.solve_path:
#                 return False
# #         # Print the contents of solve_path for debugging
# #         print("solve_path:", solve_path)

#             path = random.choice(self.solve_path)
#             self.solve_path.remove(path)
#             self.cur_x = path[0]
#             self.cur_y = path[1]

# # return False


    def get_neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            # if 0 <= r < self.maze_height and 0 <= c < self.maze_width and not self.walls[r][c]:
            if 0 <= r < self.maze_height and 0 <= c < self.maze_width and  self.elem_list[r][c] != 1:

                result.append((action, (r, c)))
        return result

# def check_valid_moves(self):
#     temp_list = []

#     if self.cur_x + 1 != self.maze_width - 1:
#         if (
#             self.elem_list[self.cur_x + 1][self.cur_y] != 1
#             and self.elem_list[self.cur_x + 1][self.cur_y] != 5
#         ):
#             temp_list.append(0)

#     if self.cur_y + 1 != self.maze_height - 1:
#         if (
#             self.elem_list[self.cur_x][self.cur_y + 1] != 1
#             and self.elem_list[self.cur_x][self.cur_y + 1] != 5
#         ):
#             temp_list.append(1)

#     if self.cur_x - 1 != 0:
#         if (
#             self.elem_list[self.cur_x - 1][self.cur_y] != 1
#             and self.elem_list[self.cur_x - 1][self.cur_y] != 5
#         ):
#             temp_list.append(2)

#     if self.cur_y - 1 != 0:
#         if (
#             self.elem_list[self.cur_x][self.cur_y - 1] != 1
#             and self.elem_list[self.cur_x][self.cur_y - 1] != 5
#         ):
#             temp_list.append(3)

#     return temp_list

# def set_solution_path(self):
#     if self.direction == 0:
#         self.elem_list[self.cur_x + 1][self.cur_y] = 5
#         self.cur_x += 2
#     if self.direction == 1:
#         self.elem_list[self.cur_x][self.cur_y + 1] = 5
#         self.cur_y += 2
#     if self.direction == 2:
#         self.elem_list[self.cur_x - 1][self.cur_y] = 5
#         self.cur_x -= 2
#     if self.direction == 3:
#         self.elem_list[self.cur_x][self.cur_y - 1] = 5
#         self.cur_y -= 2
