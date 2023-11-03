def execute_task_one(n):
    if n <= 0:
        return 0
    else:
        multiples = set()
        for i in range(1, n):
            if i % 3 == 0 or i % 5 == 0:
                multiples.add(i)
        return sum(multiples)
