def execute_task_five(str_nums):
    list_int = [int(x) for x in str_nums.split()]
    max_int = list_int[0]
    min_int = list_int[0]
    for el in list_int[1:len(str_nums)]:
        if el > max_int:
            max_int = el
        if el < min_int:
            min_int = el
    output = str(max_int) + " " + str(min_int)
    return output

