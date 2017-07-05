def reverse(string_to_revert):
    string_length = len(string_to_revert)
    reversed_string = ''
    while string_length:
        string_length-= 1
        reversed_string+= string_to_revert[string_length]

    return reversed_string
