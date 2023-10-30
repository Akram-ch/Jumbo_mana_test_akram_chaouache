import numpy as np
import matplotlib.pyplot as plt

#Defining the environment

matrix_rows = 12
matrix_columns = 12

q_values = np.zeros((matrix_rows, matrix_columns, 4))

#defining actions
# 0 = up, 1 = right, 2 = down, 3 = left
actions = ['up', 'right', 'down', 'left']

#Defining rewards
rewards = np.full((matrix_rows, matrix_columns), -1)

#Defining obstacles

# player = (7,5)
# goal = (8,5)

rewards[5, 3] = 100
rewards[5, 2] = 80

obstacles = {}
obstacles[1] = [(4,1), (2,2), (3,2), (4,2), (2,3), (3,3), (4,3), (3,4), (4,4)]
obstacles[2] = [(8,1), (9,1), (7,2), (8,2), (9,2), (7,3), (8,3), (9,3), (7,4), (8,4), (9,4), (10,4)]
obstacles[3] = [(2,7), (3,7), (4,7), (2,8), (3,8), (4,8), (2,9), (3,9), (4,9), (2,10)]
obstacles[4] = [(7,7), (8,7), (7,8), (8,8), (9,8), (7,9), (8,9), (9,9), (7,10)]

for obstacle in obstacles:
    for square in obstacles[obstacle]:
        rewards[square[0]][square[1]] = -100

#Helper functions

def is_terminal_state(current_row_index, current_column_index):
    if rewards[current_row_index, current_column_index] == -1.:
        return False
    else:
        return True

def get_starting_location():
    current_row_index = np.random.randint(matrix_rows)
    current_column_index = np.random.randint(matrix_columns)
    while is_terminal_state(current_row_index, current_column_index):
        current_row_index = np.random.randint(matrix_rows)
        current_column_index = np.random.randint(matrix_columns)
    return current_row_index, current_column_index

def get_next_action(current_row_index, current_column_index, epsilon):
    if np.random.random() < epsilon:
        return np.argmax(q_values[current_row_index, current_column_index])
    else: #choose a random action
        return np.random.randint(4)

def get_next_location(current_row_index, current_column_index, action_index):
    new_row_index = current_row_index
    new_column_index = current_column_index
    
    if actions[action_index] == 'up' and current_row_index > 0:
        new_row_index -= 1
    elif actions[action_index] == 'right' and current_column_index < matrix_columns - 1:
        new_column_index += 1
    elif actions[action_index] == 'down' and current_row_index < matrix_rows - 1:
        new_row_index += 1
    elif actions[action_index] == 'left' and current_column_index > 0:
        new_column_index -= 1
    return new_row_index, new_column_index

def get_shortest_path(start_row_index, start_column_index):
    if is_terminal_state(start_row_index, start_column_index):
        return []
    else: 
        current_row_index, current_column_index = start_row_index, start_column_index
        shortest_path = []
        shortest_path.append([current_row_index, current_column_index])
        while not is_terminal_state(current_row_index, current_column_index):
            action_index = get_next_action(current_row_index, current_column_index, 1.)
            current_row_index, current_column_index = get_next_location(current_row_index, current_column_index, action_index)
            shortest_path.append([current_row_index, current_column_index])
    return shortest_path

epsilon = 0.9 
discount_factor = 0.9 
learning_rate = 0.9 

for episode in range(1000):
    row_index, column_index = get_starting_location()
    
    while not is_terminal_state(row_index, column_index):
        action_index = get_next_action(row_index, column_index, epsilon)
        
        old_row_index, old_column_index = row_index, column_index
        row_index, column_index = get_next_location(row_index, column_index, action_index)
        
        #recieve the reward for moving to a new state and calculate the temporal difference
        reward = rewards[row_index, column_index]
        old_q_value = q_values[old_row_index, old_column_index, action_index]
        temporal_difference = reward + (discount_factor * np.max(q_values[row_index, column_index])) - old_q_value

        #update the Q-value for the previous state and action pair
        new_q_value = old_q_value + (learning_rate * temporal_difference)
        q_values[old_row_index, old_column_index, action_index] = new_q_value

print("training complete!")

print(get_shortest_path(11, 8))