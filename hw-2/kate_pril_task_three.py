def execute_task_three(arr):
    symbol_arr = [sorted([el for el in s]) for s in arr]
    group_indexes = [[0, ], ]
    for i in range(1, len(symbol_arr)):
        added = False
        for j in range(len(group_indexes)):
            if symbol_arr[i] == symbol_arr[group_indexes[j][0]]:
                group_indexes[j].append(i)
                added = True
                break
        if not added:
            group_indexes.append([i, ])

    prepared_output = [list() for i in range(len(group_indexes))]
    for i in range(len(group_indexes)):
        for j in range(len(group_indexes[i])):
            prepared_output[i].append(arr[group_indexes[i][j]])

    return prepared_output
