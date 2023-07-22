

class SolveMaze():
    

    def __init__(self, elem_maze):
        self.cur_x = 1
        self.cur_y = 1
        self.elem_maze = elem_maze
        self.is_solve = False
        self.goal_x = 19
        self.goal_y = 19
        self.direction = 0


