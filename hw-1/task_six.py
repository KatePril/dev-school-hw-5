def get_integer_list(number):
    list_int = []
    for el in str(number):
        list_int.append(int(el))
    return list_int


def bubble_sort(list):
    length = len(list)
    for i in range(length):
        for j in range(1, length-i):
            if list[j] > list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
    return list


def execute_task_six(number):
    list_int = get_integer_list(number)
    list_int = bubble_sort(list_int)
    output = "".join([str(x) for x in list_int])
    return int(output)
