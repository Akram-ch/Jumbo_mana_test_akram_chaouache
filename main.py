from matrix import Matrix
from utils import *

matrix = Matrix()

epsilon = 0.9 
discount_factor = 0.9 
learning_rate = 0.9 

for episode in range(1000):
    row_index, column_index = get_starting_location(matrix)
    
    while not is_terminal_state(matrix, row_index, column_index):
        action_index = get_next_action(matrix, row_index, column_index, epsilon)
        
        old_row_index, old_column_index = row_index, column_index
        row_index, column_index = get_next_location(matrix, row_index, column_index, action_index)
        
        #recieve the reward for moving to a new state and calculate the temporal difference
        reward = matrix.rewards[row_index, column_index]
        old_q_value = matrix.q_values[old_row_index, old_column_index, action_index]
        temporal_difference = reward + (discount_factor * np.max(matrix.q_values[row_index, column_index])) - old_q_value

        #update the Q-value for the previous state and action pair
        new_q_value = old_q_value + (learning_rate * temporal_difference)
        matrix.q_values[old_row_index, old_column_index, action_index] = new_q_value

print("training complete!")

print(get_shortest_path(matrix,11, 8))