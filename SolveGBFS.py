from settings import *
import pygame as pg
from util import Node
from Solve import Solve


class SolveGBFS(Solve):

    def solve(self):
        self.num_explored = 0

        start = Node(state=self.start, parent=None, action=None)
        frontier = self.frontier
        frontier.add(start)

        self.explored = set()

        while True:
            if frontier.empty():
                raise Exception("No solution")

            if frontier.get_len() > 1:
                index = self.get_lowest_heuritic(frontier)
                node = frontier.frontier[index]
                frontier.remove(index)

            else:
                node = frontier.frontier[0]

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


    def get_lowest_heuritic(self, frontier):
        values = self.heuristics(frontier)
        min_index, min_value = values[0]

        for index, value in values:
            if value < min_value:
                min_index = index

        return min_index


    def heuristics(self, frontier):
        heuristic_values = []

        i = 0
        for node in frontier.frontier:
            x, y = node.state
            values = self.manhattan(x, y)
            heuristic_values.append((i, values))
            i += 1

        return heuristic_values
    

    def manhattan(self, xa, ya):
        xb, yb = self.goal
        return abs(xb - xa) + abs(yb - ya)
