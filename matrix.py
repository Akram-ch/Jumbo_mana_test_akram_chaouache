import numpy as np
#Defining the environment
class Matrix():
    
    def __init__(self):

        self.matrix_rows = 12
        self.matrix_columns = 12
        self.q_values = np.zeros((self.matrix_rows, self.matrix_columns, 4))
        self.actions = ['up', 'right', 'down', 'left']
        self.rewards = np.full((self.matrix_rows, self.matrix_columns), -1)
        
        self.rewards[5, 3] = 100
        self.rewards[5, 2] = 80

        self.obstacles = {}
        self.obstacles[1] = [(4,1), (2,2), (3,2), (4,2), (2,3), (3,3), (4,3), (3,4), (4,4)]
        self.obstacles[2] = [(8,1), (9,1), (7,2), (8,2), (9,2), (7,3), (8,3), (9,3), (7,4), (8,4), (9,4), (10,4)]
        self.obstacles[3] = [(2,7), (3,7), (4,7), (2,8), (3,8), (4,8), (2,9), (3,9), (4,9), (2,10)]
        self.obstacles[4] = [(7,7), (8,7), (7,8), (8,8), (9,8), (7,9), (8,9), (9,9), (7,10)]
        
        for obstacle in self.obstacles:
            for square in self.obstacles[obstacle]:
                self.rewards[square[0]][square[1]] = -100


#defining actions
# 0 = up, 1 = right, 2 = down, 3 = left

#Defining rewards

#Defining self.obstacles

# player = (7,5)
# goal = (8,5)



