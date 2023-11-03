def is_spoilt(package):
    sausage = package[0]
    for i in range(1, len(package)):
        if package[i] != sausage:
            return True
    return False


def unpack_sausages(track):
    output = ""
    if not track:
        return output
    sausages = []
    for box in track:
        if box:
            for package in box:
                if len(package) == 6:
                    if package[0] == "[" and package[5] == "]":
                        sausages.append(package)
    unpacked_sausages = [package[1:len(package) - 1] for package in sausages]
    filtered_sausages = []
    for package in unpacked_sausages:
        if not is_spoilt(package):
            filtered_sausages.append(package)
    ready_filtered_sausages = []
    count = 0
    for sausage in filtered_sausages:
        count += 1
        if count % 5 != 0:
            ready_filtered_sausages.append(sausage)

    if ready_filtered_sausages:
        for package in ready_filtered_sausages:
            for sausage in package:
                output += sausage + " "
        return output[0:len(output) - 1]
    return output