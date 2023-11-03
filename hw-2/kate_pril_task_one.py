def execute_task_one(n, d):
    divisor = int(len(n) / d)
    tmp_honour_sums = [list() for i in range(divisor)]
    count = 0
    for el in n:
        tmp_honour_sums[count].append(el)
        if count < divisor-1:
            count += 1
        else:
            count = 0
    honour_sums = [sum(x) for x in tmp_honour_sums]
    return max(honour_sums)