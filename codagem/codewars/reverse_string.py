def reverse(input):
    string_length = len(input)
    reversed_string = ''
    while string_length:
        string_length-= 1
        reversed_string+= input[string_length]

    return reversed_string
