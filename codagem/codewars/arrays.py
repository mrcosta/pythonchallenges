def merge(first, second):
    ordered_list = []

    while first and second:
        if first[0] <= second[0]:
            ordered_list.append(first.pop(0))
        else:
            ordered_list.append(second.pop(0))

    ordered_list.extend(first) if first else ordered_list.extend(second)

    return ordered_list

