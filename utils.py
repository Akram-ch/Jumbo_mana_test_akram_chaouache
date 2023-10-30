import numpy as np
#Helper functions

def is_terminal_state(matrix,current_row_index, current_column_index):
    if matrix.rewards[current_row_index, current_column_index] == -1.:
        return False
    else:
        return True

def get_starting_location(matrix):
    current_row_index = np.random.randint(matrix.matrix_rows)
    current_column_index = np.random.randint(matrix.matrix_columns)
    while is_terminal_state(matrix, current_row_index, current_column_index):
        current_row_index = np.random.randint(matrix.matrix_rows)
        current_column_index = np.random.randint(matrix.matrix_columns)
    return current_row_index, current_column_index

def get_next_action(matrix,current_row_index, current_column_index, epsilon):
    if np.random.random() < epsilon:
        return np.argmax(matrix.q_values[current_row_index, current_column_index])
    else: #choose a random action
        return np.random.randint(4)

def get_next_location(matrix, current_row_index, current_column_index, action_index):
    new_row_index = current_row_index
    new_column_index = current_column_index
    
    if matrix.actions[action_index] == 'up' and current_row_index > 0:
        new_row_index -= 1
    elif matrix.actions[action_index] == 'right' and current_column_index < matrix.matrix_columns - 1:
        new_column_index += 1
    elif matrix.actions[action_index] == 'down' and current_row_index < matrix.matrix_rows - 1:
        new_row_index += 1
    elif matrix.actions[action_index] == 'left' and current_column_index > 0:
        new_column_index -= 1
    return new_row_index, new_column_index

def get_shortest_path(matrix, start_row_index, start_column_index):
    if is_terminal_state(matrix, start_row_index, start_column_index):
        return []
    else: 
        current_row_index, current_column_index = start_row_index, start_column_index
        shortest_path = []
        shortest_path.append([current_row_index, current_column_index])
        while not is_terminal_state(matrix, current_row_index, current_column_index):
            action_index = get_next_action(matrix, current_row_index, current_column_index, 1.)
            current_row_index, current_column_index = get_next_location(matrix, current_row_index, current_column_index, action_index)
            shortest_path.append([current_row_index, current_column_index])
    return shortest_path