def execute_task_two(arr):
    for i in range(len(arr)):
        if i == 0:
            if 0 == sum(arr[1:len(arr)]):
                return 0
        elif i == len(arr) - 1:
            if 0 == sum(arr[0: len(arr) - 1]):
                return len(arr) - 1
        else:
            if sum(arr[0:i]) == sum(arr[i+1:len(arr)]):
                return i
    return -1