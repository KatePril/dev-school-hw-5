def find_n(obj, key, n):
    output = False
    tmp_obj = obj.get(key)
    if isinstance(tmp_obj, list):
        if n in tmp_obj:
            output = True
            return output
    else:
        for key_1 in tmp_obj.keys():
            output = find_n(tmp_obj, key_1, n)
            if output:
                return output
    return output


def execute_task_five(obj, n):
    for key in obj.keys():
        if find_n(obj, key, n):
            return key
    return None
