def balance(brackets):
    openers_to_closers = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    openers_symbols = ['{', '(', '[']
    openers = []

    for bracket in brackets:
        if bracket in openers_symbols:
           openers.append(bracket)
        else:
           last_opener = openers[len(openers) - 1]
           if bracket == openers_to_closers[last_opener]:
               openers.pop()
           else:
               return False

    return openers == []
