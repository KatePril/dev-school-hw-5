def is_prime(n, i):
    if n == i:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)


def execute_task_four(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True
