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
            if openers != [] and bracket == openers_to_closers[openers[len(openers) - 1]]:
                openers.pop()
            else:
                return False

    return openers == []
