def execute_task_three(m):
    n = 1
    while True:
        m -= n**3
        if m == 0:
            return n
        elif m < 0:
            return -1
        else:
            n += 1