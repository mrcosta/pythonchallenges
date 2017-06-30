def unique_in_order(input):
    unique_in_order = []
    for element in input:
        if not unique_in_order or element != unique_in_order[-1]:
            unique_in_order.append(element)
    
    return unique_in_order

