def get_current_idx(i, j, width):
    return (width*i)+j

def get_next_node_pos(right_slots):
    for idx, slot in enumerate(right_slots):
        if slot == '0':
            return idx + 1
    return -1


def solve_there_is_no_spoon_problem(input_matrix: list):
    width = len(input_matrix[0])
    height = len(input_matrix)
    matrix = [[] for _ in range(width*height)]
    for i in range(height):
        line = input_matrix[i]  # width characters, each either 0 or .
        for j in range(width):
            current_idx = get_current_idx(i, j, width)
            if line[j] == '0':
                matrix[current_idx].append(f'{j} {i}')
            
                # For right neighbour (do it immediately)
                next_node_pos = get_next_node_pos(line[j+1:])
                matrix[current_idx].append(f'{j+next_node_pos} {i}') if ((next_node_pos > 0) and (j+next_node_pos) < width) else matrix[current_idx].append('-1 -1')
                
                # For bottom neighbour (do it retroactively once found)
                if (i > 0):
                    n = 1
                    while (i-n) >= 0:
                        previous_idx = get_current_idx(i-n, j, width)
                        if len(matrix[previous_idx]) < 3:
                            matrix[previous_idx].append(f'{j} {i}')
                        n+=1
            else:
                matrix[current_idx].append(f'-1 -1') # This line is to keep track of an empty cell

    results = []
    for i in range(width*height):
        while len(matrix[i]) < 3: # by now, if the neighbours are unknown, it means they are none.
            matrix[i].append('-1 -1')
        if (matrix[i][0]) != '-1 -1':
            results.append(' '.join(matrix[i]))
    
    return results


if __name__ == '__main__':
    ## Example
    input_matrix = [
        '0.0',
        '...',
        '0.0'
    ]
    res = solve_there_is_no_spoon_problem(input_matrix)
    print(f'Result:\n{"\n".join(res)}')
