def get_next_unused_letter(columns):
    used_letters = set(letter for col in columns for letter in col if letter != '')
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in used_letters:
            return letter
    return None  # all letters are used (with >26 columns)


def absorb_columns(columns):
    absorbed = True
    while absorbed:
        absorbed = False
        for i, col1 in enumerate(columns):
            for j, col2 in enumerate(columns):
                if i != j:
                    indices1 = {index for index, letter in enumerate(col1) if letter != ''}
                    indices2 = {index for index, letter in enumerate(col2) if letter != ''}
                    if indices1.issubset(indices2):
                        absorbed = True
                        columns.pop(i)
                        break
            if absorbed:
                break       
    return columns



def compact_letter_display(significant_pairs, num_groups):
    columns = [['a'] * num_groups]
    for pair_idx, (i, j) in enumerate(significant_pairs):
        #print(f"\nProcessing significant pair: ({i}, {j})")
        connected = False
        for idx, column in enumerate(columns):
            #print(f"checking column {column}")
            if column[i] == column[j] and column[i] != '':
                connected = True
                new_letter = get_next_unused_letter(columns)
                #print(f"New letter: {new_letter}")
                new_column = column.copy() 
                new_column = [new_letter if column[i] != '' else '' for i in range(num_groups)]
                #print(f'New column: {new_column}')
                new_column[i] = ''
                column[j] = ''
                columns[idx] = column
                #print(f"columns after removing letters: {column} and {new_column}")
                columns.append(new_column)
                #print(f"columns after appending new column: {columns}")
                columns = absorb_columns(columns)
            if connected:
                break 

        #print(f"Current columns: {columns}")

    result = [''.join(columns[k][n] for k in range(len(columns)) if columns[k][n] != '') for n in range(num_groups)]
    print(f"Final result: {result}")
    return result

num_groups = 3
pairs_list = [
    [(0, 1)],
    [(0, 2)],
    [(1, 2)],
    [(0, 1), (0, 2)],
    [(0, 1), (1, 2)],
    [(0, 2), (1, 2)],
    [(0, 1), (0, 2), (1, 2)]
]

for significant_pairs in pairs_list:
    print(f"\nTesting pairs: {significant_pairs}")
    cld_result = compact_letter_display(significant_pairs, num_groups)


