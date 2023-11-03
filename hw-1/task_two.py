def move_disk(disks_num, n):
    n += 1
    if disks_num == 1:
        return n
    else:
        n = move_disk(disks_num-1, n)
        n = move_disk(disks_num-1, n)
        return n


def execute_task_two(n):
    return move_disk(n, 0)
