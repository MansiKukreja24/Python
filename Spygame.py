def spy_game(num):
    code = [0, 0, 7, 'x']
    for a in num:
        if a == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1, 2, 0, 0, 2, 7, 1]))
