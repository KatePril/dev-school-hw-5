a = ['XOOXO',
     'XOOXO',
     'OOOXO',
     'XXOXO',
     'OXOOO']


def find_neighbours(arr, i, j):
    count = 0
    if i > 0:
        if arr[i - 1][j] == "X":
            count += 1
    if i < len(arr) - 1:
        if arr[i + 1][j] == "X":
            count += 1
    if j > 0:
        if arr[i][j - 1] == "X":
            count += 1
    if j < len(arr[i]) - 1:
        if arr[i][j + 1] == "X":
            count += 1
    return count


def execute_task_six(arr):
    number_of_neighbours = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "X":
                number_of_neighbours.append(find_neighbours(arr, i, j))

    cm_to_count = [4 - x for x in number_of_neighbours]
    return sum(cm_to_count)